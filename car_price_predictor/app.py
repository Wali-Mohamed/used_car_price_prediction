from flask import Flask, render_template, request, jsonify
# Import your ML model and other necessary libraries here

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
    data = request.json
    
    # Here you'll need to:
    # 1. Process the input data
    # 2. Make predictions using your trained model
     # Make a prediction
    prediction = model_pipeline.predict(data)
    # 3. Return the predicted price
    
    # Placeholder response (replace with actual prediction)
    predicted_price = 0  # Your model prediction goes here
    
    return jsonify({'price': prediction})

if __name__ == '__main__':
    app.run(debug=True) 