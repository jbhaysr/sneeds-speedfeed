"""
URL router for the SpeedFeed application.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('<uuid:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('<uuid:pk>/update/', views.RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('create/', views.RestaurantCreateView.as_view(), name='restaurant_create'),
]
