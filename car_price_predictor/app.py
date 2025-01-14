from flask import Flask, render_template, request, jsonify
# Import your ML model and other necessary libraries here
import pandas as pd
import pickle
import numpy as np
import os
print(os.getcwd())
# Load the saved model pipeline (including the preprocessor and model)
with open('best_neural_network.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse incoming JSON request
        data = request.json
        
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        # Prepare input data for the model
        input_data = {
            'brand': data.get('brand', '').strip().lower(),  # Ensure categorical inputs are lowercase
            'mileage(miles)': float(data.get('mileage', 0)),
            'registration_year': int(data.get('registration_year', 0)),
            'previous_owners': int(data.get('previous_owners', 0)),
            'fuel_type': data.get('fuel_type', '').strip().lower(),
            'body_type': data.get('body_type', '').strip().lower(),
            'engine': data.get('engine', '').strip().lower(),
            'gearbox': data.get('gearbox', '').strip().lower(),
            'doors': int(data.get('doors', 0)),
            'seats': int(data.get('seats', 0)),
            'emission_class': data.get('emission_class', '').strip().lower(),
            'service_history': data.get('service_history', '').strip().lower(),
        }

        # Convert JSON data to a NumPy array (or the required format for the model)
        input_data = pd.DataFrame([input_data]) # Adjust this based on your model's input format
        
        # Make a prediction
        prediction = model_pipeline.predict(input_data)
        
        # Return the prediction
        price = f'{float(prediction[0]):.2f}'
        print(price)  # This will print the result in the console
        return jsonify({'price': price})
        #return  jsonify({'price': f'£{float(prediction[0]):.2f}'})  # Ensure the response is JSON serializable
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True) 