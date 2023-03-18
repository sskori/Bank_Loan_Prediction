import streamlit as st
import pandas as pd
import pickle

# Load the trained machine learning model
model = pickle.load(open('model.pkl', 'rb'))


# Create the loan prediction function
def loan_prediction(gender, married, dependents, education, self_employed, applicant_income, coapplicant_income,
                    loan_amount, loan_amount_term, credit_history, property_area):
    # Encode the categorical variables
    gender = 1 if gender == 'Male' else 0
    married = 1 if married == 'Yes' else 0
    dependents = int(dependents.strip('+'))
    education = 1 if education == 'Graduate' else 0
    self_employed = 1 if self_employed == 'Yes' else 0
    property_rural = 1 if property_area == 'Rural' else 0
    property_semiurban = 1 if property_area == 'Semiurban' else 0
    property_urban = 1 if property_area == 'Urban' else 0

    # Make the loan prediction
    prediction = model.predict([[gender, married, dependents, education, self_employed, applicant_income,
                                 coapplicant_income, loan_amount, loan_amount_term, credit_history, property_rural]])

    return prediction[0]


# Set up the user interface
st.title('Loan Prediction')

gender = st.selectbox('Gender', ('Male', 'Female'))
married = st.selectbox('Marital Status', ('Yes', 'No'))
dependents = st.selectbox('Dependents', ('0', '1', '2', '3+'))
education = st.selectbox('Education', ('Graduate', 'Not Graduate'))
self_employed = st.selectbox('Self Employed', ('Yes', 'No'))
applicant_income = st.slider('Applicant Income', 150, 81000, 2500)
coapplicant_income = st.slider('Coapplicant Income', 0, 41667, 0)
loan_amount = st.slider('Loan Amount', 9, 700, 100)
loan_amount_term = st.selectbox('Loan Amount Term', (12, 36, 60, 84, 120, 180, 240, 300, 360, 480))
credit_history = st.selectbox('Credit History', (0, 1))
property_area = st.selectbox('Property Area', ('Rural', 'Semiurban', 'Urban'))

if st.button('Predict'):
    result = loan_prediction(gender, married, dependents, education, self_employed, applicant_income,
              coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)
    if result == 1:
        st.success('Congratulations! Your loan application has been approved.')
    else:
        st.error('Sorry, your loan application has been rejected.')