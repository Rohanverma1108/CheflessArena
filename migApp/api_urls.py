from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('dish',DishViewSet)

urlpatterns = [
    path('Dish/',include(router.urls)),
]
