# Django Shopping List

A Django app for managing shopping lists with items, categories, and priorities.

## Installation

```bash
pip install git+https://github.com/yourusername/django-shopping-list.git
```

## Setup

1. Add 'shopping_list' to INSTALLED_APPS in your Django settings.py:
```python
INSTALLED_APPS = [
    ...
    'shopping_list',
    ...
]
```

2. Include the app's URLs in your main project's urls.py:
```python
from django.urls import path, include

urlpatterns = [
    ...
    path('shopping/', include('shopping_list.urls')),
    ...
]
```

## Usage

Access your app at: `https://yoursite.com/shopping/`

## Requirements

- Python 3.8+
- Django 4.2+ 