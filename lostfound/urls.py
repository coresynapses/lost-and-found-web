from django.urls import path
from . import views
from .views import home, login_page, register_page, logout_user

app_name = 'lostfound'

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path("logout/", logout_user, name="logout"),

    path("item-list/", views.itemList, name="itemList"), #main page
    path("item-list/<int:item_id>/", views.itemDetail, name="itemDetail"), #details on one item

    path("claim-request/<int:item_id>/", views.claimRequest, name="claimRequest"),
    path("fraud-report/<int:item_id>/", views.fraudReport, name="fraudReport"),
    path("add/", views.add_item, name="add_item"),  # Media

]
