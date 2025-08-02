from django.urls import path
from . import views

app_name = 'statistics'

urlpatterns = [
    path('history/statistics/', views.get_statistics, name='get_statistics'),
    path('history/statistics/detail/', views.get_history_statistics, name='get_history_statistics'),
] 