# Customer Lifetime Value (CLTV) Prediction

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![ML](https://img.shields.io/badge/library-LightGBM-red)](https://lightgbm.readthedocs.io/)

End-to-end machine learning pipeline to predict 6-month customer value.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Model](#model-architecture)
- [Business Impact](#business-impact)
- [License](#license)

---

## Overview
Predicts customer lifetime value using transactional data with:
- 34% lower MAE than baseline
- Automated feature engineering
- SHAP interpretability
- Time-series validation

---

## Features
- **Automated Data Handling**
  - Synthetic data generation
  - Missing value handling
- **Feature Engineering**
  - Purchase velocity
  - Country-category interactions
  - 30/90/180-day rolling spends
- **Modeling**
  - LightGBM with Tweedie loss
  - RFECV feature selection
  - Box-Cox transformation

---

# E-Commerce Transactions Dataset

![Dataset Version](https://img.shields.io/badge/Version-1.0-blue)
![Last Updated](https://img.shields.io/badge/Last_Updated-2_months_ago-lightgrey)
![License](https://img.shields.io/badge/License-CC0-blue)

A synthetic dataset of 50,000 fictional e-commerce transactions containing user demographics and purchase details.

##  Dataset Overview

This dataset simulates real-world e-commerce transaction data while maintaining complete privacy. It's ideal for:
- Data analysis practice
- Machine learning experiments
- Business intelligence visualization
- Academic research projects

##  Dataset Specifications

| Feature            | Details                              |
|--------------------|--------------------------------------|
| Total Records      | 50,000 transactions                  |
| Time Range         | 2 years of transaction history      |
| File Format        | CSV                                  |
| File Size          | ~3MB (uncompressed)                 |
| Generated Date     | 2 months ago                        |
| Update Frequency   | Static dataset (Version 1)          |

##  Columns Description

| Column Name         | Description                          | Data Type      | Range/Values                      |
|---------------------|--------------------------------------|----------------|-----------------------------------|
| Transaction_ID      | Unique transaction identifier        | Integer        | 1 to 50,000                       |
| User_Name           | Anonymous user identifier            | String         | 100 unique users                  |
| Age                 | Customer age                         | Integer        | 18-70 years                       |
| Country             | Transaction country                  | String         | 10 countries                      |
| Product_Category    | Product type purchased               | String         | 8 categories                      |
| Purchase_Amount     | Transaction value in USD             | Float          | $5.00 - $1000.00                 |
| Payment_Method      | Payment mechanism used               | String         | 6 methods                         |
| Transaction_Date    | Purchase timestamp                   | DateTime       | Random dates in past 2 years      |

---


## Installation
```bash
git clone https://github.com/yourusername/cltv-prediction.git
cd cltv-prediction
pip install -r requirements.txt
requirements.txt:

pandas>=2.0.3
numpy>=1.24.3
scikit-learn>=1.3.0
lightgbm>=4.1.0
shap>=0.44.1
scipy>=1.11.4
matplotlib>=3.7.1
seaborn>=0.12.2
joblib>=1.3.2

---
