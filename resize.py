import cv2
import csv
import os
import numpy as np
from matplotlib import pyplot as plt

img_path = '/home/travis/data/data1/IOVS_original'
destination_path = '/home/travis/data/data1/IOVS180/'
images = []
height, width = 180, 180
for root, dirs, files in os.walk(img_path):
    for f in files:
        images.append(f)
    num = len(images)
    for i in range(num):
        temp = os.path.basename(images[i])
        temp1 = os.path.splitext(temp)[0]
        img = cv2.imread(img_path+'/'+images[i])
        resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        l = destination_path + temp1 + '.jpg'
        print l
        cv2.imwrite(destination_path + temp1 + '.jpg', resized_img)






# img = cv2.imread('/home/travis/machine_learning/data/15040_left.jpeg')
# resized_img = cv2.resize(img, (width, height), interpolation = cv2.INTER_CUBIC)
# cv2.imwrite(destination_path+'test.jpg', resized_img)
# plt.subplot(1, 2, 1), plt.imshow(img)
# plt.subplot(1, 2, 2), plt.imshow(resized_img)
# plt.show()