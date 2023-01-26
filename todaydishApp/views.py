import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Dish


def randomDishView(request):
    dish = {"breakfast": random.choice(Dish.objects.all()).name, "lunch": random.choice(
        Dish.objects.all()).name, "dinner": random.choice(Dish.objects.all()).name}\
    
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,PUT,PATCH,POST,DELETE",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    }
    response = JsonResponse(dish,headers=headers, json_dumps_params={'indent': 2})
    return response

def welcomeView(request):
    return HttpResponse('Welcome to Today\'s Dish')
