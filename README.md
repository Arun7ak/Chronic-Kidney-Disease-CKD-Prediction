# Chronic-Kidney-Disease-CKD-Prediction

📌 Project Overview
Chronic Kidney Disease (CKD) is a serious medical condition that requires early detection for effective treatment. This project leverages machine learning to predict CKD based on patient health indicators.

📂 Dataset
Source: Kaggle
Description: The dataset contains patient health records, including attributes like blood pressure, glucose levels, hemoglobin, and other medical indicators related to kidney function.
Machine Learning Models
I trained and evaluated the following models for CKD prediction:
✅ Decision Tree Classifier 
✅ Random Forest Classifier 

📊 Project Workflow
1️⃣ Data Collection – Extracted the dataset from Kaggle.
2️⃣ Data Preprocessing – Handled missing values, normalized features, and performed EDA.
3️⃣ Model Training – Implemented Decision Tree and Random Forest classifiers.
4️⃣ Evaluation – Assessed model performance using accuracy, precision, recall, and F1-score.

🔧 Tech Stack
Python 
Pandas, NumPy for data manipulation
Scikit-Learn for model training
Matplotlib, Seaborn for data visualization
📈 Results & Insights
Random Forest performed better than the Decision Tree model due to its ability to reduce overfitting.
Feature importance analysis helped identify key medical indicators contributing to CKD diagnosis

🌐 Streamlit Web App
The trained Random Forest model is deployed in a Streamlit app, providing real-time predictions for CKD based on user input. This app allows users to input their health data and get immediate CKD risk predictions, showcasing the real-world application of machine learning in healthcare.

