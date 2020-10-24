from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_request, name="login"),
    path('', views.logout, name="logout"),
]
