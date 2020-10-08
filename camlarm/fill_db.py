import os
import random
from datetime import datetime
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

    for i in range(20):
        if(random.randrange(100) < 90):
            s = Sensor(name=random.choice(sensor_names), broken=False,
                       note="", location=Location.objects.random())
            s.save()
        else:
            s = Sensor(name=random.choice(sensor_names),
                       broken=True, note=random.choice(sensor_notes))
            s.save()

    for i in range(200):
        d = Detection(timestamp=str(datetime.now()), photo=File(open("./image_pool/image%s.jpeg" %
                                                                     (random.randint(1, 8)), 'rb')), correctness=random.randrange(100) < 90, sensor=Sensor.objects.random())
        d.save()
