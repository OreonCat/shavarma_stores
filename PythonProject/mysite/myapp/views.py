from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from myapp.forms import AddShavarmaStoreForm, AddFoodForm, CloudForm
from myapp.models import ShavarmaStore, Food, Ingredients



class IndexView(ListView):
    model = ShavarmaStore
    template_name = 'myapp/index.html'
    context_object_name = 'stores'

class FoodListView(ListView):
    model = Food
    template_name = 'myapp/food_list.html'
    context_object_name = 'foods'

class ContactView(TemplateView):
    template_name = 'myapp/contacts.html'

def shavarma_store_detail(request, pk):
    store = ShavarmaStore.objects.get(pk=pk)
    foods = Food.objects.filter(shavarma_store=store)
    data = {
        'store': store,
        'foods': foods,

    }
    return render(request, 'myapp/shavarma_store_detail.html', data)

def food_detail(request, pk):
    request.session['return_path'] = request.path
    food = Food.objects.get(pk=pk)
    data = {
        'food': food,
    }
    return render(request, 'myapp/food_detail.html', data)

def add_shop(request):
    if request.method == 'POST':
        form = AddShavarmaStoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddShavarmaStoreForm()
    data = {
        'form': form,
    }
    return render(request, 'myapp/add_shop.html', data)

def add_food(request):
    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food')
    else:
        form = AddFoodForm()
    data = {
        'form': form,
    }
    return render(request, 'myapp/add_food.html', data)


def add_food_from_shop(request, shop_id):
    shop = ShavarmaStore.objects.get(pk=shop_id)
    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(shop.get_absolute_url())
    else:
        form = AddFoodForm(store=shop_id)
    data = {
        'form': form,
    }
    return render(request, 'myapp/add_food.html', data)

def add_ingredient_to_food(request, food_id):
    ingredients = Ingredients.objects.exclude(food=food_id)
    data = {
        'ingredients': ingredients,
        'food': food_id,
    }
    return render(request, 'myapp/add_ingredient_to_food.html', data)

def add_ingredient_redirect(request, food_id, ingredient_id):
    food = Food.objects.get(pk=food_id)
    food.ingredients.add(ingredient_id)
    return redirect(food.get_absolute_url())

def delete_ingredient_from_food(request, food_id, ingredient_id):
    food = Food.objects.get(pk=food_id)
    food.ingredients.remove(ingredient_id)
    return redirect(food.get_absolute_url())

def handle_uploaded_file(f):
    with open(f"{settings.BASE_DIR}/uploads/{f.name}", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def cloud(request):

    if request.method == 'POST':
        form = CloudForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = CloudForm()
    data = {
        'form': form,
    }
    return render(request, 'myapp/cloud.html', data)