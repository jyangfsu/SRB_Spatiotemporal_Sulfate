# Sulfate Source Apportionment and Spatiotemporal Analysis in the Shaying River Basin

This repository contains the data, code, and documentation supporting the study:

**"Unraveling Spatio-Temporal Variations of Water Geochemistry and Sulfate Sources in a Multi-Tributary River System"**  
Submitted to *Journal of Hydrology*.

## 🧭 Overview

This study integrates dual sulfate isotopes (δ³⁴S–SO₄, δ¹⁸O–SO₄) and dual water isotopes (δ²H–H₂O, δ¹⁸O–H₂O) with water geochemistry and multivariate statistical tools to trace sulfate sources in a seasonally variable, multi-tributary river system. The Bayesian mixing model **MixSIAR** was applied to quantify the proportional contributions of multiple sulfate sources across both **spatial** (upper, middle, lower reaches) and **temporal** (dry, normal, wet seasons) scales.

## 📁 Repository Structure

```bash
📂 Sulfate_Source_Apportionment_SRB/
├── data/
│   ├── water_chemistry_isotope_data.csv        # All river and groundwater sample data
│   ├── source_signature_summary.csv            # Summary statistics of sulfate source isotope data
│   └── metadata.txt                            # Description of columns and units
├── code/
│   ├── MixSIAR_input_file.R                    # R script to prepare input for MixSIAR
│   ├── MixSIAR_run_model.R                     # R script for running the model
│   └── PCA_analysis.py                         # Python script for PCA and statistical plots
├── figures/
│   ├── Figure2_Boxplots.png
│   ├── Figure3_PiperDiagram.png
│   └── Figure4_IsotopePlots.png
├── results/
│   ├── MixSIAR_outputs/
│   └── PCA_outputs/
├── README.md
└── LICENSE
```

## 📊 Datasets

- **water_chemistry_isotope_data.csv**: Contains raw geochemical and isotopic data for all collected river water and groundwater samples during the three field campaigns.
- **source_signature_summary.csv**: Summary of the isotope means, standard deviations, and sample sizes for each sulfate source category.
- **metadata.txt**: Provides variable descriptions, units, and sampling protocols.

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

> [Author List]. (2025). *Unraveling Spatio-Temporal Variations of Water Geochemistry and Sulfate Sources in a Multi-Tributary River System*. Journal of Hydrology. (Under review).

## 🛠 Requirements

- R ≥ 4.0.0
- MixSIAR (https://github.com/brianstock/MixSIAR)
- Python ≥ 3.8
- Required Python packages: `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `scipy`

## 📬 Contact

For questions, please contact:  
**[Your Name]**  
College of Water Resources and Architectural Engineering, Northwest A&F University  
Email: [your.email@domain.edu]
