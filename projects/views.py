from email import contentmanager
from sqlite3 import connect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project
# Create your views here.


def allProjectsView(request):
    queryset = Project.objects.all()
    context = {
        "projectListList" : queryset
    }
    return render(request, "projectList.html", context)


def lifesimGameShowcase(request):
    context = {}
    return render(request, "lifesimGameShowcase.html", context)

def warehouseSimulationShowcase(request):
    context = {}
    return render(request, "warehouseSimulationShowcase.html", context)
    
def detectron2Showcase(request):
    context = {}
    return render(request, "detectron2Showcase.html", context) 