from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def weather_riyadh(request : HttpRequest):

    content = "Weather in Riyadh is sunny"
    return HttpResponse(content)