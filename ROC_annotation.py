import xml.etree.cElementTree as et
import os
from PIL import Image
from matplotlib import pyplot as plt

img_path = '/home/travis/data/fundus_img/ROCtraining/'
crop_path = '/home/travis/data/fundus_img/ROCtraining/crop350/'
info_path = '/home/travis/data/fundus_img/ROCtraining/lesion_info.txt'
xml_path = '/home/travis/data/fundus_img/ROCtraining/annotations-consensus-ma-only.xml'
tree = et.parse(xml_path)
root = tree.getroot()
h = 90
# fobj = open(info_path, 'a')

for child in root:
    i = 0
    tag = child.tag
    attr = child.attrib
    img_name = attr.get('imagename')
    for annotation in child:
        mark = annotation.find('mark')
        origin = mark.attrib
        origin_x = origin.get('x')
        origin_y = origin.get('y')
        radius = mark.find('radius')
        r = int(radius.text)
        img = Image.open(img_path + img_name)
        plt.imshow(img)
        temp = os.path.splitext(img_name)[0]
        # x = int(origin_x)-h
        # y = int(origin_y)-h
        # crop_name = img_name + '_'+ i
        # crop = img.crop((x,y,x+2*h,y+2*h))
        coor1 = int(origin_x) - h
        coor2 = int(origin_y) - h
        coor3 = int(origin_x) + h
        coor4 = int(origin_y) + h
        crop = img.crop((coor1, coor2, coor3, coor4))
        crop.save(crop_path + 'ma_' + temp + "_"+str(i)+'.jpg')
        i = i+1

        # fobj.write(img_name + ' ' + origin_x + ' ' + origin_y + ' ' + r + '\n')







