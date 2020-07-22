# This file is used for generating coco style json files while running experiments with Dectron.

import argparse
import json
import matplotlib.pyplot as plt
import skimage.io as io
import cv2
from labelme import utils
import numpy as np
import glob
import PIL.Image
from shapely.geometry import Polygon

class labelme2coco(object):
    def __init__(self,labelme_json=[],save_json_path='./new.json'):
        '''
        :param labelme_json: a list of all labelme json files
        :param save_json_path: final json file path
        '''
        self.labelme_json=labelme_json
        self.save_json_path=save_json_path
        self.images=[]
        self.categories=[]
        self.annotations=[]
        # self.data_coco = {}
        self.label=[]
        self.annID=1
        self.height=0
        self.width=0

        self.save_json()

    def data_transfer(self):
        for num,json_file in enumerate(self.labelme_json):
            with open(json_file,'r') as fp:
                data = json.load(fp)  # load json files
                self.images.append(self.image(data,num))
                for shapes in data['shapes']:
                    label=shapes['label'].split('_')
                    print(shapes['label'])
                    print(label)
                    if label[0] not in self.label:
                        self.categories.append(self.categorie(label))
                        self.label.append(label[0])
                    points=shapes['points']
                    self.annotations.append(self.annotation(points,label,num))
                    self.annID+=1
        print(self.label)

    def image(self,data,num):
        image={}
        img = utils.img_b64_to_array(data['imageData'])  
        height, width = img.shape[:2]
        img = None
        image['height']=height
        image['width'] = width
        image['id']=num+1
        image['file_name'] = data['imagePath'].split('/')[-1]

        self.height=height
        self.width=width

        return image

    def categorie(self,label):
        categorie={}
        categorie['supercategory'] = label
        categorie['id']=len(self.label)+1 
        categorie['name'] = label
        return categorie

    def annotation(self,points,label,num):
        annotation={}
        annotation['segmentation']=[list(np.asarray(points).flatten())]
        poly = Polygon(points)
        area_ = round(poly.area,6)
        annotation['area'] = area_
        annotation['iscrowd'] = 0
        annotation['image_id'] = num+1
        annotation['bbox'] = list(map(float,self.getbbox(points)))

        annotation['category_id'] = self.getcatid(label)
        annotation['id'] = self.annID
        return annotation

    def getcatid(self,label):
        for categorie in self.categories:
            if label==categorie['name']:
                return categorie['id']
        return -1

    def getbbox(self,points):
        polygons = points
        mask = self.polygons_to_mask([self.height,self.width], polygons)
        return self.mask2box(mask)

    def mask2box(self, mask):

        index = np.argwhere(mask == 1)
        rows = index[:, 0]
        clos = index[:, 1]
        
        left_top_r = np.min(rows)  # y
        left_top_c = np.min(clos)  # x

        
        right_bottom_r = np.max(rows)
        right_bottom_c = np.max(clos)

        # return [(left_top_r,left_top_c),(right_bottom_r,right_bottom_c)]
        # return [(left_top_c, left_top_r), (right_bottom_c, right_bottom_r)]
        # return [left_top_c, left_top_r, right_bottom_c, right_bottom_r]  # [x1,y1,x2,y2]
        return [left_top_c, left_top_r, right_bottom_c-left_top_c, right_bottom_r-left_top_r]  # [x1,y1,w,h] a COCO style bbox

    def polygons_to_mask(self,img_shape, polygons):
        mask = np.zeros(img_shape, dtype=np.uint8)
        mask = PIL.Image.fromarray(mask)
        xy = list(map(tuple, polygons))
        PIL.ImageDraw.Draw(mask).polygon(xy=xy, outline=1, fill=1)
        mask = np.array(mask, dtype=bool)
        return mask

    def data2coco(self):
        data_coco={}
        data_coco['images']=self.images
        data_coco['categories']=self.categories
        data_coco['annotations']=self.annotations
        return data_coco

    def save_json(self):
        self.data_transfer()
        self.data_coco = self.data2coco()
        # save json file
        json.dump(self.data_coco, open(self.save_json_path, 'w'), indent=4)  

labelme_json=glob.glob('detectron/detectron/datasets/data/train/*.json')
# labelme_json=['./1.json']

labelme2coco(labelme_json,'./new2.json')
