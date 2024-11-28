from django.urls import path
from .views import create_short_url,redirect_to_long_url

urlpatterns = [
    path('api/create/', create_short_url, name='create_short_url'),
    path('<str:short_url>/', redirect_to_long_url, name='redirect_to_long_url'),
]