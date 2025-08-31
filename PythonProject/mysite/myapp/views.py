from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.forms import AddShavarmaStoreForm, AddFoodForm
from myapp.models import ShavarmaStore, Food, Ingredients


# Create your views here.
def index(request):
    stores = ShavarmaStore.objects.all()
    data = {
        'stores': stores,
    }
    return render(request, 'myapp/index.html', data)

def food_list(request):
    foods = Food.objects.all()
    data = {
        'foods': foods,
    }
    return render(request, 'myapp/food_list.html', data)

def contacts(request):
    return render(request, 'myapp/contacts.html')

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
        form = AddShavarmaStoreForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            #try:
            #    ShavarmaStore.objects.create(**form.cleaned_data)
            #    return redirect('index')
            #except:
            #    form.add_error(None, "Ошибка добавления поста")
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