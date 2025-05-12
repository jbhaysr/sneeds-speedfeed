"""
Views for the SpeedFeed app.
"""
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Restaurant

class RestaurantListView(ListView):
    """
    A restaurant list view.
    """
    model = Restaurant
    paginate_by = 20
