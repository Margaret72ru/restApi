from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class SensorMeasurement(models.Model):
    measurements = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperatureValue = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
