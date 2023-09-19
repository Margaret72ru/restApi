from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView

from measurement.models import Sensor, SensorMeasurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, SensorChangeSerializer, \
    MeasurementSerializer


class SensorsList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetails(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


class CreateSensorMeasurement(ListCreateAPIView):
    queryset = SensorMeasurement.objects.all()
    serializer_class = MeasurementSerializer
