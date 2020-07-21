import os
import cv2

img_path1 = '/home/travis/data/IOVS_data/PATCHES'
img_path2 = '/home/travis/data/data1/IOVS'
destination_path = '/home/travis/data/data1/IOVS_original/'

images = []
for root, dirs, files in os.walk(img_path2):
    for f in files:
        if os.path.splitext(f)[1] == '.jpg':
            print os.path.splitext(f)[1]
            images.append(f)
    num = len(images)
    for i in range(num):
        temp = os.path.basename(images[i])
        temp1 = os.path.splitext(temp)[0]
        img = cv2.imread(img_path1+'/' + temp1+'.jpeg')
        img1 = cv2.imwrite(destination_path + temp, img)


