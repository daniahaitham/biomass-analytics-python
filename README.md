# Biomass & Environmental Suitability: Descriptive, Predictive and Prescriptive Analytics

A three-part data analytics project in Python on a field dataset of about 312 samples: weather (rainfall, temperature, wind), satellite spectral bands and vegetation indices (NDVI, NDWI, SAVI and others), animal presence and feed-quality measures. The aim is to understand what drives **biomass** and the **Environmental Suitability Index (ESI)**, predict biomass, and find the best formula for ESI.

Course project for Data Analytics at Al-Hussein Technical University.

> **Data:** the dataset was provided by the course and is **not included** in this repository. See [Data](#data).

## 1. Descriptive analytics: `notebooks/01_descriptive_analytics.ipynb`

- Frequencies, central tendency (mean, median), spread (standard deviation, IQR, z-score outlier detection), deciles and quartiles
- About 27 charts (histograms, relationships between biomass and rainfall, temperature, protein, fibre and vegetation indices)
- Example findings: roughly 56% of the observation days had no rain; 228 samples were taken where animals were present and 84 where they were not; biomass is strongly right-skewed (the mean is well above the median), and the top decile is far above the rest

## 2. Predictive analytics: `notebooks/02_predictive_analytics.ipynb`

Predicts biomass with four models, using variance-threshold feature selection and an 80/20 train/test split:

| Model | R² (test) | MAE |
|---|---|---|
| Exponential smoothing (time series) | -3.78 | 4,230 |
| Linear regression | 0.68 | 1,309 |
| Decision tree | 0.95 | 325 |
| LSTM neural network | -0.07 | 2,133 |

The decision tree fits best on this split. Exponential smoothing and the LSTM did poorly, which is expected: the rows are not an ordered time series, and the dataset is small for deep learning. Scores come from a single split, so they should be read as indicative, and a single unpruned tree on about 300 rows can overfit.

## 3. Prescriptive analytics: `notebooks/03_prescriptive_analytics.ipynb`

Finds the best weights for a simple model of ESI:

```
ESI ≈ w1 × Rainfall + w2 × Max temperature + w3 × NDVI
```

- A **genetic algorithm written from scratch** (roulette-wheel selection, one-point crossover, mutation, elitism) minimises the mean squared error between predicted and actual ESI
- Best weights found: about **0.32 · Rainfall + 0.12 · TEMP_MAX + 0.99 · NDVI**, which gives R² ≈ 0.74 and RMSE ≈ 0.62. Vegetation (NDVI) has by far the largest influence
- `results/` compares the same objective across five optimisers (GA, PSO, GWO, MVO, WOA, 10 runs each, 30 individuals, 50 iterations): all converge to a similar error (final MSE of 0.34–0.36). The comparison was run with the open-source [EvoloPy](https://github.com/7ossam81/EvoloPy) framework, which is not included here. See the convergence curves and box plots in that folder.

## Data

`Complete_Dataset_updated.csv` was provided by the course and is not published here. To run the notebooks, put your copy at `data/Complete_Dataset_updated.csv`. The notebooks use columns such as `Biomass`, `Rainfall`, `TEMP_MAX`, `TEMP_MIN`, `WIND_SPD`, `Animals`, `Sample_type`, `Lat`, `NDVI`, `NDWI`, `SAVI`, spectral bands `B1`–`B12`, feed-quality columns (`NDF`, `ADF`, `CP`, `TDN_*`) and `Environmental Suitability Index`.

All notebook outputs are saved, so you can read the charts and results directly on GitHub without the data.

## Run it

```bash
pip install -r requirements.txt
jupyter notebook
```

Open the notebooks in `notebooks/`. The prescriptive notebook imports `solution.py` from the same folder.

## Tools

Python, pandas, NumPy, Matplotlib, Seaborn, scikit-learn, statsmodels, TensorFlow/Keras, Jupyter.

## What I learned

- Describing a dataset properly before modelling: distributions, outliers and relationships
- Comparing very different model families on the same problem, and reading the metrics honestly
- Implementing an optimisation algorithm (a genetic algorithm) from scratch and comparing it with other optimisers

## Notes

- The bar chart at the end of the predictive notebook uses metric values typed in from an earlier run, so small differences from the table above are expected.
