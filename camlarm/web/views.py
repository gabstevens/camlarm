from django.http import HttpResponse
import uuid

from .models import Detection, Sensor

from django.conf import settings
import os
import json

# Create your views here.


def detections(request):
    if(request.method == "POST"):
        print(request.POST)
        received_json_data = json.loads(
            request.POST["detection"])
        s, new_s = Sensor.objects.get_or_create(
            id=received_json_data.get("key", uuid.uuid4()))
        if(s):
            d = Detection(
                timestamp=received_json_data["timestamp"], photo=request.FILES["file"], sensor=s)
        else:
            d = Detection(
                timestamp=received_json_data["timestamp"], photo=request.FILES["file"], sensor=new_s)
        d.save()
        return HttpResponse(d)
    elif(request.method == "GET"):
        output = json.dumps([{"timestamp": str(q.timestamp), "photo_url": q.photo.url, "sensor_name": getattr(q.sensor, "name", "N/A"), "sensor_key": str(getattr(q.sensor, "id", "N/A"))}
                             for q in Detection.objects.order_by('-timestamp')])
        return HttpResponse(output)
    return HttpResponse({})


def sensors(request):
    if(request.method == "GET"):
        output = json.dumps([{"name": s.name, "key": str(s.id)}
                             for s in Sensor.objects.all()])
        return HttpResponse(output)
    return HttpResponse({})


def app(request):
    with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
        return HttpResponse(f.read())
