"""
URL configuration for TamiuLostAndFound project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("lostfound.urls")),
    path("register/", include("lostfound.urls")),
    path("main/", include("lostfound.urls")),
    path("report-item/", include("lostfound.urls")),
    path("claim-request/", include("lostfound.urls")),
    path("fraud-report/", include("lostfound.urls")),
    path('homepage/',include("lostfound.urls")),
    path('admin/', admin.site.urls),
]

#url patterns for media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)