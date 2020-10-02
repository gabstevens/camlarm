from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from .models import Detection, Sensor, Location
from django.conf import settings
import os
import json


def detections(request):
    if(request.method == "POST"):
        detectionData = json.loads(
            request.POST["detection"])
        s, created = Sensor.objects.get_or_create(
            id=detectionData.get("key"))
        if(s.broken is False):
            d = Detection(
                timestamp=detectionData["timestamp"], photo=request.FILES["file"], sensor=s)
            d.save()
            return HttpResponse(d)
        else:
            return HttpResponseBadRequest()
    elif(request.method == "GET"):
        output = json.dumps([{"id": str(d.id), "timestamp": str(d.timestamp), "photo_url": d.photo.url, "sensor_name": getattr(d.sensor, "name", None), "sensor_key": str(getattr(d.sensor, "id", None)), "sensor_location": getattr(d.sensor.location, "name", None), "sensor_broken": getattr(d.sensor, "broken", None), "correctness": d.correctness}
                             for d in Detection.objects.order_by('-timestamp')])
        return HttpResponse(output)
    return HttpResponseNotFound()


def sensors(request):
    if(request.method == "GET"):
        output = json.dumps([{"name": s.name, "key": str(s.id), "location": getattr(s.location, "name", None), "broken": s.broken, "note": s.note}
                             for s in Sensor.objects.all()])
        return HttpResponse(output)
    return HttpResponseNotFound()


def locations(request):
    if(request.method == "POST"):
        received_json_data = json.loads(request.body)
        locationData = received_json_data["location"]
        l = Location(
            name=locationData["name"], lat=locationData["lat"], lon=locationData["lon"])
        l.save()
        return HttpResponse(l)
    if(request.method == "GET"):
        output = json.dumps([{"name": l.name, "id": str(l.id), "lat": str(l.lat), "lon": str(l.lon)}
                             for l in Location.objects.all()])
        return HttpResponse(output)
    return HttpResponseNotFound()


def location(request, id):
    if(request.method in ["PATCH", "PUT"]):
        locationData = json.loads(request.body).get("location")
        location = Location.objects.get(id=id)
        if(locationData.get("name")):
            setattr(location, "name", locationData.get("name"))
        if(locationData.get("lat")):
            setattr(location, "lat", locationData.get("lat"))
        if(locationData.get("lon")):
            setattr(location, "lon", locationData.get("lon"))
        location.save()
        return HttpResponse(json.dumps({"id": str(location.id), "name": location.name, "lat": str(location.lat), "lon": str(location.lon)}))
    if(request.method == "DELETE"):
        Location.objects.filter(id=id).delete()
        return HttpResponse(json.dumps({"id": str(id)}))
    return HttpResponseNotFound()


def sensor(request, key):
    if(request.method == "GET"):
        sensor = Sensor.objects.get(id=key)
        if(sensor):
            return HttpResponse(json.dumps({"key": str(sensor.id), "name": sensor.name, "broken": sensor.broken, "note": sensor.note, "location_id": getattr(sensor.location, "id", "")}))
        else:
            return HttpResponseNotFound()
    if(request.method in ["PATCH", "PUT"]):
        sensorData = json.loads(request.body).get("sensor")
        sensor = Sensor.objects.get(id=key)
        if(sensorData.get("name")):
            setattr(sensor, "name", sensorData.get("name"))
        if(sensorData.get("broken") is not None):
            setattr(sensor, "broken", sensorData.get("broken"))
        if(sensorData.get("note")):
            setattr(sensor, "note", sensorData.get("note"))
        if(sensorData.get("location_id")):
            setattr(sensor, "location", Location.objects.get(
                id=sensorData.get("location_id")))
        sensor.save()
        return HttpResponse(json.dumps({"key": str(sensor.id), "name": sensor.name}))
    return HttpResponseNotFound()


def detection(request, id):
    if(request.method == "GET"):
        d = Detection.objects.get(id=id)
        if(d):
            return HttpResponse(json.dumps({"id": str(d.id), "timestamp": str(d.timestamp), "photo_url": d.photo.url, "sensor_name": getattr(d.sensor, "name", None), "sensor_key": str(getattr(d.sensor, "id", None)), "sensor_location": getattr(d.sensor.location, "name", None), "sensor_broken": getattr(d.sensor, "broken", None),  "correctness": d.correctness}))
        else:
            return HttpResponseNotFound()
    if(request.method in ["PATCH", "PUT"]):
        detectionData = json.loads(request.body).get("detection")
        detection = Detection.objects.get(id=id)
        if(detectionData.get("correctness") is not None):
            setattr(detection, "correctness", detectionData.get("correctness"))
        detection.save()
        return HttpResponse(json.dumps({"id": str(detection.id), "correctness": detection.correctness}))
    return HttpResponseNotFound()


def app(request):
    with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
        return HttpResponse(f.read())
