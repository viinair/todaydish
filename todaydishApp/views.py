import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Dish


def randomDishView(request):
    dish = {"breakfast": random.choice(Dish.objects.all()).name, "lunch": random.choice(
        Dish.objects.all()).name, "dinner": random.choice(Dish.objects.all()).name}

    return JsonResponse(dish,json_dumps_params={'indent': 2})


def welcomeView(request):
    return HttpResponse('Welcome to Today\'s Dish')
