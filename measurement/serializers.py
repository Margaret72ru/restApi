from rest_framework import serializers
from measurement.models import SensorMeasurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorMeasurement
        fields = ['measurements', 'temperatureValue', 'date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['description']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']