from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myapp import views
from mysite import settings

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('food/', views.FoodListView.as_view(), name='food'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('store/<int:pk>/', views.ShavarmaStoreDetailView.as_view(), name='shavarma_store_detail'),
    path('food/<int:pk>/', views.FoodDetailView.as_view(), name='food_detail'),
    path('add_shop/', views.AddShopView.as_view(), name='add_shop'),
    path('update_shop/<int:pk>', views.UpdateShopView.as_view(), name='update_shop'),
    path('store/<int:pk>/delete', views.ShavarmaStoreDeleteView.as_view(), name='store_delete'),
    path('add_food/', views.AddFoodView.as_view(), name='add_food'),
    path('add_food/<int:shop_id>', views.AddFoodFromShopView.as_view(), name='add_food_from_shop'),
    path('update_food/<int:pk>', views.UpdateFoodView.as_view(), name='update_food'),
    path('food/<int:pk>/delete', views.DeleteFoodView.as_view(), name='delete_food'),
    path('delete_ingredient_from_food/<int:food_id>/<int:ingredient_id>/', views.delete_ingredient_from_food, name='delete_ingredient_from_food'),
    path('add_ingredient_to_food/<int:food_id>/', views.AddIngredientsToFoodView.as_view(), name='add_ingredient_to_food'),
    path('add_ingredient_redirect/<int:food_id>/<int:ingredient_id>/', views.add_ingredient_redirect, name='add_ingredient_redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)