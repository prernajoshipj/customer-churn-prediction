import streamlit as st
import numpy as np

import joblib  



# 🎨 Set Page Config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# 📢 Informative Header
st.title("📊 Customer Churn Prediction App")
st.write(
    "🔮 This app predicts whether a customer is likely to churn or stay "
    "based on their service usage and account details. "
    "Enter the required details below and click **Predict Churn**!"
)

# ℹ️ Add an explanation of churn
st.markdown("""
### 📌 What is Customer Churn?
Customer churn refers to when a customer **stops using a company's service**. 
Understanding churn helps businesses **retain customers** and improve services.

- **Churn = 1** → Customer is likely to leave.
- **Churn = 0** → Customer is likely to stay.

### 🚀 How to Use This App?
1️⃣ **Enter Customer Details** (Tenure, Monthly Charges, etc.).  
2️⃣ **Click "Predict Churn"**.  
3️⃣ The app will show **churn probability** and a **prediction result**.  

### 🎯 Why This Matters?
- Helps businesses **reduce churn** by identifying at-risk customers.  
- Improves customer service & retention strategies.  

💡 *Try different inputs to see how churn probability changes!*  
""")

# Load trained XGBoost model
model = joblib.load("xgb_churn_model.pkl")  

# Define the Streamlit app
st.title("📊 Customer Churn Prediction App")

st.write("Enter customer details below to predict churn probability.")

# Essential User Inputs
tenure = st.slider("Tenure (Months)", min_value=0, max_value=72, value=12, step=1)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=600.0)

gender = st.radio("Gender", ["Male", "Female"])
senior_citizen = st.radio("Senior Citizen", ["Yes", "No"])
partner = st.radio("Has Partner?", ["Yes", "No"])
dependents = st.radio("Has Dependents?", ["Yes", "No"])
phone_service = st.radio("Phone Service", ["Yes", "No"])
paperless_billing = st.radio("Paperless Billing", ["Yes", "No"])
contract_type = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber Optic", "No Internet"])
payment_method = st.selectbox("Payment Method", ["Credit Card (Automatic)", "Electronic Check", "Mailed Check"])
multiple_lines = st.radio("Multiple Lines", ["Yes", "No", "No Phone Service"])
online_security = st.radio("Online Security", ["Yes", "No", "No Internet Service"])
online_backup = st.radio("Online Backup", ["Yes", "No", "No Internet Service"])
device_protection = st.radio("Device Protection", ["Yes", "No", "No Internet Service"])
tech_support = st.radio("Tech Support", ["Yes", "No", "No Internet Service"])
streaming_tv = st.radio("Streaming TV", ["Yes", "No", "No Internet Service"])
streaming_movies = st.radio("Streaming Movies", ["Yes", "No", "No Internet Service"])

# Convert categorical inputs to match model features
binary_map = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}

contract_map = {
    "Month-to-Month": [0, 0],  
    "One Year": [1, 0],  
    "Two Year": [0, 1]  
}

internet_map = {
    "DSL": [0, 0],  
    "Fiber Optic": [1, 0],  
    "No Internet": [0, 1]  
}

payment_map = {
    "Credit Card (Automatic)": [1, 0, 0],  
    "Electronic Check": [0, 1, 0],  
    "Mailed Check": [0, 0, 1]  
}

# Ensure all expected features are included
user_input = np.array([
    1,  # "Count" (constant feature)
    binary_map[gender], binary_map[senior_citizen], binary_map[partner], binary_map[dependents],
    tenure, binary_map[phone_service], binary_map[paperless_billing],
    monthly_charges, total_charges, 0,  # CLTV (not available, set to 0)
    1 if multiple_lines == "No Phone Service" else 0,  
    1 if multiple_lines == "Yes" else 0,  
    1 if internet_service == "Fiber Optic" else 0,  
    1 if internet_service == "No Internet" else 0,  
    1 if online_security == "No Internet Service" else 0,  
    1 if online_security == "Yes" else 0,  
    1 if online_backup == "No Internet Service" else 0,  
    1 if online_backup == "Yes" else 0,  
    1 if device_protection == "No Internet Service" else 0,  
    1 if device_protection == "Yes" else 0,  
    1 if tech_support == "No Internet Service" else 0,  
    1 if tech_support == "Yes" else 0,  
    1 if streaming_tv == "No Internet Service" else 0,  
    1 if streaming_tv == "Yes" else 0,  
    1 if streaming_movies == "No Internet Service" else 0,  
    1 if streaming_movies == "Yes" else 0,  
    *contract_map[contract_type], *payment_map[payment_method]  
]).reshape(1, -1)

# Ensure correct shape before prediction
#st.write(f"Feature Shape: {user_input.shape} (Expected: {model.n_features_in_})")

# Predict churn probability
if st.button("Predict Churn"):
    churn_prob = model.predict_proba(user_input)[0][1]  # Get probability of churn (class 1)
    st.write(f"📊 **Churn Probability: {churn_prob:.2%}**")

    
    if churn_prob > 0.5:
        st.error("⚠️ This customer is **likely to churn**.")
    else:
        st.success("✅ This customer is **not likely to churn**.")
