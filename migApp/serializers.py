from rest_framework import serializers
from .models import Dish

class DishSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'description', 'price' , 'url')
