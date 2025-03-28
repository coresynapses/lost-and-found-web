from django.shortcuts import render
from django.http import HttpResponse

def android(request):
    return HttpResponse("Android.")
