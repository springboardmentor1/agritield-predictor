# AgriYield Predictor - Milestone 1

 Objective
Prepare dataset for crop yield prediction using preprocessing techniques.

# Work Done
- Loaded dataset in Google Colab
- Checked dataset structure
- Handled missing values
- Removed duplicates
- Applied feature scaling

# File
- Milestone1.ipynb

# Output
Cleaned dataset ready for further analysis




# AgriYield Predictor - Milestone 2

# Objective
Perform Exploratory Data Analysis (EDA) and Feature Engineering to understand the dataset and improve model performance.

---

# Work Completed

# Exploratory Data Analysis (EDA)
- Visualized data distributions using histograms
- Analyzed relationships between features and crop yield using scatter plots
- Identified patterns and trends in environmental and soil data

# Correlation Analysis
- Generated correlation heatmap
- Identified important features influencing crop yield
- Selected relevant variables for model training

# Categorical Encoding
- Converted categorical variables (e.g., soil type, crop type) into numerical format using encoding techniques

# Feature Engineering
- Created new features such as:
  - Temperature-Rainfall interaction
  - Humidity Index
- Improved dataset quality for better prediction accuracy


# Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn


# Files
- Milestone2.ipynb
- final_dataset.csv


# Output
Processed dataset with selected and engineered features, ready for machine learning model development.

# Milestone 3: Model Development & Evaluation

# Overview

In this phase, multiple regression models were developed and evaluated to identify the best-performing model for predicting the target variable.


# Models Implemented

The following regression models were trained and tested:

* **Linear Regression** – a baseline model to capture linear relationships
* **Random Forest Regressor** – an ensemble model using multiple decision trees
* **XGBoost Regressor** – a boosting algorithm for improved accuracy


# Data Preparation

* Dataset was preprocessed by handling missing values
* Categorical variables were converted using one-hot encoding
* Data was split into:

  * **Training set (80%)**
  * **Testing set (20%)**


# Evaluation Metrics

Models were evaluated using the following metrics:

* **RMSE (Root Mean Squared Error):** Measures overall prediction error
* **MAE (Mean Absolute Error):** Measures average absolute error
* **R² Score:** Indicates how well the model explains the variance

---

# Model Comparison

All models were compared based on their performance metrics. The results were organized in a tabular format to identify the most accurate model.


# Best Model Selection

The best-performing model was selected based on:

* Highest **R² Score**
* Lowest **RMSE** and **MAE**

This model is considered optimal for deployment in the next phase.


# Model Interpretation

To understand model behavior and feature impact:

* **Feature Importance** was used for tree-based models
* **SHAP (SHapley Additive Explanations)** was applied to interpret predictions and understand the contribution of each feature


# Outcome

* Successfully trained and evaluated multiple regression models
* Identified the best-performing model
* Gained insights into feature influence on predictions
* Prepared the model for future deployment



