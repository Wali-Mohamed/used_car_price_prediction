# Used Car Prices in UK Dataset Analysis

## **Problem Statement**
The used car market is a dynamic and vital segment of the automotive industry, offering consumers more affordable options and significant cost savings compared to new cars. However, pricing a used car can be challenging due to numerous factors that influence its value. These factors include the car's age, mileage, fuel type, engine capacity, and more. 

Consumers and sellers often struggle to determine a fair price for a vehicle, leading to inefficiencies and mistrust in transactions. Additionally, understanding trends such as the impact of eco-friendly policies on fuel preferences or how maintenance history influences buyer confidence can provide valuable insights into market dynamics.

This project aims to analyze and model used car prices using a comprehensive dataset sourced from Autotrader UK. By leveraging data-driven insights, the project will:

1. **Help Sellers**: Accurately price their cars to attract buyers while maximizing returns.
2. **Assist Buyers**: Identify fair pricing and explore trends to make informed purchase decisions.
3. **Inform Market Analysts**: Provide trends and key drivers of value in the used car market.

---
Dataset

https://www.kaggle.com/datasets/muhammadawaistayyab/used-cars-prices-in-uk

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
## ColumnTransformer and Pipeline

### ColumnTransformer  
The `ColumnTransformer` is a tool in scikit-learn that allows you to apply different preprocessing techniques to specific columns of your dataset. This is particularly useful when you have a mix of numerical and categorical features, as it lets you handle each type appropriately. For instance, you can scale numerical columns and one-hot encode categorical columns in a single step. 

## Pipeline

The `Pipeline` in scikit-learn is a powerful tool that allows you to chain together multiple steps, such as data preprocessing and model training, into a single streamlined workflow. It ensures that these steps are executed in sequence, reducing the risk of errors and improving code readability. 

### Key Features
- **Consistency**: Ensures that the same preprocessing steps are applied to both training and testing data, preventing data leakage.
- **Automation**: Automates repetitive tasks like feature scaling and transformation.
- **Modularity**: Each step in the pipeline can be replaced or modified easily.
- **Integration**: Combines preprocessing and machine learning models into one object for simplified training and testing.

---

### How to Import  
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

```

### Interface
## On cloud

[Car Price Predictor](http://3.8.208.61:9696)

## **Usage Instructions**

### How to Run Application



## Build and Run the Application Using Docker
```bash
docker build -t car_price_predictor .
docker run -it --rm -p 9696:9696 car_price_predictor
```
## Run it on Docker

if you are in main working directory
```
python run test.py
```
and make sure localhost is 9696


## Run locally
```bash
git clone https://github.com/Wali-Mohamed/used_car_prediction.git

```
```
cd car_price_predictor

conda create --name price_prediction

```
### create conda environment
```
# activate virtual environment
conda activate price_prediction
```

```
pip install -r requirements.text
```

```bash
#train if needed by
python train.py

python app.py

# Test it
python test.py

```
make sure of the local host number by editing test.py in the port number. Change from 9696 to 5000

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

