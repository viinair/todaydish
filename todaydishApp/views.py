import random
from django.http import HttpResponse
from django.shortcuts import render
from .models import Dish

def randomDishView(request):
    dish = random.choice(Dish.objects.all())
    return HttpResponse(dish.name)
