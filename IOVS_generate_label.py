import os
import shutil

# image_path = '/home/travis/data/IOVS_data/resized_IOVS'
# image_path = '/home/travis/software/caffe/examples/mAs_detection/bvlc_googlenet/ma_aug/testingData40'
image_path = '/home/travis/software/caffe/examples/mAs_detection/bvlc_googlenet/ma_aug/trainingData60'
labelFile = '/home/travis/data/grey_scale_dataset/trainLabel_60.txt'
# destination = '/home/travis/data/grey_scale_dataset/test'
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