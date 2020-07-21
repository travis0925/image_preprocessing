import os
import cv2
import csv

def preprocessing(dir,images):
    newDir = dir
    if os.path.isfile(dir):
        images.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir,s)
            preprocessing(newDir, images)
    return images

destination = '/home/travis/data/grey_scale_dataset/training2/'
img_path = '/home/travis/data/grey_scale_dataset/training1'
images = []
labelFile = '/home/travis/data/grey_scale_dataset/Messidor_patch_label.txt'
annotation_path = '/home/travis/data/data1/messidor/Annotation_Base1.csv'
images = preprocessing(img_path,images)
num_of_img = len(images)
csvfile = open(annotation_path)
reader = csv.reader(csvfile)
i = 0
name = []
label1 = []
for line in reader:
    if i < 1:
        i += 1
    else:
        name.append(line[0])
        label1.append(line[2])
        # label1.append(line[1])
csvfile.close()
fobj = open(labelFile,'a')
for j in range(num_of_img):
    temp = os.path.basename(images[j])
    temp1 = os.path.splitext(temp)[0]
    name1 = temp1.split('PP')[0]
    temp2 = name1 +'PP'+'.tif'
    ix = name.index(temp2)
    # ix = name.index(temp1)
    label = label1[ix]
    fobj.write(temp1+'.jpg'+' '+label+'\n')
    print(temp1+'.jpg'+' '+label+'writes to the file successfully')
fobj.close()




def maketrainList(imageFile, pathFile):
    fobj = open(pathFile, 'a')
    for root,dirs,files in os.walk(imageFile):
        files.sort()
        for f in files:
            images.append(f)
        num = len(images)
        for i in range(num):
            # label = images[i].split('_')[1]
            base = os.path.basename(images[i])
            base1 = os.path.splitext(base)[0]
            label = base1.split('_')[1]
            print label
            # print files
            fobj.write(images[i] + ' ' + label+'\n')
            print(images[i] + ' ' + label + ' writes to the file successfully ')
    fobj.close()



