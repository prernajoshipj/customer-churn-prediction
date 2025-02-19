# customer-churn-prediction
A Streamlit-powered ML app that predicts telecom customer churn using XGBoost &amp; Random Forest. Provides churn probability &amp; feature impact analysis to help businesses improve customer retention.

# 📊 Customer Churn Prediction App 🚀

![Streamlit App](https://customer-churn-prediction-ehnsxvpezgusoupzfhappvj.streamlit.app/)

## 🎯 Overview  
This project predicts **customer churn** for a telecom company.  
It helps businesses **identify at-risk customers** and take proactive actions to **reduce churn**.  

### 🔮 **What is Customer Churn?**  
Customer churn happens when customers **stop using a company's service**.  
- **Churn = 1** → Customer is likely to leave.  
- **Churn = 0** → Customer is likely to stay.  

---

## 🎥 **Live Demo**  
🚀 **Try the App Here:** [Click to Open](https://customer-churn-prediction-ehnsxvpezgusoupzfhappvj.streamlit.app/)

---

## ⚙️ **How It Works**  
1️⃣ **User Inputs Customer Details** (Tenure, Monthly Charges, etc.)  
2️⃣ **App Predicts Churn Probability** using a **trained XGBoost model**  
3️⃣ **Displays the prediction & feature impact (SHAP analysis)**  

---

## 📊 **Model Performance**  
The model was evaluated on test data, achieving the following accuracy:
- **Random Forest Accuracy:** 79.77%
- **XGBoost Accuracy:** 80.48%

The XGBoost model was selected as the final model for deployment due to its superior performance.

---

## 🏢 **Tech Stack**  
- **Frontend:** Streamlit  
- **Machine Learning:** XGBoost, Random Forest  
- **Data Processing:** Pandas, NumPy, Scikit-learn  
- **Visualization:** Matplotlib, Seaborn, SHAP  

---

## 📂 **Project Files**  
📺 **Main App:** [`app.py`](app.py) (Streamlit UI)  
📺 **Model Notebook:** [`project.ipynb`](project.ipynb) (Model training & evaluation)  
📺 **Trained Model:** [`xgb_churn_model.pkl`](xgb_churn_model.pkl)  
📺 **Dependencies:** [`requirements.txt`](requirements.txt)  

---

## 🛠 **Run Locally**  
Want to run this project on your machine? Follow these steps:

### 🔹 **Step 1: Clone the Repository**  
```bash  
git clone https://github.com/your-username/customer-churn-prediction.git  
cd customer-churn-prediction  
```

### 🔹 **Step 2: Install Dependencies**  
```bash  
pip install -r requirements.txt  
```

### 🔹 **Step 3: Run the App**  
```bash  
streamlit run app.py  
```
**Now open `http://localhost:8501` in your browser!** 🎉  

---

## 🚀 **Future Enhancements**  
✅ Deploy on **Streamlit Cloud**  
✅ Optimize Model using **SMOTE for Imbalanced Data**  
✅ Add **AUC-ROC Score** for better evaluation  
✅ Implement **LIME for Model Explainability**  

---

## 📢 **Author**  
👩‍💻 Developed by **Prerna Joshi**  
💙 Connect with me on [LinkedIn](https://linkedin.com/in/joshi-prerna)  

---

### 🎉 **Happy Predicting! 🚀🔥**


