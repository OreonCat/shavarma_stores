from django.contrib import admin

from myapp.models import ShavarmaStore, Food, Ingredients


# Register your models here.
@admin.register(ShavarmaStore)
class ShavarmaStoreAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    search_fields = ('name',)