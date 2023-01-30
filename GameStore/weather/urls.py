from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("riyadh/", views.weather_riyadh, name="Weather_for_riyadh")
]