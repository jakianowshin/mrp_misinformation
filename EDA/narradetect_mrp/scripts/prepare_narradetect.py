from pathlib import Path
import json
import pandas as pd
from sklearn.model_selection import StratifiedKFold


ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = ROOT / "data" / "NarraDetect"
OUTPUT_DIR = ROOT / "outputs"


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LARGE_PATH = RAW_DIR / "NarraDetect_Large.csv"
SCALAR_PATH = RAW_DIR / "NarraDetect_Scalar_AllModels.csv"


def standardize_columns(df):
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(".", "_", regex=False)
    )
    return df


def find_col(df, candidates):
    for col in candidates:
        if col in df.columns:
            return col
    return None


def main():
    print("Loading NarraDetect files...")

    large = pd.read_csv(LARGE_PATH)
    scalar = pd.read_csv(SCALAR_PATH)

    large = standardize_columns(large)
    scalar = standardize_columns(scalar)

    print("\nLarge shape:", large.shape)
    print("Scalar shape:", scalar.shape)

    large_id = find_col(large, ["ID", "id", "PassageID", "passage_id"])
    scalar_id = find_col(scalar, ["ID", "id", "PassageID", "passage_id"])

    large_label = find_col(large, ["Label", "label"])
    scalar_label = find_col(scalar, ["Reader_Predicted_Label", "Label", "label"])

    large_genre = find_col(large, ["GENRE", "Genre", "genre"])
    scalar_genre = find_col(scalar, ["GENRE", "Genre", "genre"])

    print("\nDetected columns:")
    print("Large ID:", large_id)
    print("Scalar ID:", scalar_id)
    print("Large label:", large_label)
    print("Scalar label:", scalar_label)
    print("Large genre:", large_genre)
    print("Scalar genre:", scalar_genre)

    if large_id:
        print("Duplicate Large IDs:", large[large_id].duplicated().sum())

    if scalar_id:
        print("Duplicate Scalar IDs:", scalar[scalar_id].duplicated().sum())

    if large_id and scalar_id:
        overlap = set(large[large_id].dropna()) & set(scalar[scalar_id].dropna())
        print("ID overlap between Large and Scalar:", len(overlap))

    if large_genre and large_label:
        genre_label_map = (
            large.groupby(large_genre)[large_label]
            .agg(lambda x: x.mode()[0])
            .to_dict()
        )

        with open(OUTPUT_DIR / "genre_label_map.json", "w") as f:
            json.dump(genre_label_map, f, indent=4)

        print("\nSaved genre_label_map.json")

    if scalar_genre:
        scalar["strat_key"] = scalar[scalar_genre]

        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        scalar["fold"] = -1

        for fold, (_, val_idx) in enumerate(skf.split(scalar, scalar["strat_key"])):
            scalar.iloc[val_idx, scalar.columns.get_loc("fold")] = fold

        print("\nCreated 5-fold CV splits stratified by genre.")
        print(scalar["fold"].value_counts().sort_index())

    large.to_parquet(OUTPUT_DIR/ "large_clean.parquet", index=False)
    scalar.to_parquet(OUTPUT_DIR/ "scalar_clean.parquet", index=False)

    print("\nSaved:")
    print(OUTPUT_DIR/ "large_clean.parquet")
    print(OUTPUT_DIR/ "scalar_clean.parquet")


if __name__ == "__main__":
    main()