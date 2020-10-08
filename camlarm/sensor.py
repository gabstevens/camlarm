# import RPi.GPIO as GPIO
# import time
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(4, GPIO.IN)         #Read output from PIR motion sensor
# while True:
#   i=GPIO.input(4)
#   if i==0:                 #When output from motion sensor is LOW
#     print("No intruders",i)
#     time.sleep(0.1)
#   elif i==1:               #When output from motion sensor is HIGH
#     print("Intruder detected",i)
#     time.sleep(0.1)

from gpiozero import MotionSensor
import requests
from datetime import datetime
import uuid
import json
import cv2

pir1 = MotionSensor(4)
key = str(uuid.uuid4())

while True:
    cam = cv2.VideoCapture(2)   # 2 -> index of camera
    pir1.wait_for_motion()
    print("Motion Detected")
    url = 'http://0.0.0.0:8080/web/detections'
    data = {'detection': json.dumps(
        {"timestamp": str(datetime.now()), "key": key})}
    s, frame = cam.read()
    if s:    # frame captured without any errors
        imencoded = cv2.imencode(".jpg", frame)[1]
        file = {'file': ('image.jpg', imencoded.tostring(),
                         'image/jpeg', {'Expires': '0'})}
        try:
            r = requests.post(url, files=file, data=data)
        except requests.exceptions.RequestException as e:
            print(e)
    cam.release()
    pir1.wait_for_no_motion()
    print("Motion Stopped")
