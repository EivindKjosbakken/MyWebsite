"""tryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import homeView, contactView, aboutView, productDetailView, productCreateView, dynamicLookupView, productDeleteView, productListView

from users.views import userView, userCreateView, userViewAllView
from familyMember.views import createMemberView, specificMemberView, memberListView

from projects.views import allProjectsView, lifesimGameShowcase, detectron2Showcase
from projects import views



urlpatterns = [

    path("products/", include("products.urls")),
   
    path('admin/', admin.site.urls),
    path('', homeView, name="home"),
    path('home', homeView, name="home"),
    path('contact/', contactView, name="contact"),
    path('about/', aboutView, name="about"),
    path('create/', productCreateView),
    path("productList/", productListView, name="productList"),

    path("users/", userView, name="userView"),
    path("createUser/", userCreateView, name="userCreateView"),

    path("createMember/", createMemberView, name="createMemberView"),
    path("specificMember/<int:id>", specificMemberView, name="specificMemberView"),
    path("memberList/", memberListView, name="memberList"),
    path("viewAll/", userViewAllView, name="viewAll"),


    #projects:
    path("projectList/", allProjectsView, name="allProjects"),
    path("projectList/lifesimGameShowcase", lifesimGameShowcase, name="lifesimGame"),
    path("projectList/detectron2Showcase", detectron2Showcase, name="detectron2"),

    path('admin/', admin.site.urls),
    #path('', views.index), #TODO fikse her

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)