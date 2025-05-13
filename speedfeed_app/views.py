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

    def get_form(self, form_class=None):
        form = super(RestaurantCreateView, self).get_form(form_class)
        for field in form:
            field.field.widget.attrs.update({'class' : 'form-control offset-1'})
        return form

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

    def get_form(self, form_class=None):
        form = super(RestaurantUpdateView, self).get_form(form_class)
        for field in form:
            field.field.widget.attrs.update({'class' : 'form-control offset-1'})
        return form
