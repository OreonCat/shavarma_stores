from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myapp import views
from mysite import settings

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('food/', views.FoodListView.as_view(), name='food'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('store/<int:pk>/', views.shavarma_store_detail, name='shavarma_store_detail'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('add_food/', views.add_food, name='add_food'),
    path('add_food/<int:shop_id>', views.add_food_from_shop, name='add_food_from_shop'),
    path('delete_ingredient_from_food/<int:food_id>/<int:ingredient_id>/', views.delete_ingredient_from_food, name='delete_ingredient_from_food'),
    path('add_ingredient_to_food/<int:food_id>/', views.add_ingredient_to_food, name='add_ingredient_to_food'),
    path('add_ingredient_redirect/<int:food_id>/<int:ingredient_id>/', views.add_ingredient_redirect, name='add_ingredient_redirect'),
    path('cloud/', views.cloud, name='cloud'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)