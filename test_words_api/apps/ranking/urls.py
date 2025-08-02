from django.urls import path
from . import views

app_name = 'ranking'

urlpatterns = [
    path('ranking/', views.get_ranking, name='get_ranking'),
    path('ranking/user-rank/', views.get_user_rank, name='get_user_rank'),
] 