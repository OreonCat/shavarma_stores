from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('food/', views.food_list, name='food'),
    path('contacts/', views.contacts, name='contacts'),
    path('store/<int:pk>/', views.shavarma_store_detail, name='shavarma_store_detail'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
]