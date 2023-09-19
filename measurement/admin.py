from django.contrib import admin

from measurement.models import Sensor, SensorMeasurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

@admin.register(SensorMeasurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'measurements', 'temperatureValue', 'date']
    list_filter = ['date']