from django.urls import path
from . import views

app_name='order'

urlpatterns=[
    path('<slug:c_slug>/<slug:product_slug>',views.order_detail, name='order_detail'),
    path('order/', views.order, name="order"), 

]