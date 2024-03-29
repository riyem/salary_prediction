import streamlit as st
from predict_page1 import show_predict_page1
from explore_page1 import show_explore_page1


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page1()
else:
    show_explore_page1()