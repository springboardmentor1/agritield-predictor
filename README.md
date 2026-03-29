# 🌾 AgriYield Predictor

## 📌 Project Overview

The **AgriYield Predictor** is a machine learning-based project aimed at forecasting crop yield using environmental and soil parameters such as rainfall, temperature, soil nutrients, and other agricultural factors.

The project is developed as part of an internship program and is divided into multiple milestones covering **data preprocessing, exploratory data analysis, feature engineering, and machine learning model development**.

---

## 🎯 Objective

To develop a predictive system that estimates crop yield based on agricultural and environmental conditions, helping farmers and planners make informed decisions.

---

## 📂 Dataset Description

The dataset used in this project is a **pre-integrated agricultural dataset** containing:

* 🌍 State (Geographical location)
* 🌱 Crop type
* 🌾 Soil type
* 🧪 Fertilizer type
* 🌿 Nutrients (N, P, K)
* 🌧️ Rainfall (mm)
* 🌡️ Temperature (°C)
* ⚗️ Soil pH
* 📅 Year
* 🎯 Crop Yield (kg per acre)

✅ The dataset already includes environmental, soil, and crop-related features.
👉 Therefore, no additional dataset merging was required.

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost

---

# 🟢 Milestone 1: Data Preprocessing

## 📌 Objective

To prepare and preprocess the dataset for analysis and model development.

## 🛠️ Steps Performed

* Loaded dataset using Pandas
* Checked dataset structure using `.info()` and `.describe()`
* Verified missing values using `.isnull()`
* Removed duplicate records
* Cleaned column names
* Applied feature scaling to numerical features

## ✅ Output

* Cleaned dataset (`cleaned_dataset.csv`)
* Data ready for EDA and feature engineering

---

# 🟡 Milestone 2: EDA & Feature Engineering

## 📌 Objective

To explore the dataset, identify patterns, and enhance features for better model performance.

## 📊 Exploratory Data Analysis (EDA)

* Histograms and distribution plots for feature understanding
* Scatter plots to analyze relationships (Rainfall vs Yield, Temperature vs Yield)
* Count plots and bar charts for categorical analysis
* Correlation heatmap to identify important variables
* Pairplots, boxplots, and violin plots for deeper insights

## 🔍 Key Insights

* Rainfall and temperature significantly influence crop yield
* Nutrient levels (N, P, K) strongly impact productivity
* Certain crops perform better under specific environmental conditions

## 🔢 Categorical Encoding

* Applied Label Encoding on:

  * State
  * Crop
  * Soil Type
  * Fertilizer

## ⚙️ Feature Engineering

Created new features to improve prediction:

* **NPK_sum** → Total nutrient content
* **temp_rainfall** → Interaction of temperature and rainfall
* **ph_temp** → Combined effect of soil pH and temperature

## ✅ Output

* Processed dataset (`final_dataset.csv`)
* Dataset optimized for machine learning

---

# 🔵 Milestone 3: Machine Learning Model Development

## 📌 Objective

To build, evaluate, and select the best machine learning model for crop yield prediction.

## 🤖 Models Used

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

## ⚙️ Process

* Split dataset into training and testing sets (80:20)
* Trained multiple regression models
* Evaluated models using:

  * RMSE (Root Mean Squared Error)
  * MAE (Mean Absolute Error)
  * R² Score

## 📊 Model Comparison

* XGBoost achieved the best performance
* Provided highest accuracy and lowest error

## 📈 Feature Importance

* Identified key influencing features:

  * Rainfall
  * Temperature
  * N, P, K nutrients

## 💾 Output

* Trained model saved as `model.pkl`
* Model ready for deployment

---

# 🚀 Future Scope

* Develop a web-based user interface (Streamlit/Flask)
* Enable real-time prediction using user inputs
* Integrate external weather APIs for dynamic data
* Deploy the model on cloud platforms

---

# 👩‍💻 Author

**Mansi Yelkar**
BTech – Data Science & Machine Learning

---

# ⭐ Conclusion

The AgriYield Predictor project successfully demonstrates the end-to-end pipeline of a machine learning system, from data preprocessing and analysis to model development. The selected model can effectively predict crop yield based on environmental and soil parameters, making it a valuable tool for agricultural decision-making.
