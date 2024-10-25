import requests
import random
import time

# Function to simulate sensor data
def send_sensor_data():
    data = {
        "pH": round(random.uniform(6.0, 9.0), 2),
        "Temperature_C": round(random.uniform(15, 35), 2),
        "Turbidity_NTU": round(random.uniform(1.0, 20.0), 2),
        "Dissolved_Oxygen_mgL": round(random.uniform(4.0, 10.0), 2),
        "Conductivity_uScm": random.randint(100, 1000)
    }
    
    print("Sending data to server:", data)
    
    # Sending a POST request to Flask app
    response = requests.post("http://139.84.172.161:5000/predict", json=data)
    
    # Handle the response
    if response.status_code == 200:
        print("Server response:", response.json())
    else:
        print(f"Failed to get valid response. Status code: {response.status_code}")

# Run the simulation in a loop
if __name__ == "__main__":
    while True:
        send_sensor_data()
        time.sleep(10)  # Wait for 10 seconds before sending the next data
