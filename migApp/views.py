from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from rest_framework import viewsets
from .serializers import DishSerializers


# Create your views here.
class home(TemplateView):
    template_name='home.html'

def profile(request):
    return render(request,'profile.html')

def restaurantList(request):
    res = Restaurant.objects.all()
    context = {'restro':res}
    return render(request,'restaurantList.html',context)

def restaurant(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = int(request.POST['number'])
        street = request.POST['street']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        stateOrProvince = request.POST['stateOrProvince']
        country = request.POST['country']
        telephone = request.POST['telephone']
        restObj = Restaurant(
            name=name,
            number=number,
            street=street,
            city=city,
            zipcode=zipcode,
            stateOrProvince=stateOrProvince,
            country=country,
            telephone=telephone
        )
        restObj.save()
        return redirect('/')
    return render(request,'restaurant.html')

def dish(request):
    return render(request,'dish.html')

def review(request,r_id):
    if request.method == 'POST':
        rating = request.POST['rating_choice']
        comment = request.POST['description']
        restObj = Restaurant.objects.get(id=r_id)
        restaurant = restObj
        revObj = Review(
        rating = rating,
        comment = comment,
        restaurant = restaurant
        )
        revObj.save()
        return redirect('/Restaurant/{0}'.format(r_id))

    res = Restaurant.objects.get(id=r_id)
    context={'restro':res}
    return render(request,'review.html',context)

def restaurantShowAll(request):
    res=Restaurant.objects.all()
    context={'restro':res}
    return render(request,'restaurantShowAll.html',context)

@login_required()
def restaurantShow(request,id):
    res = Restaurant.objects.get(id=id)
    rev = Review.objects.filter(restaurant=id).order_by('-rating')

    paginator = Paginator(rev,2)
    page = request.GET.get('page')
    reviews = paginator.get_page(page)

    context = {'restro':res,'revi':reviews}
    return render(request,'restaurantShow.html',context)

def dishes(request,id):
    dis = Dish.objects.filter(restaurant=id)
    context = {'dishObj':dis}
    return render(request,'dishesShow.html',context)

def dishesEdit(request,r_id,id):
    dis = Dish.objects.get(id=id)
    rest = Restaurant.objects.all()
    context = {'dishObj':dis , 'restObj':rest}
    return render(request,'dish.html',context)

def delete(request,r_id,id):
    obj = Review.objects.get(id=id)
    obj.delete()
    return redirect('/Restaurant/{0}'.format(r_id))

def signup(request):
    if request.method=='POST':
       form1=SignUpForm(request.POST)
       if form1.is_valid():
           username=form1.cleaned_data['username']
           first_name = form1.cleaned_data['first_name']
           last_name = form1.cleaned_data['last_name']
           email = form1.cleaned_data['email']
           password = form1.cleaned_data['password']
           User.objects.create_user(username=username,
           first_name=first_name,last_name=last_name,
           email=email,password=password)
           messages.success(request,'Yay! {0} , You are now part of Chefless Arena.'.format(username))

           send_mail(
            'Chefless Arena',
            'Hello {0}, You are now part of Chefless Arena. Login to explore more. Link : localhost:8000/Login/'.format(username),
            'smartersmart69@gmail.com',
            [email],
            fail_silently=False,
           )

           return redirect('/')
    suForm = SignUpForm()
    context = {'suForm':suForm}
    return render(request,'signup.html',context)

def loginUser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('<h1>invalid</h1>')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def update(request,id):
    reviObj = Review.objects.get(id=id)
    restObj = reviObj.restaurant
    context_new = {'revi':reviObj , 'restro':restObj}
    return render(request,'review.html', context_new)

def suggestions(request):
    if request.method=='POST':
        form = SuggestionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Done Nigg* </h1>')
        else:
            return HttpResponse('<h1> Try Again </h1>')
    else:
        form = SuggestionForm()
    context = {'form' : form}
    return render(request,'suggestions.html',context)

def changePassword(request):
    user = request.user
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            return redirect('Login/')
    else:form = ChangePasswordForm()
    return render(request,'password.html',{'form':form})







# class EmployeeListView(ListView):
#     template_name = 'show.html'
#     model = Employee
#
#     def get_context_data(self,**kwargs):
#         context = super(EmployeeList,self).get_context_data(**kwargs)
#         qs1 = Employee.objects.all()
#         context.update({
#             'users' : qs1
#         })
#         return context
#
#
#
#
#
#
################# pass primary key in url : path('emp/<int:pk>',EmployeeDetail.as_view(),name='employeeDetail')
#
#           name inside <int : mention_name_here> matters.
#
# class EmployeeDetail(DetailView):
#    template_name = 'employee_list.html'
#    queryset = Employee.objects.all() ################### Dont need this if modifying via get_object(self)
#    context_object_name='emp'
#
#    def get_object(self):
#     id_ = self.kwargs.get('id')
#     return get_objector_404(Employee,id=id_)
#
#
#
#
#
#
#
#

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializers
