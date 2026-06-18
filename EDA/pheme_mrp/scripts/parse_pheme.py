import json
from pathlib import Path
import pandas as pd


# paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "pheme-rnr-dataset"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


records = [] #This will store all tweets, including source tweets and replies.

# Loop through events
for event_path in DATA_DIR.iterdir():

    if not event_path.is_dir():
        continue

    event_name = event_path.name

    # Rumours and non-rumours
    for label_folder in ["rumours", "non-rumours"]:

        label_path = event_path / label_folder #joining event path and label folder

        if not label_path.exists():
            continue

        label = 1 if label_folder == "rumours" else 0

        # Loop through threads
        for thread_path in label_path.iterdir():

            if not thread_path.is_dir():
                continue

            thread_id = thread_path.name

            # Source tweet + reactions in one pass
            for kind, subdir in [("source", "source-tweet"), ("reply", "reactions")]:

                d = thread_path / subdir

                if not d.exists():
                    continue

                for json_file in d.glob("*.json"):

                    with open(json_file, "r", encoding="utf-8") as f:
                        tweet = json.load(f)

                    # Attaching PHEME-level metadata to use in our work
                    tweet["event"] = event_name
                    tweet["label"] = label
                    tweet["label_name"] = label_folder
                    tweet["thread_id"] = thread_id
                    tweet["is_source_tweet"] = int(kind == "source")

                    records.append(tweet)


# Flatten nested dicts: user, entities etc.
df = pd.json_normalize(records, sep="_")


# Lightweight count columns for hashtags/urls/mentions/media
# the full lists are still kept in entities_* columns
def _len_or_zero(x):
    return len(x) if isinstance(x, list) else 0


for src, dst in [
    ("entities_hashtags", "n_hashtags"),
    ("entities_urls", "n_urls"),
    ("entities_user_mentions", "n_mentions"),
    ("entities_media", "n_media"),
    ("entities_symbols", "n_symbols"),
]:
    if src in df.columns:
        df[dst] = df[src].apply(_len_or_zero)
    else:
        df[dst] = 0


# Save Parquet (keeping everyting unchanged)
parquet_file = OUTPUT_DIR / "pheme_tweets.parquet"
df.to_parquet(parquet_file, index=False)


# Saving CSV too, but dropping columns that contain lists/dicts (cz CSV can't store them cleanly)
nested_cols = [
    c for c in df.columns
    if df[c].apply(lambda x: isinstance(x, (list, dict))).any()
]
csv_file = OUTPUT_DIR / "pheme_tweets.csv"
df.drop(columns=nested_cols).to_csv(
    csv_file, index=False, encoding="utf-8", quoting=1
)


print("=" * 50)
print("PHEME parsing complete")
print("=" * 50)
print(f"Rows:    {len(df):,}")
print(f"Columns: {len(df.columns)}  (CSV drops {len(nested_cols)} nested cols)")
print(f"Parquet: {parquet_file}")
print(f"CSV:     {csv_file}")
print("\nDropped from CSV (kept in Parquet):")
print(nested_cols)
print("\nFirst columns:")
print(df.columns.tolist()[:30])
