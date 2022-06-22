from django.contrib import admin
from django.urls import path, include
from products.views import homeView, contactView, aboutView, productDetailView, productCreateView, dynamicLookupView, productDeleteView, productListView


#app_name brukes for modellen og sikrer unike navn
app_name = "products"
urlpatterns = [

    path("<int:id>/", dynamicLookupView, name="productDetail"),
    path("<int:id>/delete/", productDeleteView),
    


]
