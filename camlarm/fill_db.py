import os
import random
from datetime import datetime, timedelta
from django.core.files import File
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "camlarm.settings")
application = get_wsgi_application()
from web.models import Detection, Sensor, Location


if __name__ == '__main__':
    locations = [
        ("Magazzino Amazon Empoli", 43.203492, 11.293853),
        ("Banca Intesa San Paolo San Mauro a Signa", 43.293041, 11.384953),
        ("Gelateria Novoli", 43.102389, 11.192932),
        ("Negozio TIM Campi Bisenzio", 43.192743, 11.283846),
        ("Fabbrica Gucci Villa Costanza", 43.374839, 11.394975),
    ]

    for name, lat, lon in locations:
        l = Location(name=name, lat=lat, lon=lon)
        l.save()

    sensor_names = ["Retro", "Terrazzo", "Entrata principale",
                    "Entrata secondaria", "Cassa", "Uscita d'emergenza"]

    sensor_notes = ["Le foto sono nere", "Le foto sono mosse", "Rileva troppi falsi positivi",
                    "Non viene rilevato alcun movimento", "Il sensore è nel posto sbagliato / è caduto"]

    sensor_keys = ['3e6292f1-9a37-4bd4-82c1-934b452acef3',
                   'edbb6656-8534-42ae-bdb5-acd2b6ad6827',
                   '0294e93e-7999-41a1-a506-84cb418adffc',
                   '0f4972f4-d6e0-4805-9858-54c70ca27bfe',
                   'd0df5422-b5c9-4e26-9add-2460a46f606e',
                   '6269e1de-cade-464f-9140-e393a4353269',
                   'df4d4c13-0d11-4711-b4d2-7f1c0a64535f',
                   'a9f12689-c19c-41c0-95a8-059b83e4d31f']
    for i in range(8):
        if(random.randrange(100) < 90):
            s = Sensor(id=sensor_keys[i], name=random.choice(sensor_names), broken=False,
                       note="", location=Location.objects.random())
            s.save()
        else:
            s = Sensor(name=random.choice(sensor_names),
                       broken=True, note=random.choice(sensor_notes))
            s.save()
    for i in range(12):
        if(random.randrange(100) < 90):
            s = Sensor(name=random.choice(sensor_names), broken=False,
                       note="", location=Location.objects.random())
            s.save()
        else:
            s = Sensor(name=random.choice(sensor_names),
                       broken=True, note=random.choice(sensor_notes))
            s.save()

    start_date = datetime(2020, 6, 1, 0, 0, 0, 0)
    end_date = datetime.now()
    time_between_dates = end_date - start_date
    for i in range(200):
        random_date = start_date + \
            timedelta(days=random.randrange(time_between_dates.days),
                      seconds=random.randrange(time_between_dates.seconds))
        d = Detection(timestamp=random_date, photo=File(open("./image_pool/image%s.jpeg" %
                                                             (random.randint(1, 8)), 'rb')), correctness=random.randrange(100) < 90, sensor=Sensor.objects.random())
        d.save()
