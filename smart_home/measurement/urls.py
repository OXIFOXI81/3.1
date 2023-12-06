from django.urls import path
from django.contrib import admin



from .views import  CreateSensorView, SensorsListView, SensorsUpdateView,CreateMeasurementView,SensorDetailListView

urlpatterns = [
     path('sensors/',SensorsListView.as_view()),
     path('sensors/create/', CreateSensorView.as_view()),
     path('sensors/update/<int:pk>/', SensorsUpdateView.as_view()),
     path('sensors/create_m/<int:pk>/', CreateMeasurementView.as_view()),
     path('sensors/list/<int:pk>/', SensorDetailListView.as_view()),

]

