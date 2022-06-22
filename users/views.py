from email import contentmanager
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.


#where you can view all the users
def userView(request, *args, **kwargs):
    #obj = User.objects.get(id=1)
    #return HttpResponse("<h1>User page</h1>")
    context = {
        
    }
    return render(request, "users/userView.html", context)


def userCreateView(request, *args, **kwargs):
    myForm = UserForm()

    if request.method == "POST":
        myForm = UserForm(request.POST)
        if myForm.is_valid():
            print("good stuff")
            User.objects.create(**myForm.cleaned_data)
        else:
            print("something went wrong")
    context = {
        "form" : myForm
    }
    return render(request, "users/signupView.html", context)


def userViewAllView(request, *args, **kwargs):
    queryset = User.objects.all()
    context = {
        "objectList" : queryset
    }
    return render(request, "users/viewAll.html", context)