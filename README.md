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

## **Solution Approach**
To address the challenges and objectives, the following approach will be undertaken:

### **1. Data Cleaning and Preprocessing**
- Handle missing values using imputation techniques.
- Standardize numerical features (e.g., Mileage, Price) for better model performance.
- Encode categorical features (e.g., Fuel Type, Gearbox) using appropriate encoding methods like `OneHotEncoder` or `DictVectorizer`.

### **2. Exploratory Data Analysis (EDA)**
- Visualize correlations between features and price.
- Identify trends in mileage, age, and fuel type preferences.
- Segment cars based on attributes like Body Type or Emission Class.

### **3. Predictive Modeling**
- Develop a regression model to predict car prices based on the dataset's features.
- Evaluate model performance using metrics like RMSE and R².
- Optimize the model using feature engineering and hyperparameter tuning.

### **4. Insights and Recommendations**
- Provide actionable insights for buyers and sellers.
- Highlight trends, such as how fuel type affects pricing or the role of service history.

---

## **Key Outcomes**
- **Accurate Pricing Model**: A reliable regression model to predict car prices.
- **Market Trends**: Insights into how different features influence car pricing.
- **Consumer Guidance**: Practical recommendations for buyers and sellers in the UK used car market.

---

## **Technologies Used**
- **Python**: Primary programming language for data analysis and modeling.
- **Libraries**: 
  - `pandas`, `numpy`: Data manipulation and preprocessing.
  - `matplotlib`, `seaborn`: Visualization.
  - `scikit-learn`: Machine learning.

---

## **Usage Instructions**
1# How to Run Application

### Build and Run the Application Using Docker
```bash
docker build -t depression_app .
docker run -it --rm -p 5000:9696 depression_app
```



## Run locally
```bash
git clone https://github.com/Wali-Mohamed/DepressionRiskPredictor.git
cd depression_predictor
pip install pipenv
```
### Install Dependencies

```bash
pipenv install
```
### Activate virtual environment
```bash
pipenv shell
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

- import requests
- url = 'http://localhost:9696/predict'
- person ={
    "age": 6.0,
    "academic-pressure": -1,
    "work-pressure": 5,
    "cgpa": -1,
    "study-satisfaction": -1,
    "job-satisfaction": 1,
    "work-study-hours": 15.0,
    "financial-stress": 5.0,
    "gender": "male",
    "city": "pune",
    "working-professional-or-student": "working professional",
    "profession": "teacher",
    "sleep-duration": "less than 5 hours",
    "dietary-habits": "unhealthy",
    "degree": "b.tech",
    "have-you-ever-had-suicidal-thoughts-?": "no",
    "family-history-of-mental-illness": "yes"
}
	- requests.post(url, json=person).json()

```
On command line

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "age": 60.0,
    "academic-pressure": -1,
    "work-pressure": 5,
    "cgpa": -1,
    "study-satisfaction": -1,
    "job-satisfaction": 1,
    "work-study-hours": 15.0,
    "financial-stress": 5.0,
    "gender": "male",
    "city": "pune",
    "working-professional-or-student": "working professional",
    "profession": "teacher",
    "sleep-duration": "less than 5 hours",
    "dietary-habits": "unhealthy",
    "degree": "b.tech",
    "have-you-ever-had-suicidal-thoughts-?": "yes",
    "family-history-of-mental-illness": "yes"

}'  http://localhost:9696/predict
```

## **Future Work**
- Incorporate additional data sources for richer analysis.
- Explore advanced models like Gradient Boosting or Neural Networks.
- Create a web-based application for real-time price prediction.

---

## **Contributions**
Contributions to this project are welcome. Feel free to submit a pull request or open an issue with suggestions or improvements.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For queries or collaborations, reach out at: [Your Email Address].