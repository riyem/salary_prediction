import streamlit as st
import pickle
import numpy as np  

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def predict_salary(regressor, le_country, le_education, country, education, experience):
    X = np.array([[country, education, experience]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X = X.astype(float)
    salary = regressor.predict(X)
    return salary[0]

data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page1():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some info to predict the salary""")

    countries = (
        "United States of America",                                
        "Other",                                                     
        "Germany",                                                 
        "United Kingdom of Great Britain and Northern Ireland",     
        "Canada",                                                  
        "India",                                                     
        "France",                                                    
        "Netherlands",                                              
        "Poland",                                                   
        "Brazil",                                                    
        "Australia",                                                
        "Spain",                                                   
        "Sweden",                                                  
        "Italy",                                                    
        "Switzerland",                                              
        "Austria",                                                   
        "Denmark",                                                   
        "Czech Republic",                                             
        "Norway",                                                    
        "Portugal",                                                   
        "Israel",                                                    
        "Belgium",                                                   
        "Finland",                                                    
        "Russian Federation",                                         
        "Ukraine",                                                   
        "New Zealand",                                                
        "Romania",        
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education_level = st.selectbox("Education Level", education)
    experience = st.slider("Years of Experience", 0, 50, 3)

    calculate_salary_button = st.button("Calculate Salary")
    if calculate_salary_button:
        salary = predict_salary(regressor, le_country, le_education, country, education_level, experience)
        st.subheader(f"The estimated salary is ${salary:.2f}")
