from rest_framework import serializers
from .models import Sensor, Measurement
class SensorSerializer(serializers.ModelSerializer):
      class Meta:
        model=Sensor
        fields='__all__'


class MeasurementSerializer_sensor(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
            class Meta:
                model = Measurement
                fields = ['temperature', 'datetime']
class SensorDetailSerializer(serializers.ModelSerializer):
            measurements = MeasurementSerializer(read_only=True, many=True)

            class Meta:
                model = Sensor
                fields = ['id', 'name', 'location', 'measurements']





