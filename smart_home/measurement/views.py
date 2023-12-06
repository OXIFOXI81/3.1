# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor,Measurement
from .serializers import SensorSerializer,SensorDetailSerializer,MeasurementSerializer_sensor

@api_view (['GET','POST','PUT','PATCH'])
def sensors_list(request):
      sensors=Sensor.objects.all()
      serializer=SensorSerializer(sensors,many=True)
      data=serializer.data
      print(data)
      return Response(data)

class CreateSensorView(CreateAPIView):
    queryset=Sensor.objects.all()
    serializer_class=SensorSerializer

    Measurement
class CreateMeasurementView(CreateAPIView):
    queryset=Measurement.objects.all()
        # prefetch_related('measurements')
    serializer_class=MeasurementSerializer_sensor

class SensorsListView(RetrieveAPIView):
    queryset=Sensor.objects.prefetch_related('measurements')
    serializer_class=SensorSerializer

class SensorsUpdateView(RetrieveUpdateAPIView):
    queryset=Sensor.objects.prefetch_related('measurements')
    serializer_class=SensorSerializer

class SensorDetailListView(RetrieveAPIView):
    queryset=Sensor.objects.prefetch_related('measurements')
    serializer_class=SensorDetailSerializer









