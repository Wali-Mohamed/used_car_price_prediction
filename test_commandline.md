curl -X POST -H "Content-Type: application/json" -d '{
    "brand": "Skoda",
    "fuel_type": "Diesel",
    "body_type": "Hatchback",
    "mileage": 50000,
    "registration_year": 2016,
    "previous_owners": 2,
    "doors": 5,
    "seats": 5
}' http://127.0.0.1:5000/predict
