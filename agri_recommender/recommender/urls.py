from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('form/', views.home, name='form'),
    path('results/', views.results, name='results'),
    path('data-visualization/', views.data_visualization, name='data_visualization'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('latest-articles/', views.latest_articles, name='latest_articles'),
]
