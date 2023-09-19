from django.urls import path

from measurement.views import SensorsList, UpdateSensor, SensorDetails, \
    CreateSensorMeasurement


urlpatterns = [
    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>', SensorDetails.as_view()),
    path('sensor/<pk>', UpdateSensor.as_view()),
    path('measurements/', CreateSensorMeasurement.as_view()),
]
