# Django App Template

Use this template to create new Django apps that can be installed into existing Django sites.

## Required Directory Structure

```
your_app_name/
├── your_app_name/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   └── your_app_name/
│   │       └── home.html
│   └── static/
│       └── your_app_name/
│           ├── css/
│           │   └── style.css
│           └── js/
│               └── script.js
├── setup.py
├── MANIFEST.in
├── README.md
└── requirements.txt
```

## File Contents

### 1. `your_app_name/__init__.py`
```python
# Empty file - makes the directory a Python package
```

### 2. `your_app_name/apps.py`
```python
from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app_name'
```

### 3. `your_app_name/urls.py`
```python
from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    path('', views.home, name='home'),
    # Add more URL patterns as needed
]
```

### 4. `your_app_name/views.py`
```python
from django.shortcuts import render
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    """Main view for the app"""
    context = {
        'app_name': 'Your App Name',
        'message': 'Welcome to your new Django app!'
    }
    return render(request, 'your_app_name/home.html', context)

# Add more views as needed
```

### 5. `your_app_name/models.py`
```python
from django.db import models

# Define your models here
# Example:
# class YourModel(models.Model):
#     name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     
#     def __str__(self):
#         return self.name
```

### 6. `your_app_name/templates/your_app_name/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ app_name }}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'your_app_name/css/style.css' %}">
</head>
<body>
    <div class="container">
        <h1>{{ app_name }}</h1>
        <p>{{ message }}</p>
    </div>
    
    <script src="{% static 'your_app_name/js/script.js' %}"></script>
</body>
</html>
```

### 7. `your_app_name/static/your_app_name/css/style.css`
```css
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
    text-align: center;
}

p {
    color: #666;
    text-align: center;
    font-size: 18px;
}
```

### 8. `your_app_name/static/your_app_name/js/script.js`
```javascript
// Your JavaScript code here
console.log('Your app is loaded!');
```

### 9. `setup.py`
```python
import os
from setuptools import find_packages, setup

# Read the README for long description
try:
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
        README = readme.read()
except:
    README = ''

setup(
    name='your-app-name',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Description of your Django app',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo-name',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=4.2.0',
    ],
)
```

### 10. `MANIFEST.in`
```
include README.md
include requirements.txt
recursive-include your_app_name/static *
recursive-include your_app_name/templates *
```

### 11. `README.md`
```markdown
# Your App Name

Description of what your Django app does.

## Installation

```bash
pip install git+https://github.com/yourusername/your-repo-name.git
```

## Setup

1. Add 'your_app_name' to INSTALLED_APPS in your Django settings.py:
```python
INSTALLED_APPS = [
    ...
    'your_app_name',
    ...
]
```

2. Include the app's URLs in your main project's urls.py:
```python
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('your_app_name.urls')),
    ...
]
```

## Usage

Access your app at: `https://yoursite.com/`

## Requirements

- Python 3.8+
- Django 4.2+
```

### 12. `requirements.txt`
```
Django>=4.2.0
```

## Installation Steps

1. **Create the directory structure** as shown above
2. **Replace all instances** of `your_app_name` with your actual app name
3. **Update the setup.py** with your actual information (name, description, URL, author)
4. **Customize the views, models, and templates** as needed
5. **Install in your Django project:**
   ```bash
   pip install git+https://github.com/yourusername/your-repo-name.git
   ```
6. **Add to INSTALLED_APPS** in your Django settings.py
7. **Include URLs** in your main project's urls.py

## Notes

- The `app_name` in urls.py creates a namespace for your app's URLs
- Templates should be in `templates/your_app_name/` to avoid conflicts
- Static files should be in `static/your_app_name/` for the same reason
- The `MANIFEST.in` ensures all necessary files are included when packaging
- Update the Django version requirements in setup.py as needed 