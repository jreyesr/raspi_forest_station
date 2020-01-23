#!/usr/bin/env python3

from pi_sht1x import SHT1x
import RPi.GPIO as GPIO
import requests
import time
import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

with SHT1x(18, 23, gpio_mode=GPIO.BCM) as sensor:
    temp = sensor.read_temperature()
    humidity = sensor.read_humidity(temp)
    sensor.calculate_dew_point(temp, humidity)
    print(sensor)

    timestamp = int(time.time())

    c.execute("INSERT INTO sensirion (timestamp, temp, humid) VALUES (?,?,?)", (timestamp, temp, humidity))
    conn.commit()

    #url = "http://200.126.14.250/api/Data"

    #headers = {"Content-Type": "application/json"}
    #payload_humid = '{"data": [ { "StationId": 14, "SensorId": 2, "Timestamp": "' + str(timestamp) + '", "Type": "Humidity", "Value": ' + str(humidity) + ', "Units": "Percentaje", "Location": "Environment" } ] }'
    #payload_temp = '{"data": [ { "StationId": 14, "SensorId": 1, "Timestamp": "' + str(timestamp) + '", "Type": "Temperature", "Value": ' + str(temp) + ', "Units": "Celcius", "Location": "Environment" } ] }'

    #print(requests.post(url, data=payload_humid, headers=headers))
    #print(requests.post(url, data=payload_temp, headers=headers))
