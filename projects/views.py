from email import contentmanager
from sqlite3 import connect

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project, Image

from projects.forms import ImageForm, Image

from projects.forms import ImageForm
# Create your views here.



""" TODO
# import some common detectron2 utilities (not in use now since it is not working)
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.structures import BoxMode
import torch
import torchvision
import detectron2
from detectron2.utils.logger import setup_logger
from detectron2.data.datasets import register_coco_instances
import detectron2
from detectron2.utils.logger import setup_logger
import cv2
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.utils.visualizer import ColorMode
setup_logger()
"""
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

#""" 
#TODO not in use now since object detector is not working
#def detectObjects(im):

   # from detectron2.engine import DefaultTrainer

   # SHOULD_TRAIN = False

   # cfg = get_cfg()
   # cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
   # #cfg.DATASETS.TRAIN = ("tdt4265_dataset_train",)
   # cfg.DATASETS.TEST = ()
   # cfg.DATALOADER.NUM_WORKERS = 0
   # cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")  # Let training initialize from model zoo
   # cfg.SOLVER.IMS_PER_BATCH = 2
   # cfg.SOLVER.BASE_LR = 5e-3 #same lr as in other models  
   # cfg.SOLVER.MAX_ITER = 10000    # same number of steps as original model
   # cfg.SOLVER.STEPS = []        # could decay lr here
   # cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 512   
   # cfg.MODEL.ROI_HEADS.NUM_CLASSES = 9  #9 classes which which the tdt4265 dataset has

   # os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
 #   if (SHOULD_TRAIN):
 #       trainer = DefaultTrainer(cfg) 
 #       trainer.resume_or_load(resume=False)
#
 #       trainer.train() #if cfg not found, comment out this, and run the cell (so it finds the cfg, but doesnt train)
 #   # Running inference 
 #   cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "C:/Users/eivin/OwnProjects/MyWebsite/projects/out#put/model_final.pth")  # path to model
 #   cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set a iou threshhold to what I used in other models

#    import cv2
#    
#    import glob
#   
#    folder_path = r'C:\Users\eivin\OwnProjects\MyWebsite\media\images'
#    file_type = r'\*jpg'
#    files = glob.glob(folder_path + file_type)
#    max_file = max(files, key=os.path.getctime)
#    print("LATEST file is:", max_file)
#    import time
#    #time.sleep(2)
#    # read image 
#    #print("IMAGE ER:", image)
#    im = cv2.imread(max_file)
#    #im=np.uint8(im)
#    cv2.imshow('image window', im)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#

#    predictor = DefaultPredictor(cfg)
#

#    #Running inference on custom images. Works pretty well, even works for all image shapes (not just 1024 width, 128 height), but does not show labels
#    from detectron2.utils.visualizer import ColorMode
#    
#

    #outputs = predictor(im)
    #v = Visualizer(im[:, :, ::-1],
    #                #metadata=valMetaData, 
    #                scale=1.2, 
    #                instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels. This option is only available for segmentation models
    #)
    #out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

    #cv2.imshow("image", out.get_image()[:, :, ::-1])
   # cv2.waitKey(0) 
  #  #closing all open windows 
 #   cv2.destroyAllWindows() 
#    return out

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

