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
}' http://127.0.0.1:5000/predict
