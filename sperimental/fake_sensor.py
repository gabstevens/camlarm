import requests
from datetime import datetime
import time
import uuid
import json
from io import BytesIO

key = str(uuid.uuid4())

while True:
    print("Motion Detected")
    url = 'http://0.0.0.0:8080/web/detections'
    data = {'detection': json.dumps(
        {"timestamp": str(datetime.now()), "key": key})}
    response = requests.get('https://picsum.photos/200/300')
    img = BytesIO(response.content)
    file = {'file': ('image.jpg', img,
                     'image/jpeg', {'Expires': '0'})}
    try:
        r = requests.post(url, files=file, data=data)
    except requests.exceptions.RequestException as e:
        print(e)
    print("Motion Stopped")
    time.sleep(30)
