from django.urls import path
from . import views

app_name = 'lostfound'

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),  # Homepage
    #path("homepage/login/", views.loginPage, name="loginPage"), #login page
    #path("register2/", views.registerUser, name="register"), #register user
    path("item-list/", views.itemList, name="itemList"), #main page
    path("item-list-/<int:item_id>/", views.itemDetail, name = "itemDetail"), #details on one item
    path("add-item/", views.add_item, name="add_item"), #
    path("claim-request/<int:item_id>/", views.claimRequest, name="claimRequest"),
    path("fraud-report/<int:item_id>/", views.fraudReport, name="fraudReport"),
    path("add/", views.add_item, name="add_item"),  # Media
    
]
