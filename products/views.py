from email import contentmanager
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def productListView(request):
    queryset = Product.objects.all()
    context = {
        "objectList" : queryset
    }
    return render(request, "products/productList.html", context)


def productDeleteView(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../../home")
    context = {
        "object" : obj
    }
    return render(request, "products/productDelete.html", context)

def dynamicLookupView(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object" : obj
    }
    return render(request, "products/productDetail.html", context)



def productCreateView(request):
    myForm = RawProductForm()

    if request.method == "POST":
        myForm = RawProductForm(request.POST)
        if myForm.is_valid():
            #now data is good
            print(myForm.cleaned_data)
            Product.objects.create(**myForm.cleaned_data)
        else:
            print(myForm.errors)
    context = {
        "form" : myForm
    }
    return render(request, "products/productCreate.html", context)

"""
def productCreateView(request):
    initialData = {
        "title" : "Cool title",
        "description" : "awesome product"
    }
    obj = Product.objects.get(id=12)
    form = ProductForm(request.POST or None, instance=obj)

    #if request.method == "POST":
        #newTitle = request.POST.get("title")
        #print(newTitle)
        #Product.objects.create(title=newTitle)   # lage nytt objekt fra formen
    if form.is_valid():
        form.save()

    context = {
        "form" : form
    }
    #form = ProductForm(request.POST or None)
    #if form.is_valid():
    #    form.save()
    #    form = ProductForm()
    #context = {
    #    "form" : form
    #}
    
    return render(request, "products/productCreate.html", context)
"""

def productDetailView(request):
    obj = Product.objects.get(id=1)
    context = {
        "object" : obj
    }
    return render(request, "products/productDetail.html", context)


def homeView(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html", {})

def contactView(request, *args, **kwargs):
    return HttpResponse("<h1>Contact page</h1>")

def aboutView(request, *args, **kwargs):
    myContext = {
        "myText": "this is about us",
        "myNumber" : 123,
        "myList" : [123, 312, 121]
    }  
    return render(request, "about.html", myContext)
