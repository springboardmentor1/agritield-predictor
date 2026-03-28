# agritield-predictor
📌 Project Overview

The AgriYield Predictor is a machine learning-based project aimed at forecasting crop yield using environmental and soil parameters such as rainfall, temperature, humidity, and nutrient content.

This repository contains the implementation of Milestone 1, which focuses on data collection and preprocessing to prepare the dataset for further analysis and model development.

🎯 Objective

To prepare and preprocess the agricultural dataset for crop yield prediction by:

Cleaning the dataset
Handling missing values
Removing duplicate records
Applying feature scaling
Preparing data for exploratory analysis
📂 Dataset Description

The dataset used in this project is a pre-integrated agricultural dataset containing:

🌍 State (Geographical location)
🌱 Crop type
🌾 Soil type
🧪 Fertilizer type
🌿 Nutrients (Nitrogen, Phosphorus, Potassium)
🌧️ Rainfall (mm)
🌡️ Temperature (°C)
⚗️ Soil pH
📅 Year
🎯 Crop Yield (kg per acre)

✅ The dataset already includes environmental, soil, and crop-related features.
👉 Therefore, no additional dataset merging was required.

⚙️ Technologies Used
Python 🐍
Pandas
NumPy
Scikit-learn
🛠️ Data Preprocessing Steps
1. Data Loading
Loaded dataset into Google Colab using Pandas
2. Data Understanding
Checked dataset structure using .info() and .describe()
Analyzed columns and data types
3. Handling Missing Values
Verified missing values using .isnull()
No missing values were found in the dataset
4. Removing Duplicates
Checked duplicate records
Removed duplicates to ensure data consistency
5. Data Cleaning
Standardized column names
Ensured uniform data formatting

📁 Files Included
Milestone1.ipynb → Jupyter Notebook with preprocessing steps
cleaned_dataset.csv → Final cleaned dataset
✅ Output
Cleaned and preprocessed dataset
Data ready for Exploratory Data Analysis (EDA) and Machine Learning
🚀 Future Work

In the next milestone:

Perform Exploratory Data Analysis (EDA)
Apply Feature Engineering
Identify important features
Prepare dataset for model training
👩‍💻 Author

Mansi Yelkar
BTech – Data Science & Machine Learning

⭐ Conclusion

Milestone 1 successfully prepares the dataset by ensuring data quality, consistency, and readiness for further analysis and predictive modeling.
