import csv
import os
import random
import shutil

# csvfile = open('trainLabels.csv', 'rb')
# reader = csv.reader(csvfile)
# i = 0
# name = []
# label = []
# for line in reader:
#     if i < 1:
#         i += 1
#     else:
#         name.append(line[0:1])
#         label.append(line[1:])
#         print name,label


imageFile = '/home/travis/data/fundus_img/kaggle_contrast'
pathFile = '/home/travis/software/caffe/examples/mAs_detection/bvlc_googlenet/kaggle_label.txt'
images = []
def maketrainList(imageFile, pathFile):
    fobj = open(pathFile, 'a')
    csvfile = open('trainLabels.csv', 'rb')
    reader = csv.reader(csvfile)
    i = 0
    name1 = []
    label1 = []
    for line in reader:
        if i < 1:
            i += 1
        else:
            name1.append(line[0])
            label1.append(line[1])
    csvfile.close()
    for root, dirs, files in os.walk(imageFile):
        # files.sort()
        for f in files:
            images.append(f)
        num = len(images)
        for j in range(num):
            temp = os.path.basename(images[j])
            temp1 = os.path.splitext(temp)[0]
            ix = name1.index(temp1)
            label = label1[ix]
            fobj.write(images[j] + ' ' + label+'\n')
            print(images[j] + ' ' + label + ' writes to the file successfully ')
    fobj.close()


maketrainList(imageFile, pathFile)