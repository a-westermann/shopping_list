from django.urls import path
from . import views

app_name = 'shopping_list'

urlpatterns = [
    path('', views.home, name='home'),
    # Add more URL patterns as needed
] 