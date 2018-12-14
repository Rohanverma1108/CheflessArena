from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('',home.as_view(),name='home'),
    path('Profile/',profile,name='profile'),
    path('Register/',restaurant,name='restro'),
    path('Dish/',dish),
    path('Restaurant/',restaurantList,name='restList'),
    path('Restaurant/<int:id>',restaurantShow,name='show'),
    path('Restaurant/<int:id>/Dishes/',dishes,name='dishes'),
    path('Restaurant/<int:r_id>/Dishes/<int:id>/',dishesEdit),
    path('Restaurant/<int:r_id>/Review/',review,name='review'),
    path('delete/<int:r_id>/<int:id>',delete,name='delete'),
    path('update/<int:id>',update,name='update'),
    path('Suggestions/',suggestions,name= 'suggestions'),
    path('Signup/',signup,name='signup'),
    path('Login/',loginUser,name='loginUser'),
    path('Logout/',logoutUser,name='logoutUser'),
    path('ChangePassword/',changePassword,name='changePass'),
    path('aboutus/',TemplateView.as_view(template_name='aboutus.html'),name='aboutus')
]
