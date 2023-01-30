from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request : HttpRequest):

    result = "Welcome to my Homepage"

    return HttpResponse(result)
