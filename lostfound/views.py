from django.shortcuts import render
from django.http import HttpResponse
from . models import Report


def index(request):
    return HttpResponse("Hello, World.")

def reportList (request):
    reports = Report.objects.all()
    return render(request, 'reportList.html', {'Reports':reports})
