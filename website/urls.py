"""
website/urls.py
URL patterns for the portfolio website application.
"""
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
]
