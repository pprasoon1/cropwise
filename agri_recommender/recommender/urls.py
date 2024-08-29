from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('form/', views.AgriForm, name='form'),
    path('results/', views.results, name='results'),
    path('data-visualization/', views.data_visualization, name='data_visualization'),
]
