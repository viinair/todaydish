
from django.urls import path
from .views import randomDishView

urlpatterns = [path('dish/' , randomDishView, name='randomDish')]


