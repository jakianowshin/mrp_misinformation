# Early Detection of Emerging Misinformation through Narrative Evolution and Semantic Drift: A Temporal Graph-Based Approach

Master's Research Project (MSc Data Science and Analytics)

Toronto Metropolitan University

## Overview

This repository contains the data preparation and exploratory data analysis (EDA) stages of a Master's Research Project investigating early misinformation detection on social media.

The study explores whether changes in discussion structure, semantic content, and narrative characteristics can provide early indicators of misinformation before formal fact-checking becomes available.

### Research Question

> Can structural and semantic changes in online discussions over time provide early indicators of misinformation before formal fact-checking becomes available?

---

## Datasets

Raw datasets are not included in this repository due to size constraints.

Place the PHEME and NarraDetect datasets in the corresponding `data/` directories before running the notebooks and scripts.

### PHEME Rumour and Non-Rumour Dataset

The PHEME dataset contains Twitter conversation threads collected from five breaking-news events:

* Charlie Hebdo
* Ferguson
* Germanwings Crash
* Ottawa Shooting
* Sydney Siege

The dataset is used to analyse:

* Temporal evolution of discussions
* Reply dynamics
* Conversation structure
* User behaviour
* Rumour versus non-rumour propagation patterns

---

### NarraDetect Dataset

The NarraDetect dataset contains narrative and non-narrative texts annotated using both binary labels and human-assigned narrativity scores.

The dataset is used to:

* Model narrativity
* Analyze narrative characteristics
* Support future narrativity scoring of social media discussions

---

## Repository Structure

```text
mrp_misinformation/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── EDA/
    │
    ├── pheme_mrp/
    │   ├── data/
    │   ├── notebooks/
    │   ├── outputs/
    │   └── scripts/
    │
    ├── narradetect_mrp/
    │   ├── data/
    │   ├── notebooks/
    │   ├── outputs/
    │   └── scripts/
    │
    └── reports/
```

### PHEME

Contains data preparation and exploratory data analysis for the PHEME dataset.

### NarraDetect

Contains data preparation and exploratory data analysis for the NarraDetect dataset.

### Reports

Contains the project's EDA report.

---

## Current Progress

### Completed

* Literature Review
* Dataset Preparation
* PHEME Exploratory Data Analysis
* NarraDetect Exploratory Data Analysis

### Next Steps

* Narrativity Modelling
* Semantic Drift Analysis
* Temporal Feature Engineering
* Graph-Based Modelling
* Early Misinformation Detection Framework

---

## Technologies

- Python
- Pandas
- NumPy
- SciPy
- Scikit-learn
- NetworkX
- Matplotlib
- Seaborn
- PyArrow
- Jupyter Notebook

---

## Author

Jakia Nowshin

MSc Data Science and Analytics

Toronto Metropolitan University
