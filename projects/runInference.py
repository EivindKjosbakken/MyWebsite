

import numpy as np
import os, json, random, sys


""" TODO not in use now since object detector is not working
# import some common detectron2 utilities
import cv2

from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.structures import BoxMode
import torch
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
from typing import Dict, List
from detectron2.data.datasets import register_coco_instances
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.utils.visualizer import ColorMode
"""


""" TODO not in use now since object detector is not working
def detectObjects(im):

    from detectron2.engine import DefaultTrainer

    SHOULD_TRAIN = False

    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
    #cfg.DATASETS.TRAIN = ("tdt4265_dataset_train",)
    cfg.DATASETS.TEST = ()
    cfg.DATALOADER.NUM_WORKERS = 0
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")  # Let training initialize from model zoo
    cfg.SOLVER.IMS_PER_BATCH = 2
    cfg.SOLVER.BASE_LR = 5e-3 #same lr as in other models  
    cfg.SOLVER.MAX_ITER = 10000    # same number of steps as original model
    cfg.SOLVER.STEPS = []        # could decay lr here
    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 512   
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 9  #9 classes which which the tdt4265 dataset has

    os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
    if (SHOULD_TRAIN):
        trainer = DefaultTrainer(cfg) 
        trainer.resume_or_load(resume=False)

        trainer.train() #if cfg not found, comment out this, and run the cell (so it finds the cfg, but doesnt train)

    # Running inference 
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")  # path to model
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set a iou threshhold to what I used in other models
    predictor = DefaultPredictor(cfg)


    #Running inference on custom images. Works pretty well, even works for all image shapes (not just 1024 width, 128 height), but does not show labels
    from detectron2.utils.visualizer import ColorMode
    


    outputs = predictor(im)
    v = Visualizer(im[:, :, ::-1],
                    #metadata=valMetaData, 
                    scale=1.2, 
                    instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels. This option is only available for segmentation models
    )
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

    cv2.imshow("image", out.get_image()[:, :, ::-1])
    cv2.waitKey(0) 
    #closing all open windows 
    cv2.destroyAllWindows() 
 #CHOOSE IMAGE:
im = cv2.imread("./try1img.jpg")
#im = cv2.imread("./try2img.jpg")
detectObjects(im)
"""


