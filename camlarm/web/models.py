from django.db import models
import uuid

# Create your models here.


class Sensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()


class Detection(models.Model):
    timestamp = models.DateTimeField()
    photo = models.ImageField()
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.timestamp)
