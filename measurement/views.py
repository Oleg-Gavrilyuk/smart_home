# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorSerializer, InfoSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorIdView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class InfoSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = InfoSerializer
