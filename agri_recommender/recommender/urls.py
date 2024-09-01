from django.urls import path, include
from . import views
from .views import proxy_view

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
    path('proxy/', proxy_view, name='proxy_view'),
    path('pseudo/', views.pseudo, name='pseudo'),
]

# Adding i18n patterns
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]
