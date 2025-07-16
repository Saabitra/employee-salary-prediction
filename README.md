Income Prediction Web Applications
This repository contains two machine learning-powered web applications built with Streamlit to predict an individual's income level based on census data. The prediction is whether the income is greater than $50K or less than or equal to $50K per year.

🌟 Features
Two Predictive Models: Implements both a Random Forest Classifier and a K-Nearest Neighbors (KNN) model for income prediction.

Interactive Web Interface: User-friendly interface created with Streamlit that allows users to input features and get real-time predictions.

Dynamic Input: Users can adjust various demographic and economic features via sliders and dropdowns to see how they affect the prediction.

Prediction Probabilities: Displays the probability for each income class, giving more insight into the model's confidence.

Data Preprocessing: Includes all necessary steps for data cleaning, encoding categorical variables, and feature scaling.

🤖 Models & Dataset
Models Used
Random Forest Classifier: An ensemble learning method that operates by constructing a multitude of decision trees at training time. It is known for its high accuracy and robustness.

K-Nearest Neighbors (KNN): A simple, supervised machine learning algorithm that can be used for classification. It classifies a data point based on the majority class of its 'k' nearest neighbors.

Dataset
The project uses the "Adult" dataset, also known as the "Census Income" dataset, from the UCI Machine Learning Repository. It contains 15 features such as age, workclass, education, marital status, and occupation to predict whether an income exceeds $50K/yr.

adult 3.csv: The dataset file used for training and testing the models.

📂 File Structure
.
├── employee_salary_app.py    # Streamlit app using Random Forest
├── knn_app.py                # Streamlit app using KNN
├── adult 3.csv               # Dataset
├── requirements.txt          # Python dependencies
└── README.md                 # Project README file

🛠️ Setup and Installation
To run these applications on your local machine, follow these steps:

Clone the repository:

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
Create a requirements.txt file with the following content:

streamlit
pandas
scikit-learn

Then, install the packages:

pip install -r requirements.txt

🚀 How to Run the Applications
You can run each application separately. Make sure you are in the project's root directory where the scripts and the adult 3.csv file are located.

To run the Employee Salary Prediction App (Random Forest):

streamlit run employee_salary_app.py

To run the KNN Income Prediction App:

streamlit run knn_app.py

After running the command, your web browser will open with the Streamlit application. Use the sidebar to input features and see the prediction results.

🖼️ Screenshots
(Here you can add screenshots of your running applications to give users a visual preview.)

Employee Salary Prediction App (Random Forest):

KNN Income Prediction App:

🤝 Contributing
Contributions are welcome! If you have any suggestions, bug reports, or want to add new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.
