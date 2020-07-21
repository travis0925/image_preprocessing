import os

images=[]
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


maketrainList('/home/travis/software/caffe/examples/mAs_detection/bvlc_googlenet/ma_aug/testingData40', '/home/travis/data/grey_scale_dataset/testLabel_40.txt')
#maketrainList('/home/travis/software/caffe/examples/mAs_detection/bvlc_googlenet/ma_aug/trainingData60', '/home/travis/data/grey_scale_dataset/trainLabel_60.txt')