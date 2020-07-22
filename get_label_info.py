

import csv
import os
import random
import shutil


imageFile = '' # image file path
pathFile = '' # generated label file path
images = []
def maketrainList(imageFile, pathFile):
    fobj = open(pathFile, 'a')
    csvfile = open('trainLabels.csv', 'rb') # orginal csv file path
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
