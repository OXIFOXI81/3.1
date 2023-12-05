# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from models import Sensor,Measurement
from serializers import SensorSerializer,MeasurementSerializer

# @api_view (['GET'])
# def

