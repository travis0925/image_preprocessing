import os
from PIL import Image
from matplotlib import pyplot as plt
import xml.etree.cElementTree as et

img_path = '/home/travis/data/fundus_img/ROCtraining/ROC_selected'
crop_path = '/home/travis/data/fundus_img/ROCtraining/180/'
xml_path = '/home/travis/data/fundus_img/ROCtraining/annotations-consensus-ma-only.xml'
tree = et.parse(xml_path)
root = tree.getroot()
images = []

for root1, dirs, files in os.walk(img_path):
    for f in files:
        if os.path.splitext(f)[1] == '.jpg':
            print os.path.splitext(f)[1]
            images.append(f)
    num = len(images)
    for child in root:
        i = 0
        tag = child.tag
        attr = child.attrib
        img_name = attr.get('imagename')
        if img_name in images:
            for annotation in child:
                mark = annotation.find('mark')
                origin = mark.attrib
                origin_x = origin.get('x')
                origin_y = origin.get('y')
                radius = mark.find('radius')
                r = int(radius.text)
                x1 = int(origin_x) - 90
                y2 = int(origin_y) - 90
                x2 = int(origin_x) + 90
                y1 = int(origin_y) + 90

                img = Image.open(img_path + '/' + img_name)
                plt.imshow(img)
                temp = os.path.splitext(img_name)[0]
                crop = img.crop((x1, y2, x2, y1))
                crop.save(crop_path + 'ma_' + temp + "_" + str(i) + '.jpg')
                i = i + 1


        else:
            continue



