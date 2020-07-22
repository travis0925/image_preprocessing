# The following codes are used for generating a label file in txt format, according to the the keyword in the file name. It is written with python 2.6, 
# which can be easily modified with a higher version of python.

import os
import shutil

image_path = '' # Your file path here
labelFile = '' # location of the generated label file

fobj = open(labelFile, 'a')
images = []

def preprocessing(dir,images):
    newDir = dir
    if os.path.isfile(dir):
        images.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir,s)
            preprocessing(newDir, images)
    return images


images = preprocessing(image_path,images)
num = len(images)
for i in range(num):
    temp =os.path.basename(images[i])
    temp1 = os.path.splitext(temp)[0]
    if 'norm' in temp1:
        fobj.write(temp+' '+'0'+'\n')
        # shutil.copy(images[i],destination)
        print(temp+' '+ '0' + 'writes to the file successfully')
    elif 'ma' in temp1:
        fobj.write(temp+' '+'1'+'\n')
        # shutil.copy(images[i],destination)
        print(temp+' '+ '1' + 'writes to the file successfully')
    elif 'dbh' in temp1:
        fobj.write(temp+' '+'2'+'\n')
        # shutil.copy(images[i],destination)
        print(temp+' '+ '2' + 'writes to the file successfully')
    elif 'ex' in temp1:
        fobj.write(temp+' '+'3'+'\n')
        # shutil.copy(images[i],destination)
        print(temp+' '+ '3' + 'writes to the file successfully')
