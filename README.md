# Early Detection of Misinformation Through Temporal, Structural, and Narrative Analysis

## Overview

This repository contains the code developed for a Major Research Project (MRP) in the MSc Data Science and Analytics program at Toronto Metropolitan University.

The research investigates whether structural and semantic changes in online discussions can provide early indicators of misinformation before formal fact-checking becomes available.

### Research Question

Can structural and semantic changes in online discussions over time provide early indicators of misinformation before formal fact-checking becomes available?

---

## Datasets

### PHEME

The PHEME dataset contains Twitter discussion threads associated with real-world news events. Threads are labelled as rumours or non-rumours and are used to analyse:

* Temporal discussion dynamics
* Conversational structure
* User behaviour
* Semantic characteristics

### NarraDetect

The NarraDetect datasets are used to model narrativity in text.

* NarraDetect Large: narrative vs non-narrative texts
* NarraDetect Scalar: narrativity-related annotations for model evaluation

Narrativity scores derived from these datasets will later be applied to PHEME discussions.

---

## Repository Structure

```text
EDA/
├── pheme_mrp/
│   ├── notebooks/
│   ├── scripts/
│   └── outputs/
│
├── narradetect_mrp/
│   ├── notebooks/
│   ├── scripts/
│   └── outputs/
```

---

## Project Workflow

1. Data preparation and cleaning
2. Exploratory Data Analysis (EDA)
3. Narrativity model development
4. Narrativity score generation
5. Feature integration
6. Analysis of discussion evolution
7. Identification of early misinformation indicators

---

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* NetworkX
* Jupyter Notebook

---

## Status

Current stage: Exploratory Data Analysis (EDA) completed for PHEME and NarraDetect datasets.
