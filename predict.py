from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the saved model pipeline (including the preprocessor and model)
with open('car_price_predictor/best_random_forest_model.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Extract user input
    data = request.json if request.is_json else request.form
    
    try:
        # Prepare input data for the model
        input_data = {
            'title': data.get('title', '').strip().lower(),  # Ensure categorical inputs are lowercase
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

        # Create a 2D array (single sample) for the model
        input_df = np.array([list(input_data.values())]).reshape(1, -1)

        # Make a prediction
        prediction = model_pipeline.predict(input_df)[0]

        # Return the prediction result
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2)
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
