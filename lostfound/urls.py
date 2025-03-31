from django.urls import path
from . import views
#from .views import mainPage

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),  # Homepage
    path("homepage/login/", views.loginPage, name="loginPage"), #login page
    path("register/", views.registerUser, name="register"), #register user
    path("main/", views.itemList, name="itemList"), #main page
    path("main/<int:item_id>/", views.itemDetail, name = "itemDetail"), #details on one item
    path("report-item/", views.add_item, name="reportItem"), #
    path("claim-request/<int:item_id>/", views.claimRequest, name="claimRequest"),
    path("fraud-report/<int:item_id>/", views.fraudReport, name="fraudReport"),
    path("add/", views.add_item, name="add_item"),  # Media
    
]
