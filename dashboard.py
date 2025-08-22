import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Patient Health Insights Dashboard")

# 1. Load dataset
df = pd.read_csv('cleaned_df_patient_race.csv')

# Encode Gender
df['Gender_encoded'] = df['Gender'].map({'Female':0, 'Male':1})

st.header("Dataset Preview")
st.dataframe(df.head(10))

# 2. Descriptive Analysis
st.header("Descriptive Statistics")
st.write(df.describe())

st.header("Correlation with Glucose")
correlation = df[['glucose','carb_input','basal_rate','steps','Sleep Quality (1-10)']].corr()
st.write(correlation['glucose'])

# 3. Visualizations
st.header("Glucose vs Carb Input")
plt.figure(figsize=(6,4))
sns.scatterplot(x='carb_input', y='glucose', data=df)
plt.xlabel('Carb Intake (g)')
plt.ylabel('Glucose (mg/dL)')
plt.title('Glucose vs Carb Input')
st.pyplot(plt.gcf())
plt.clf()

st.header("Glucose vs Basal Insulin")
plt.figure(figsize=(6,4))
sns.scatterplot(x='basal_rate', y='glucose', data=df)
plt.xlabel('Basal Rate (units/hour)')
plt.ylabel('Glucose (mg/dL)')
plt.title('Glucose vs Basal Insulin')
st.pyplot(plt.gcf())
plt.clf()

# 4. Simple Predictive Tool
st.header("Simple Glucose Predictor")
carbs = st.number_input("Enter Carb Intake (grams):", min_value=0.0, value=10.0)
basal = st.number_input("Enter Basal Rate (units/hour):", min_value=0.0, value=0.035)

predicted_glucose = 80 + 1.5*carbs - 40*basal
st.write(f"Predicted Glucose: {predicted_glucose:.1f} mg/dL")

# 5. Prescriptive Insight
st.header("Prescriptive Insight")
if predicted_glucose > 180:
    st.warning("Predicted glucose is high! Consider adjusting insulin or activity.")
elif predicted_glucose < 70:
    st.warning("Predicted glucose is low! Consider consuming carbs.")
else:
    st.success("Glucose is in a healthy range.")

