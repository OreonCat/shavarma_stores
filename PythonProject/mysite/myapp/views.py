from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from myapp.forms import AddShavarmaStoreForm, AddFoodForm, CloudForm
from myapp.models import ShavarmaStore, Food, Ingredients
from myapp.utils import DataMixin


class IndexView(DataMixin, ListView):
    model = ShavarmaStore
    template_name = 'myapp/index.html'
    context_object_name = 'stores'
    title_page = "Шаурма"
    paginate_by = 11

class FoodListView(DataMixin, ListView):
    model = Food
    template_name = 'myapp/food_list.html'
    context_object_name = 'foods'
    title_page = "Блюда"
    paginate_by = 11

class ContactView(DataMixin, TemplateView):
    template_name = 'myapp/contacts.html'
    title_page = "Контакты"

class ShavarmaStoreDetailView(DetailView):
    model = ShavarmaStore
    template_name = 'myapp/shavarma_store_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'store'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foods"] = context['store'].food.all()
        context["title"] = context['store'].name
        return context

class FoodDetailView(DetailView):
    model = Food
    template_name = 'myapp/food_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'food'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['food'].name
        return context


class AddShopView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddShavarmaStoreForm
    template_name = 'myapp/add_shop.html'
    success_url = reverse_lazy('index')
    title_page = "Добавить магазин"
    permission_required = 'myapp.add_shavarmastore'


class UpdateShopView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    model = ShavarmaStore
    form_class = AddShavarmaStoreForm
    template_name = 'myapp/add_shop.html'
    title_page = "Редактировать"
    permission_required = 'myapp.change_shavarmastore'


class ShavarmaStoreDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DataMixin, DeleteView):
    model = ShavarmaStore
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('index')
    title_page = "Удалить"
    permission_required = 'myapp.delete_shavarmastore'


class AddFoodView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddFoodForm
    template_name = 'myapp/add_food.html'
    success_url = reverse_lazy('food')
    title_page = "Добавить блюдо"
    permission_required = 'myapp.add_food'


class UpdateFoodView(LoginRequiredMixin, DataMixin, UpdateView):
    model = Food
    form_class = AddFoodForm
    template_name = 'myapp/add_food.html'
    title_page = "Редактировать"


class DeleteFoodView(LoginRequiredMixin, DataMixin, DeleteView):
    model = Food
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('food')
    title_page = "Удалить"


class AddFoodFromShopView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddFoodForm
    template_name = 'myapp/add_food.html'
    title_page = "Добавить блюдо"
    permission_required = 'myapp.add_food'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['store'] = self.kwargs['shop_id']
        return kwargs

    def get_success_url(self):
        shop = ShavarmaStore.objects.get(pk=self.kwargs['shop_id'])
        return shop.get_absolute_url()


class AddIngredientsToFoodView(LoginRequiredMixin, DataMixin, ListView):
    model = Ingredients
    template_name = 'myapp/add_ingredient_to_food.html'
    context_object_name = 'ingredients'
    title_page = "Добавить ингредиенты"

    def get_queryset(self):
        return Ingredients.objects.exclude(food=self.kwargs['food_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food"] = self.kwargs['food_id']
        return context



@login_required
def add_ingredient_redirect(request, food_id, ingredient_id):
    food = Food.objects.get(pk=food_id)
    food.ingredients.add(ingredient_id)
    return redirect(food.get_absolute_url())

@login_required
def delete_ingredient_from_food(request, food_id, ingredient_id):
    food = Food.objects.get(pk=food_id)
    food.ingredients.remove(ingredient_id)
    return redirect(food.get_absolute_url())
