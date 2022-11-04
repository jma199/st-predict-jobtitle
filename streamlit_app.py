import streamlit as st
import pandas as pd
import pickle5 as pickle

st.set_page_config(layout="wide")

st.write(
    """
    # Data Analytics Careers
    Predict whether a job description you've written\
    is a data analyst role or a data scientist role

    Choose to input text by typing/pasting into the text box or drag & drop a text file.
    """
)

st.markdown("")

col1, col2 = st.columns(2)
# create form element to input text
with col1:
    with st.form("Job description"):
        doc1 = st.text_input(
            "Paste or type your text below (max 1000 characters)",
            max_chars=1000
            )
        submit_button1 = st.form_submit_button(label="Show Prediction")

# create form to upload text file with text
with col2:
    with st.form("File with job description"):
        doc2 = st.file_uploader(
            "Upload text (.txt) file containing job description",
            type='txt'
            )
        submit_button2 = st.form_submit_button(label="Show Prediction")

# define helper functions
def load_model():
    return pickle.load(open('catboost2.pkl', 'rb'))

def prep_text(doc):
    text = str(doc).replace('\n', ' ')
    data = pd.Series({'jobdescription':text})
    return data

def print_prediction(data):
    '''Take in text data and return a prediction'''
    prediction = clf.predict(data)
    if int(prediction) == 0:
        st.write("This job description is predicted to be a Data Analyst role")
    else:
        st.write("This job description is predicted to be a Data Scientist role")

# load model
clf = load_model()

# pass input to model and make predictions
with st.container():
    st.subheader("Prediction output")
    
    if submit_button1:
        data1 = prep_text(doc1)
        print_prediction(data1)
    
    if submit_button2:
        data2 = prep_text(doc2)
        print_prediction(data2)
