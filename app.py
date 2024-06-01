# Import Necessary Libraries
from flask import Flask, render_template, request
import pickle

# Creates a Flask application instance named app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data (Key:Value)
    features = {
        'ApplicantIncome': float(request.form['ApplicantIncome']),
        'CoapplicantIncome': float(request.form['CoapplicantIncome']),
        'LoanAmount': float(request.form['LoanAmount']),
        'Loan_Amount_Term': float(request.form['Loan_Amount_Term']),
        'Credit_History': float(request.form['Credit_History']),
        'Gender': float(request.form['Gender']),
        'Married': float(request.form['Married']),
        'Dependents_0': float(request.form['Dependents_0']),
        'Dependents_1': float(request.form['Dependents_1']),
        'Dependents_2': float(request.form['Dependents_2']),
        'Dependents_3+': float(request.form['Dependents_3+']),
        'Education': float(request.form['Education']),
        'Self_Employed': float(request.form['Self_Employed']),
        'Property_Area_Rural': float(request.form['Property_Area_Rural']),
        'Property_Area_Semiurban': float(request.form['Property_Area_Semiurban']),
        'Property_Area_Urban': float(request.form['Property_Area_Urban'])
    }
    
    # Convert feature values to a list
    feature_values = [features[feature] for feature in features]
    
    # Make prediction
    prediction = model.predict([feature_values])[0]
    
    # Map prediction to human-readable output
    result = 'Approved' if prediction == 1 else 'Rejected'
    
    # Render the result template with prediction result
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
