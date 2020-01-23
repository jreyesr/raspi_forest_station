#!/usr/bin/env python3

import requests
import time
import sqlite3
import os

STATION_ID = "14"

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS sensirion (timestamp TEXT, temp TEXT, humid TEXT)")
conn.commit()
c.execute("CREATE TABLE IF NOT EXISTS camera (timestamp TEXT, filename TEXT)")
conn.commit()

# https://www.raspberrypi-spy.co.uk/2012/09/getting-your-raspberry-pi-serial-number-using-python/
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

def try_send_sensor():
    url = "http://200.126.14.250/api/Data"
    headers = {"Content-Type": "application/json"}
    
    for row in c.execute("SELECT ROWID, timestamp, temp, humid FROM sensirion"):
        payload_humid = '{"data": [ { "StationId": ' + STATION_ID + ', "SensorId": 2, "Timestamp": "' + row[1] + '", "Type": "Humidity", "Value": ' + row[3] + ', "Units": "Percentaje", "Location": "Environment" } ] }'
        payload_temp = '{"data": [ { "StationId": ' + STATION_ID + ', "SensorId": 1, "Timestamp": "' + row[1] + '", "Type": "Temperature", "Value": ' + row[2] + ', "Units": "Celcius", "Location": "Environment" } ] }'

        response1 = requests.post(url, data=payload_humid, headers=headers)
        response2 = requests.post(url, data=payload_temp, headers=headers)
        
        if response1.status_code == 200 and response2.status_code == 200:
            c.execute("DELETE FROM sensirion WHERE ROWID = ?", (row[0],))
            conn.commit()
            
def sendimage(filename, timestamp):
    url = "http://200.126.14.250/api/imgcapture"

    data = {
        "CaptureDate": timestamp,
        "StationId": STATION_ID,
        "ApiKey": getserial()
    }
    files = {"ImageFile": ("photo.jpg", open(filename, "rb"), "image/jpeg")}
    return requests.post(url, data=data, files=files)
            
def try_send_images():
    for row in c.execute("SELECT ROWID, timestamp, filename FROM camera"):
        response = sendimage(row[2], row[1])
        
        if response.status_code == 200:
            c.execute("DELETE FROM camera WHERE ROWID = ?", (row[0],))
            conn.commit()
            
            os.remove(row[2])

while True:
    try:
        try_send_sensor() # Send all sensor data
        try_send_images() # Send all images
    except: # ignore all exceptions, keep looping
        pass
    
    time.sleep(10) # Sleep for 10 secs
