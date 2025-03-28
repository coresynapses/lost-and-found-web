from django.urls import path
from . import views
from .views import reportList  # Ensure we import reportList and homepage

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_item, name="add_item"),  # Media
    path("report/", reportList, name="reportList"),  # Report List
    path("homepage/", views.homepage, name="homepage"),  # Homepage
]
