import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('adult 3.csv')
    return data

data = load_data()

# Preprocessing
le = LabelEncoder()
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = le.fit_transform(data[col])

# Define features and target
features = data.drop('income', axis=1)
target = data['income']

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Streamlit App
st.title('Employee Income Prediction App')
st.write('This app predicts if an employee\'s income is <=50K or >50K.')

st.sidebar.header('Input Features')

def user_input_features():
    age = st.sidebar.slider('Age', 17, 90, 35)
    workclass = st.sidebar.selectbox('Workclass', features['workclass'].unique())
    fnlwgt = st.sidebar.slider('Final Weight', int(data['fnlwgt'].min()), int(data['fnlwgt'].max()), int(data['fnlwgt'].mean()))
    education = st.sidebar.selectbox('Education', features['education'].unique())
    educational_num = st.sidebar.slider('Educational Number', 1, 16, 10)
    marital_status = st.sidebar.selectbox('Marital Status', features['marital-status'].unique())
    occupation = st.sidebar.selectbox('Occupation', features['occupation'].unique())
    relationship = st.sidebar.selectbox('Relationship', features['relationship'].unique())
    race = st.sidebar.selectbox('Race', features['race'].unique())
    gender = st.sidebar.selectbox('Gender', features['gender'].unique())
    capital_gain = st.sidebar.slider('Capital Gain', 0, 99999, 0)
    capital_loss = st.sidebar.slider('Capital Loss', 0, 4356, 0)
    hours_per_week = st.sidebar.slider('Hours per Week', 1, 99, 40)
    native_country = st.sidebar.selectbox('Native Country', features['native-country'].unique())
    
    data_in = {
        'age': age,
        'workclass': workclass,
        'fnlwgt': fnlwgt,
        'education': education,
        'educational-num': educational_num,
        'marital-status': marital_status,
        'occupation': occupation,
        'relationship': relationship,
        'race': race,
        'gender': gender,
        'capital-gain': capital_gain,
        'capital-loss': capital_loss,
        'hours-per-week': hours_per_week,
        'native-country': native_country
    }
    features_df = pd.DataFrame(data_in, index=[0])
    return features_df

input_df = user_input_features()

st.subheader('User Input Features')
st.write(input_df)

# Prediction
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader('Prediction')
income_level = '<=50K' if prediction[0] == 0 else '>50K'
st.write(f'The predicted income level is: **{income_level}**')

st.subheader('Prediction Probability')
st.write(prediction_proba)