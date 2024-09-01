import requests
import schedule
import time
from django.conf import settings

# Function to fetch data from various sources
def fetch_data():
    # Example: Fetch data from a weather API
    weather_api_url = "https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London"
    response = requests.get(weather_api_url)
    weather_data = response.json()

    # Example: Fetch data from another source
    another_api_url = "https://api.example.com/data"
    response = requests.get(another_api_url)
    another_data = response.json()

    # Process and save the data
    process_and_save_data(weather_data, another_data)

# Function to process and save the data
def process_and_save_data(weather_data, another_data):
    # Process the data as needed
    # Save the data to your database or use it to train your model
    print("Weather Data:", weather_data)
    print("Another Data:", another_data)

# Schedule the RPA task to run every day at midnight
schedule.every().day.at("00:00").do(fetch_data)

# Function to keep the script running
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()

def train_model():
    # Call your model training script or function
    # Example: subprocess.run(["python", "train_model.py"])
    print("Training the model...")

# Update the fetch_data function to call train_model
def fetch_data():
    # Fetch data from various sources
    weather_api_url = "https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London"
    response = requests.get(weather_api_url)
    weather_data = response.json()

    another_api_url = "https://api.example.com/data"
    response = requests.get(another_api_url)
    another_data = response.json()

    # Process and save the data
    process_and_save_data(weather_data, another_data)

    # Train the model
    train_model()
