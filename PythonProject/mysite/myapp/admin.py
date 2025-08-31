from django.contrib import admin

from myapp.models import ShavarmaStore, Food, Ingredients


# Register your models here.
@admin.register(ShavarmaStore)
class ShavarmaStoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "rating", "network", "time_created", "time_updated", "brief_info")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("id", "name")

    @admin.display(description="Кол-во блюд")
    def brief_info(self, shavarma_store: ShavarmaStore):
        return shavarma_store.food.count()

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rating", "shavarma_store", "spicy", "price", "time_created", "time_updated")
    list_display_links = ("id", "name")
    search_fields = ("name", "shavarma_store__name")
    ordering = ("id", "name")



@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "emoji")
    list_display_links = ("id", "name")
    search_fields = ("name", )