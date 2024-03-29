import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data 


def load_data():
    df = pd.read_csv("stack-overflow-developer-survey-2023/survey_results_public.csv")
    # Data cleaning and preprocessing steps...
    return df

df = load_data()
df=df[df['ConvertedCompYearly'].notnull()]

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
def show_explore_page1():
    st.title("Explore Software Engineer Salaries")

    st.write("""### Stack Overflow Developer Survey 2023""")

     
    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(10, 10))  # Adjust the size as needed
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.write("""#### Number of Data from different countries""")
    st.pyplot(fig1)
    
   
    st.write("""#### Mean Salary Based On Country""")
    
    data = df.groupby(["Country"])["ConvertedCompYearly"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Mean Salary Based On Experience""")

    data = df.groupby(["YearsCodePro"])["ConvertedCompYearly"].mean().sort_values(ascending=True)
    st.line_chart(data)
