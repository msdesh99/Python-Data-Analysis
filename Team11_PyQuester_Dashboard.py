import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Install streamlit from command prompt
#       python -m pip install --user streamlit
#       pip install openpyxl
#       pip install seaborn
# To run Dashboard
#   python -m streamlit run Dashboard.py

#Variables
path = "HUPA-UC Diabetes Dataset/"
demographic_path = path + "T1DM_patient_sleep_demographics_with_race.csv"
all_patients_path = path + "ALL_PATIENTS.csv"
modified_demographic_path = path+"DEMOGRAPHIC.csv"
patients_demographic_path = path +"PATIENTS_WITH_DEMOGRAPHIC.csv"

#Read csv file into dataframe
demographic_df = pd.read_csv(modified_demographic_path)

#Sort dataset by age
demographic_df.sort_values('age')

#Categorize AGE
def age_category(patient_age):
    if 18 <= patient_age < 40:
        return 'Young Adults[18-40]'
    elif 40 <= patient_age < 60:
        return 'Middle Age [41-60]'
    elif patient_age > 60:
        return 'Older Adults[>60]'
demographic_df['age_group'] = demographic_df['age'].apply(age_category)

# Count age per group
age_counts = demographic_df['age_group'].value_counts().sort_index()
# race per race group
race_counts = demographic_df['race'].value_counts()

#Streamlit UI
st.set_page_config(layout="wide")

st.title("Dashboard")
st.title("Descriptive Analysis")
st.title("AGE & Sleep Distrubances percentage Analysis")
# Layout: Side-by-side columns
col1, col2,col3 = st.columns(3)

# Distribution of Patient Age 
# seaborn histogram plot
with col1:
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.histplot(demographic_df['age'], bins=20, kde=True, ax=ax1)
    ax1.set_title('Distribution of Patient Age')
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Frequency')
    st.pyplot(fig1)
    st.write("The age groups are fairly balanced in size but not equal. The middle-aged and older groups might be slightly smaller or larger than the youngest group of patients (7–10).This balance is good for comparing sleep disturbances across age groups because no single group dominates the sample.")

# Sleep Disturbances percentage by Age Group
# seaborn box plot
with col2:
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.boxplot(x="age_group", y="sleep_disturbances_percentage", data=demographic_df, color='orange')
    ax2.set_title("Sleep Disturbances percentage by Age Group")
    st.pyplot(fig2)
    st.write("Sleep disturbances are highest in younger patients (≤40), lowest in middle-aged patients (41–60), and moderate in older patients (>60). \nStudy also shows that variability factor increases with age: middle-aged group is consistent at lower values, while older adults show the widest range of experiences.")

# Pie chart for Race distribution
# matplotlib pie chart
with col3:
     fig3, ax3 = plt.subplots(figsize=(6, 4))
     plt.pie(race_counts,labels=race_counts.index, autopct='%1.1f%%',startangle=90)
     ax3.set_title("Pie chart for Race distribution")
     st.pyplot(fig3)
     st.write("Pie chart shows that the dataset has more patients with Black,Other and Native American categories, than the White, Hispanic, and Asian populations.This is important when interpreting sleep-related statistics, as race distribution could influence trends or comparisons.")
