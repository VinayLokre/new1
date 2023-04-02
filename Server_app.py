import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import LabelEncoder

model = joblib.load('C:\\Users\\HP\\Pictures\\chunk\\logmodel.plk')

st.title("CUSTOMER CHUNK PREDICTION APPLICATION")

st.write('### WELCOME TO THE APPLICATION  ')
st.write('### Please select the options and add values to the required fields')


# Load the trained model

# Define the input options
options = {
    'gender_Male': ['0', '1'],
    'SeniorCitizen_1': ['0', '1'],
    'Partner_Yes': ['0', '1'],
    'Dependents_Yes': ['0', '1'],
    'PhoneService_Yes': ['0', '1'],
    'MultipleLines_Yes': ['0', '1'],
    'InternetService_No': ['0', '1'],
    'MultipleLines_No phone service': ['0', '1'],
    'InternetService_Fiber optic': ['0', '1'],
    'OnlineSecurity_Yes': ['0', '1'],
    'OnlineBackup_Yes': ['0', '1'],
    'DeviceProtection_Yes': ['0', '1'],
    'TechSupport_Yes': ['0', '1'],
    'StreamingTV_Yes': ['0', '1'],
    'StreamingMovies_Yes': ['0', '1'],
    'Contract_One year': ['0', '1'],
    'Contract_Two year': ['0', '1'],
    'PaperlessBilling_Yes': ['0', '1'],
    'PaymentMethod_Credit card (automatic)': ['0', '1'],
    'PaymentMethod_Mailed check': ['0', '1'],
    'PaymentMethod_Electronic check': ['0', '1'],
    'Tenure': [],
    'MonthlyCharges': [],
    'TotalCharges': []
}


# Define the input widgets
# Define the input widgets
input_widgets = {}
for key, values in options.items():
    if key == 'Tenure' or key == 'MonthlyCharges'  or key == 'TotalCharges':
        input_widgets[key] = st.number_input(f"Enter a value for {key}")
    else:
        input_widgets[key] = st.selectbox(f"Select an option for {key}", options[key])


# Define a function to preprocess the input data
def preprocess_input(input_data):
    le = LabelEncoder()
    for key, value in input_data.items():
        if isinstance(value, str):
            input_data[key] = le.fit_transform([value])[0]
    return input_data

# Define the prediction function
def predict(input_data):
    input_data = preprocess_input(input_data)
    input_df = pd.DataFrame(input_data, index=[0])
    pred = model.predict(input_df)
    return pred[0]

# Define the Streamlit app
st.title('Predict')

# Make a prediction and show the result
if st.button('Predict'):
    pred = predict(input_widgets)
    st.write('## Result')
    if pred == 0:
        st.error('The customer is likely to stay.')
    else:
        st.success('The customer is likely to churn.')