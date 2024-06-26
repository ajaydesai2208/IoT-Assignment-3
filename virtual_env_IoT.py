import network
import time
import urandom
from umqtt.simple import MQTTClient

# ThingSpeak MQTT broker details
mqtt_client_id = "GRgFEQciJRobLgE6ICQCFDg"
mqtt_user = "GRgFEQciJRobLgE6ICQCFDg"
mqtt_password = "wVWg8llDDLbD8lbPn2KyQQQA"
mqtt_server = "mqtt3.thingspeak.com"
mqtt_port = 1883
mqtt_topic_temperature = "channels/2488579/publish/fields/field1"
mqtt_topic_humidity = "channels/2488579/publish/fields/field2"
mqtt_topic_co2 = "channels/2488579/publish/fields/field3"


WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""


def generate_sensor_data():
    temperature = urandom.uniform(-50, 50)
    humidity = urandom.uniform(0, 100)
    co2 = urandom.uniform(300, 2000)
    return temperature, humidity, co2

# Publishing data
def publish_to_thingspeak(temperature, humidity, co2):
    client = MQTTClient(mqtt_client_id, mqtt_server, user=mqtt_user, password=mqtt_password)
    client.connect()
    client.publish(mqtt_topic_temperature, str(temperature))
    client.publish(mqtt_topic_humidity, str(humidity))
    client.publish(mqtt_topic_co2, str(co2))
    client.disconnect()

# Establishing Wi-Fi connection
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(WIFI_SSID, WIFI_PASSWORD)

# Connection loading
while not sta_if.isconnected():
    pass

print("Connected to Wi-Fi")

# Publishing sensor data to ThingSpeak
while True:
    temperature, humidity, co2 = generate_sensor_data()
    publish_to_thingspeak(temperature, humidity, co2)
    print("Published: Temperature={:.2f}C, Humidity={:.2f}%, CO2={:.2f}ppm".format(temperature, humidity, co2))
    time.sleep(10)  
