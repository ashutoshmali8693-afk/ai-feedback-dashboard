import streamlit as st
import pandas as pd
import os

st.title("Admin Dashboard")

file_path = "data/reviews.csv"

if not os.path.exists(file_path):
    st.warning("No data available yet.")
else:
    df = pd.read_csv(file_path)

    st.subheader("All Feedback")
    st.dataframe(df)

    st.subheader("Analytics")
    st.write("Total Reviews:", len(df))
    st.write("Average Rating:", round(df["rating"].mean(), 2))
