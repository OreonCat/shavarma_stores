from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import ShavarmaStore, Food



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
    food = Food.objects.get(pk=pk)
    data = {
        'food': food,
    }
    return render(request, 'myapp/food_detail.html', data)

