"""
Views for the SpeedFeed app.
"""

from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Restaurant

class RestaurantCreateView(CreateView):
    """
    A restaurant create view.
    """
    model = Restaurant
    fields = '__all__'
    success_url = reverse_lazy('speedfeed_app:restaurant_list')

class RestaurantDeleteView(DeleteView):
    """
    A restaurant delete view.
    """
    model = Restaurant
    success_url = reverse_lazy('speedfeed_app:restaurant_list')

class RestaurantDetailView(DetailView):
    """
    A restaurant detail view.
    """
    model = Restaurant

class RestaurantListView(ListView):
    """
    A restaurant list view.
    """
    model = Restaurant
    paginate_by = 20

class RestaurantUpdateView(UpdateView):
    """
    A restaurant update view.
    """
    model = Restaurant
    fields = '__all__'
    success_url = reverse_lazy('speedfeed_app:restaurant_list')
