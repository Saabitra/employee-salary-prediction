import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('adult 3.csv')
    return data

data = load_data()

# Preprocessing
data.replace('?', pd.NA, inplace=True)
data.dropna(inplace=True)

# Encode categorical variables
data = pd.get_dummies(data, drop_first=True)

# Define features and target
features = data.drop('income_>50K', axis=1)
target = data['income_>50K']

# Scale the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Train the model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(features_scaled, target)

# Streamlit App
st.title('KNN Income Prediction App')
st.write('This app uses the K-Nearest Neighbors algorithm to predict income level.')

st.sidebar.header('Input Features')

def user_input_features():
    age = st.sidebar.slider('Age', 17, 90, 35)
    fnlwgt = st.sidebar.slider('Final Weight', int(data['fnlwgt'].min()), int(data['fnlwgt'].max()), int(data['fnlwgt'].mean()))
    educational_num = st.sidebar.slider('Educational Number', 1, 16, 10)
    capital_gain = st.sidebar.slider('Capital Gain', 0, 99999, 0)
    capital_loss = st.sidebar.slider('Capital Loss', 0, 4356, 0)
    hours_per_week = st.sidebar.slider('Hours per Week', 1, 99, 40)
    
    # Create a dictionary for the input, ensuring all columns are present
    data_in = {col: [0] for col in features.columns}
    data_in['age'] = [age]
    data_in['fnlwgt'] = [fnlwgt]
    data_in['educational-num'] = [educational_num]
    data_in['capital-gain'] = [capital_gain]
    data_in['capital-loss'] = [capital_loss]
    data_in['hours-per-week'] = [hours_per_week]
    
    features_df = pd.DataFrame(data_in)
    return features_df

input_df = user_input_features()

st.subheader('User Input Features')
st.write(input_df.iloc[:, :6]) # Show only the primary input features for brevity

# Scale the user input
input_scaled = scaler.transform(input_df)

# Prediction
prediction = knn.predict(input_scaled)
prediction_proba = knn.predict_proba(input_scaled)

st.subheader('Prediction')
income_level = '<=50K' if prediction[0] == 0 else '>50K'
st.write(f'The predicted income level is: **{income_level}**')

st.subheader('Prediction Probability')
st.write(prediction_proba)