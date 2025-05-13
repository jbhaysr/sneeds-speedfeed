from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('<uuid:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
]