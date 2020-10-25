from django.urls import path
from . import views

app_name = 'main'

urlpatterns=[
    path('', views.first, name='first'),
    path('home/', views.home, name='home'),
]