from django.urls import path
from . import views
from .views import reportList  # Ensure we import reportList

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_item, name="add_item"),  # Media
    path("report/", reportList, name="reportList"),  # Report List
]
