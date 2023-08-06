from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone, Brand
from django.http import JsonResponse
import json


# Create your views here.

def all(request):
    data = list(Phone.objects.values())
    return JsonResponse(data, safe=False)

