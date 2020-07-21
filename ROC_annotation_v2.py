import xml.etree.cElementTree as et
import os
from PIL import Image
from matplotlib import pyplot as plt

img_path = '/home/travis/data/fundus_img/ROCtraining/'
crop_path = '/home/travis/data/fundus_img/ROCtraining/crop2/'
info_path = '/home/travis/data/fundus_img/ROCtraining/roc_coor1.txt'
xml_path = '/home/travis/data/fundus_img/ROCtraining/annotations-consensus-ma-only.xml'
tree = et.parse(xml_path)
root = tree.getroot()
h = 60
fobj = open(info_path, 'a')

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
        # coor1 = int(origin_x) - r
        # coor2 = int(origin_y) - r
        # coor3 = int(origin_x) + r
        # coor4 = int(origin_y) + r
        x1 = int(origin_x) - r
        y2 = int(origin_y) - r
        x2 = int(origin_x) + r
        y1 = int(origin_y) + r
        # img = Image.open(img_path + img_name)
        # plt.imshow(img)
        temp = os.path.splitext(img_name)[0]
        # x = int(origin_x)-h
        # y = int(origin_y)-h
        # # crop_name = img_name + '_'+ i
        # crop = img.crop((x,y,x+2*h,y+2*h))
        # crop.save(crop_path + 'ma_' + temp+ "_"+str(i)+'.jpg')
        i = i+1

        # fobj.write('ma' + ' ' + str(coor1) + ' ' + str(coor2) + ' ' + str(coor3) + ' ' + str(coor4) + '\n')
        fobj.write(temp + '\n' 
                   '    {'+'\n'+'      "line_color": null, '+'\n'
                    + '      "points": [' +
                   '\n' + '        [' + '\n' + '          ' + str(x1) + ',' + '\n' + '          ' + str(y2) + '\n' + '        ],'
                   + '\n' + '        [' + '\n' + '          ' + str(x2) + ',' + '\n' + '          ' + str(y2) + '\n' + '        ],'
                   + '\n' + '        [' + '\n' + '          ' + str(x2) + ',' + '\n' + '          ' + str(y1) + '\n' + '        ],'
                   + '\n' + '        [' + '\n' + '          ' + str(x1) + ',' + '\n' + '          ' + str(y1) + '\n' + '        ]'
                   + '\n' + '      ],' + '\n' + '      "fill_color": null,' + '\n' + '      "label": "ma"' + '\n' + '    },' + '\n ')







