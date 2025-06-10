"""
Views for the SpeedFeed app.
"""

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from rest_framework import filters, permissions, viewsets
from .models import Restaurant
from .permissions import IsStaffOrReadOnly
from .serializers import RestaurantSerializer

class RestaurantCreateView(LoginRequiredMixin, CreateView):
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

class RestaurantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A restaurant delete view.
    """
    model = Restaurant
    success_url = reverse_lazy('speedfeed_app:restaurant_list')

    def test_func(self):
        return self.request.user.is_staff

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    """
    A restaurant detail view.
    """
    model = Restaurant

class RestaurantListView(LoginRequiredMixin, ListView):
    """
    A restaurant list view.
    """
    model = Restaurant
    paginate_by = 20

class RestaurantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        return self.request.user.is_staff

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('-id')
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStaffOrReadOnly]
    filterset_fields = ['name', 'address__location', 'currency', 'rating']
    search_fields = ['name', 'address__location', 'currency']
    ordering_fields = ['rating', 'name']