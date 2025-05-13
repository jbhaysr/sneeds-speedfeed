"""
Views for the SpeedFeed app.
"""
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Restaurant

class RestaurantDetailView(DetailView):
    """
    A restaurant list view.
    """
    model = Restaurant

class RestaurantListView(ListView):
    """
    A restaurant list view.
    """
    model = Restaurant
    paginate_by = 20
