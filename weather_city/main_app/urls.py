from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.MainView.as_view(), name='search'),
    path('weather/<str:country>/', views.WeatherView.as_view(), name='weather'),
]
