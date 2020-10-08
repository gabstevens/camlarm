import requests
from datetime import datetime
import time
import uuid
import json
import random
import pytz

keys = [
    '0f7252db-df96-412a-a0f8-b5d1193b4839',
    '2527143f-f2ca-48de-bc68-b2537fa8bca3',
    '3e6292f1-9a37-4bd4-82c1-934b452acef3',
    'edbb6656-8534-42ae-bdb5-acd2b6ad6827',
    '0294e93e-7999-41a1-a506-84cb418adffc',
    '0f4972f4-d6e0-4805-9858-54c70ca27bfe',
    'd0df5422-b5c9-4e26-9add-2460a46f606e',
    '6269e1de-cade-464f-9140-e393a4353269',
    'df4d4c13-0d11-4711-b4d2-7f1c0a64535f',
    'a9f12689-c19c-41c0-95a8-059b83e4d31f'
]

while True:
    print("Motion Detected")
    url = 'http://localhost:8000/web/detections'
    data = {'detection': json.dumps(
        {"timestamp": str(datetime.utcnow().replace(tzinfo=pytz.utc)), "key": random.choice(keys)})}
    img = open("./image_pool/image%s.jpeg" %
               (random.randint(1, 8)), 'rb')
    file = {'file': ('image.jpg', img,
                     'image/jpeg', {'Expires': '0'})}
    try:
        r = requests.post(url, files=file, data=data)
    except requests.exceptions.RequestException as e:
        print(e)
    print("Motion Stopped")
    wait = random.randint(0, 30)
    print("Waiting for {}s".format(wait))
    time.sleep(wait)
