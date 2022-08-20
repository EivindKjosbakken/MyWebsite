from email import contentmanager
from sqlite3 import connect

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project, Image

from projects.forms import ImageForm, Image

from projects.forms import ImageForm
# Create your views here.


# import some common libraries
import numpy as np
import os, json, random
import sys


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
    context={}
    return render(request, "warehouseSimulationShowcase.html", context)


def detectron2Showcase(request):
   
    #Process images uploaded by users
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            #img_obj = detectObjects(img_obj)

            return render(request, "detectron2Showcase.html", {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, "detectron2Showcase.html", {'form': form})

