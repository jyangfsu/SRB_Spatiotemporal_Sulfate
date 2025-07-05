This repository contains the data, code, and documentation supporting the study:

Su et al., 2025. **"Unraveling Spatio-Temporal Variability of Water Geochemistry and Sulfate Sources in a Multi-Tributary River System"**, submitted to *Journal of Hydrology*.

## 🧭 Overview

This study integrates dual sulfate isotopes (δ³⁴S–SO₄, δ¹⁸O–SO₄) and dual water isotopes (δ²H–H₂O, δ¹⁸O–H₂O) with water geochemistry and multivariate statistical tools to trace sulfate sources in a seasonally variable, multi-tributary river system. The Bayesian mixing model **MixSIAR** was applied to quantify the proportional contributions of multiple sulfate sources across both **spatial** (upper, middle, lower reaches) and **temporal** (dry, normal, wet seasons) scales.

## 📁 Repository Structure

```bash
📂 Sulfate_Source_Apportionment_SRB/
├── data/
│   ├── data_122019.csv                        # All river and groundwater sample data collected in Dec. 2019
│   ├── data_052020.csv                        # All river and groundwater sample data collected in May. 2020
│   └── data_082020.csv                        # All river and groundwater sample data collected in Aug. 2020
├── code/
│   ├── plot_Figure2a.py                       # Python script to plot Figure2a
│   ├── plot_Figure2b.py                       # Python script to plot Figure2b
│   ├── plot_Figure3.py                        # Python script to plot Figure3
│   ├── plot_Figure4.py                        # Python script to plot Figure4
│   │── plot_Figure6.py                        # Python script to plot Figure6
│   │── plot_Figure7.py                        # Python script to plot Figure7
│   │── plot_Figure8.py                        # Python script to plot Figure8
│   │── plot_Figure9.py                        # Python script to plot Figure9
│   │── plot_Figure10.py                       # Python script to plot Figure10
│   └── PCA_analysis.ipynb                     # Python Jupyter notebook file for PCA analysis
├── figures/
│   ├── Figure1.jpg
│   ├── Figure2.jpg
│   ├── Figure3.jpg
│   ├── Figure4.jpg
│   ├── Figure5.jpg
│   ├── Figure6.jpg
│   ├── Figure7.jpg
│   ├── Figure8.jpg
│   ├── Figure9.jpg
│   ├── Figure10.jpg
│   └── Figure11.jpg
├── results/
│   ├── MixSIAR_inputs_outputs/               # Input and output files for MixSIAR across spatial and temporal scales
│   └── Mantel_inputs_outputs/                # R script and associated data used to generate the initial version of Figure 5
├── README.md
└── LICENSE
```

## 📊 Datasets

- **data_122019.csv**: Contains raw geochemical and isotopic data for all collected river water and groundwater samples during December 2019.
- **data_052020.csv**: Contains raw geochemical and isotopic data for all collected river water and groundwater samples during May 2020.
- **data_082020.csv**: Contains raw geochemical and isotopic data for all collected river water and groundwater samples during August 2020.

## ⚙️ Analysis Tools

- **MixSIAR (R)**: Used to perform Bayesian isotope mixing using the process × residual error structure with summary source statistics.
- **Python (SciPy, scikit-learn)**: Used for statistical analysis and PCA of hydrochemical data.

## 📌 Key Features

- Novel integration of **spatiotemporal water geochemistry and isotopic data** in a multi-tributary system.
- First application of **MixSIAR** with four isotopes for sulfate source apportionment across seasonal and spatial gradients in the Shaying River Basin.
- Data and code openly shared for reproducibility and adaptation in other regional studies.

## 🌍 Broader Applications

The provided dataset and code framework can serve as a transferable template for:
- Investigating sulfate pollution in seasonally variable rivers
- Supporting source-tracking strategies in catchments with agricultural and urban influence
- Applying Bayesian mixing models in other isotope tracer studies

## 📜 Citation

If you use this repository, please cite:

> Su et al. (2025). *Unraveling Spatio-Temporal Variations of Water Geochemistry and Sulfate Sources in a Multi-Tributary River System*. Journal of Hydrology. (Under review).

## 🛠 Requirements

- R ≥ 4.0.0 with linkET packages 
- MixSIAR (https://github.com/brianstock/MixSIAR)
- Python ≥ 3.9
- Required Python packages: `pandas 2.2.3`, `numpy 1.23.1`, `matplotlib 3.5.2`, `seaborn 0.11.0`, `scipy 1.13.1`, 'statannot 0.2.3`

## 📬 Contact

For questions, please contact:  
**Jing Yang**  
College of Water Resources and Architectural Engineering, Northwest A&F University  
Email: jyang@nwafu.edu.cn; jing.yang@126.com
