from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('tests/questions/', views.get_questions, name='get_questions'),
    path('tests/submit/', views.submit_test, name='submit_test'),
    path('tests/result/<int:test_id>/', views.get_test_result, name='get_test_result'),
    path('tests/history/', views.get_test_history, name='get_test_history'),
] 