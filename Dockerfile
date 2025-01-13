# Use the official Python 3.12 image as the base image
FROM python:3.11-slim




# Set the working directory in the container
WORKDIR /app


# Copy the requirements file into the container
COPY car_price_predictor/requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY car_price_predictor /app/

# Expose the port your app will run on (if applicable, adjust based on your app)
EXPOSE 9696



# Start the application using Gunicorn, ensuring the path is correct
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "app:app"]