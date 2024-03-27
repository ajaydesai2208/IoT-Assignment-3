# IoT-Assignment-3

## Description

The system emulates an environmental station by generating random virtual sensor readings for temperature, humidity, and CO2 levels. It's built with Python and utilizes the MQTT protocol to communicate with the ThingSpeak platform for data visualization.

## Prerequisites

Ensure you have the following before starting:
- Python 3.x installed on your machine.
- An active Wi-Fi connection.
- A configured ThingSpeak channel for MQTT.

## Installation

To set up the project locally, clone the repository using the following command:

git clone https://github.com/ajaydesai2208

Navigate to the project directory:

cd IoT-Assignment-3

## Configuration

Update the following variables in the main.py script according to your setup:

- WIFI_SSID with your Wi-Fi network name.
- WIFI_PASSWORD with your Wi-Fi password. Leave this blank if you are connecting to an open network.
- MQTT credentials (mqtt_client_id, mqtt_user, mqtt_password) and topics (mqtt_topic_temperature, mqtt_topic_humidity, mqtt_topic_co2) as per your ThingSpeak channel configuration.

## Running the System
Execute the script with Python by running:

python main.py
Upon running, the system will start generating and publishing sensor data to the MQTT broker.

## Data Simulation
The script generates random data within the following ranges:

- Temperature: -50°C to 50°C
- Humidity: 0% to 100%
- CO2 Levels: 300ppm to 2000ppm

## MQTT Broker Details
- Server: mqtt3.thingspeak.com
- Port: 1883

## Output
The console will display output in the following format after each data publish:

Connected to Wi-Fi
Published: Temperature=X°C, Humidity=Y%, CO2=Zppm


