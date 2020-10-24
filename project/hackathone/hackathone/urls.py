"""hackathone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('calendar/', include('calendar_app.urls', namespace='calendar_app')),
    path('login/', include('login.urls', namespace='login')),
    path('mypage/', include('mypage.urls', namespace='mypage')),
    path('delivery/', include('mypage.urls', namespace='delivery')),
    path('notice/', include('mypage.urls', namespace='notice')),
    path('event/', include('mypage.urls', namespace='event')),
    path('basket/', include('mypage.urls', namespace='basket')),
    path('first/', include('main.urls', namespace='first')),

]
