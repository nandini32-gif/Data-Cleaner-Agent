import streamlit as st
import pandas as pd

st.title("Data Cleaning")
st.write("Upload a CSV file and clean it with one click.")

file = st.file_uploader("Upload dataset", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Original data")
    st.dataframe(df)

    if st.button("Start Cleaning"):
        rows_before = len(df)
        nulls_found = int(df.isnull().sum().sum())

        cleaned = df.dropna()
        after_nulls = len(cleaned)

        cleaned = cleaned.drop_duplicates()
        duplicates_removed = after_nulls - len(cleaned)

        st.subheader("Cleaning report")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Rows before", rows_before)
        col2.metric("Nulls found", nulls_found)
        col3.metric("Duplicates removed", duplicates_removed)
        col4.metric("Rows after", len(cleaned))

        st.subheader("Cleaned data")
        st.dataframe(cleaned)

        st.download_button(
            "Export Clean Data",
            cleaned.to_csv(index=False),
            "clean_data.csv",
            "text/csv",
        )