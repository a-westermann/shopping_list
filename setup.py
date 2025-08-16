import os
from setuptools import find_packages, setup

# Read the README for long description
try:
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
        README = readme.read()
except:
    README = ''

setup(
    name='django-shopping-list',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app for managing shopping lists',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/django-shopping-list',
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