from django.urls import path

from measurement.serializers import SensorSerializer
from measurement.views import MeasurementView, SensorView, SensorIdView, InfoSensorView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorIdView.as_view()),
    path('measurement/', MeasurementView.as_view()),
    path('info/<pk>', InfoSensorView.as_view()),

]
