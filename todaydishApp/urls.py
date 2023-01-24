
from django.urls import path
from .views import randomDishView, welcomeView

urlpatterns = [path('dish/' , randomDishView),path('' , welcomeView) ]
