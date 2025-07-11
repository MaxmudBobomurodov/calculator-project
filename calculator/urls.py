from django.urls import path

from calculator import views

app_name = 'calculator'

urlpatterns = [
    path('', views.calculator_view, name='calculator'),
    path('history/', views.history_view, name='history'),
]