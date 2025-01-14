# Used Car Prices in UK Dataset Analysis

## **Problem Statement**
The used car market is a dynamic and vital segment of the automotive industry, offering consumers more affordable options and significant cost savings compared to new cars. However, pricing a used car can be challenging due to numerous factors that influence its value. These factors include the car's age, mileage, fuel type, engine capacity, and more. 

Consumers and sellers often struggle to determine a fair price for a vehicle, leading to inefficiencies and mistrust in transactions. Additionally, understanding trends such as the impact of eco-friendly policies on fuel preferences or how maintenance history influences buyer confidence can provide valuable insights into market dynamics.

This project aims to analyze and model used car prices using a comprehensive dataset sourced from Autotrader UK. By leveraging data-driven insights, the project will:

1. **Help Sellers**: Accurately price their cars to attract buyers while maximizing returns.
2. **Assist Buyers**: Identify fair pricing and explore trends to make informed purchase decisions.
3. **Inform Market Analysts**: Provide trends and key drivers of value in the used car market.

---

## **Dataset Overview**
The dataset contains 3,685 unique vehicle listings with the following 13 features:

- **Price**: The price of the car (target variable for prediction).
- **Mileage (miles)**: Total miles traveled by the car.
- **Registration (year)**: The year of the car's first registration.
- **Previous Owners**: Number of previous car owners.
- **Fuel Type**: Type of fuel used (e.g., Petrol, Diesel, Electric).
- **Body Type**: Car's body type (e.g., Sedan, Hatchback, SUV).
- **Engine**: Engine capacity (in cc or liters).
- **Gearbox**: Type of transmission (e.g., Manual, Automatic).
- **Seats**: Number of seats in the car.
- **Doors**: Number of doors in the car.
- **Emission Class**: Environmental class based on emissions.
- **Service History**: Details of the car's maintenance and service record.

### **Potential Challenges**
- Missing or incomplete data (e.g., Service History or Emission Class).
- Categorical variables requiring encoding for analysis.
- Normalizing numerical data like Price and Mileage.

---

---

## **Technologies Used**
- **Python**: Primary programming language for data analysis and modeling.
- **Libraries**: 
  - `pandas`, `numpy`: Data manipulation and preprocessing.
  - `matplotlib`, `seaborn`: Visualization.
  - `scikit-learn`: Machine learning.
  - `Neural Networks`: Deep Learning

---

## **Usage Instructions**
1# How to Run Application

### Build and Run the Application Using Docker
```bash
docker build -t car_price_predictor .
docker run -it --rm -p 9696:9696 car_price_predictor
```



## Run locally
```bash
git clone https://github.com/Wali-Mohamed/used_car_prediction.git
cd car_price_predictor
pip install requirements
```

### Run the Application
```
```bash
python app.py

```

### Deactivate the environment
```bash
exit
```
* Web Service

```
Start service:  python app.py
In jupyter notebook, issue following statements:

import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    "brand": "SKODA",
    "mileage(miles)": 70189,
    "registration_year": 2016,
    "previous_owners": 3,
    "fuel_type": "Diesel",
    "body_type": "Hatchback",
    "engine": "1.4L",
    "gearbox": "Manual",
    "doors": 5,
    "seats": 5,
    "emission_class": "Euro 6",
    "service_history": "unknown"
}

response = requests.post(url, json=data)

```
On command line

```bash
curl -X POST -H "Content-Type: application/json" -d '{
     "brand": "SKODA",
    "mileage(miles)": 70189,
    "registration_year": 2016,
    "previous_owners": 3,
    "fuel_type": "Diesel",
    "body_type": "Hatchback",
    "engine": "1.4L",
    "gearbox": "Manual",
    "doors": 5,
    "seats": 5,
    "emission_class": "Euro 6",
    "service_history": "unknown"
}'  http://localhost:5000/predict
```

### Model Performance

# Model Performance

## Linear Regression
- **RMSE**: 2173
- **R2 Score**: 0.76

## Random Forest Regression
- **RMSE**: 1574
- **R2 Score**: 0.87

## Neural Network (MLPRegressor)
- **RMSE**: 1397
- **R2 Score**: 0.90

## Final Deep Learning Model (Training and Validation Combined)
- **RMSE**: 1332
- **R2 Score**: 0.88

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

