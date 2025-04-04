from django.urls import path
from .views import home, login_page, register_page, logout_user

urlpatterns = [
    path('home/', home, name="home"),
    path('', login_page, name="login"),
    path('register/', register_page, name="register"),
    path("logout/", logout_user, name="logout"),
]
