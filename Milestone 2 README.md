# 🌾 AgriYield Predictor – Milestone 2

## 📌 Overview

This milestone focuses on **Exploratory Data Analysis (EDA)** and **Feature Engineering** to understand the dataset and enhance it for better machine learning performance.

The goal is to identify patterns, relationships, and important features influencing crop yield.

---

## 🎯 Objective

To analyze the agricultural dataset using visualization techniques and improve data quality through feature engineering for accurate crop yield prediction.

---
## 📊 Exploratory Data Analysis (EDA)

The following visualizations were used to understand the dataset:

### 🔹 Distribution Analysis

* Histograms and distribution plots were used to analyze the spread of numerical features like rainfall, temperature, and nutrients.

### 🔹 Relationship Analysis

* Scatter plots were used to study relationships between:

  * Rainfall vs Yield
  * Temperature vs Yield

### 🔹 Categorical Analysis

* Count plots and bar charts were used to analyze crop distribution and average yield per crop.

### 🔹 Correlation Analysis

* A heatmap was generated to identify relationships between variables.
* Key influencing features:

  * Rainfall
  * Temperature
  * N, P, K nutrients

### 🔹 Advanced Visualizations

* Pairplots to observe multi-variable relationships
* Boxplots and violin plots to detect outliers and distribution patterns

---

## 🔍 Key Insights from EDA

* Crop yield is strongly influenced by environmental factors such as rainfall and temperature.
* Soil nutrients (N, P, K) play a significant role in productivity.
* Certain crops perform better under specific soil and climatic conditions.
* Some features show strong correlation with yield, making them important for model training.

---

## 🔢 Categorical Encoding

* Converted categorical variables into numerical format using **Label Encoding**:

  * State
  * Crop
  * Soil Type
  * Fertilizer

---

## ⚙️ Feature Engineering

New features were created to improve model performance:

* **NPK_sum** → Total nutrient content
* **temp_rainfall** → Interaction between temperature and rainfall
* **ph_temp** → Combined effect of soil pH and temperature

These features help capture complex relationships in agricultural data.

---

## 📁 Files Included

* `Milestone2.ipynb` → Notebook with EDA and feature engineering
* `final_dataset.csv` → Processed dataset ready for ML models

---

## ✅ Output

* Visual understanding of dataset
* Identification of key influencing factors
* Enhanced dataset with new engineered features
* Data ready for machine learning model development

---

## 🚀 Next Steps

* Train machine learning models (Regression)
* Compare model performance (RMSE, R², MAE)
* Deploy model with a user interface

---

## 👩‍💻 Author

**Mansi Yelkar**
BTech – Data Science & Machine Learning

---

## ⭐ Conclusion

Milestone 2 successfully provides insights into the dataset and enhances it using feature engineering, making it suitable for building accurate crop yield prediction models.
