from django.urls import path
from .views import api_get_recommendations, api_data_visualization
from . import views

urlpatterns = [
    path('get-recommendations/', api_get_recommendations, name='api_get_recommendations'),
    path('data-visualization/', api_data_visualization, name='api_data_visualization'),
    path('register/', views.api_register, name='register'),
    path('login/', views.api_login, name='login'),
]
