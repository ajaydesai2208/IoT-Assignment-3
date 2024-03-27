# IoT-Assignment-3

# Virtual Environmental Sensor System

This repository contains the Python script and related documentation for a virtual environmental sensor system designed for the CIS600 Internet of Things Application Development course.

## Overview

The purpose of this system is to simulate an IoT environment where temperature, humidity, and CO2 levels are monitored. The script generates random sensor data within specified ranges and publishes it to a cloud-based IoT platform using MQTT protocol.

## Features

- Simulates temperature, humidity, and CO2 sensors.
- Sends data to the ThingsBoard platform using MQTT.
- Generates and publishes data every minute.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.6 or higher
- Paho-MQTT Python package

## Installation

Clone this repository to your local machine using:
https://github.com/ajdesai2208/IoT-Assignment-3.git

## Usage

To run the script, navigate to the cloned directory and execute:

python Device_Deployment_Code_Assignment_3.py


## Configuration

You will need to set up a device on the ThingsBoard platform and obtain an access token. Replace the `username` variable in the script with your device's access token.

## Output

The script will output the data being sent to the MQTT broker in the terminal. It will look something like this:

publish topic v1/devices/me/telemetry data out= {"temperature":"22°C", "humidity":"58%", "CO2":"450 ppm"}


## Visualization

You can visualize the sensor data on the ThingsBoard dashboard. Make sure to configure the dashboard widgets to display temperature, humidity, and CO2 data.

