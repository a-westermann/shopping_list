from django.shortcuts import render
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    """Main view for the shopping list app"""
    context = {
        'app_name': 'Shopping List',
        'message': 'Welcome to your shopping list manager!'
    }
    return render(request, 'shopping_list/home.html', context)

# Add more views as needed 