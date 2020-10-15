from django.urls import path
from . import views

app_name = 'calendar_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_events/', views.all_events, name='all_events'),
]