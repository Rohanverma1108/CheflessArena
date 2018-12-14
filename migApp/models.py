from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    age = models.IntegerField()
    email=models.CharField(max_length=50,default='')
    phone = models.IntegerField(default=None)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField(null=True)
    number = models.IntegerField(null=True)
    city = models.TextField(default="")
    zipcode = models.TextField(null=True)
    stateOrProvince = models.TextField(null=True)
    country = models.TextField(null=True)
    telephone = models.TextField(null=True)
    url = models.URLField(null = True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="myrestaurants")
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

class Review(models.Model):
    RATING_CHOICES= ((1,'one') , (2,'two') , (3,'three') , (4,'four') , (5,'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', choices=RATING_CHOICES)
    comment = models.TextField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.id)

class Suggestions(models.Model):
    name = models.CharField(max_length=100)
    suggestions = models.TextField()
