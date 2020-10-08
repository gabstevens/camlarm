from django.db.models.aggregates import Count
from django.db import models
from random import randint
import uuid


class LocationsManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Location(models.Model):
    objects = LocationsManager()

    name = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)


class SensorsManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Sensor(models.Model):
    objects = SensorsManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True)
    broken = models.BooleanField(default=False)
    note = models.TextField(null=True)


class Detection(models.Model):
    timestamp = models.DateTimeField()
    photo = models.ImageField()
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING, null=True)
    correctness = models.BooleanField(default=True)
