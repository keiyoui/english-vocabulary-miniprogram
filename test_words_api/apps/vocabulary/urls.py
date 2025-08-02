from django.urls import path
from . import views

app_name = 'vocabulary'

urlpatterns = [
    path('vocabulary/', views.get_vocabulary_list, name='vocabulary_list'),
    path('vocabulary/<str:word>/', views.get_vocabulary_detail, name='vocabulary_detail'),
] 