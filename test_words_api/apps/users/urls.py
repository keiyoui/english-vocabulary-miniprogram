from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('auth/login/', views.login, name='login'),
    path('auth/profile/', views.profile, name='profile'),
] 