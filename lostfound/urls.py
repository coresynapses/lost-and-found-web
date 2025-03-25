from django.urls import path
from . views import reportList

from . import views

urlpatterns = [
    path ("", views.index, name = "index"),
    path('report', reportList, name ='reportList'),
]