import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("Fichier Uploader")
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Display the uploaded file with a good column presentation  I need a scatterplot and a pieplot
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataframe Preview:")
    st.dataframe(df.head())

    st.subheader('Scatter Plot')
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_columns) >= 2:
        x_axis = st.selectbox('Select X-axis', numeric_columns, index=0)
        y_axis = st.selectbox('Select Y-axis', numeric_columns, index=1)
        scatter_plot = sns.scatterplot(data=df, x=x_axis, y=y_axis)
        st.pyplot(scatter_plot.figure)
    else:
        st.warning("Not enough numeric columns for scatter plot.")

    st.subheader('Pie Chart')
    categorical_columns = df.select_dtypes(include='object').columns.tolist()
    if categorical_columns:
        pie_column = st.selectbox('Select Column for Pie Chart', categorical_columns)
        pie_data = df[pie_column].value_counts()
        pie_plot = pie_data.plot.pie(autopct='%1.1f%%', startangle=90)
        st.pyplot(pie_plot.figure)
    else:
        st.warning("No categorical columns available for pie chart.")


 
    