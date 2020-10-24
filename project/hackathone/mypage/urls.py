from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns=[
    path('', views.home, name='mypage'),
    path('delivery/',views.delivery, name='delivery'),
    path('notice/',views.notice, name='notice'),
    path('basket/',views.basket, name='basket'),
    path('event/',views.event, name='event'),
]