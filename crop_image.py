import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('/home/travis/data/data1/messidor/contrast/base23_contrast/20060411_61478_0200_PP.tif')
img = cv2.imread('/home/travis/data/data1/messidor/contrast/base21_contrast/20060407_39780_0200_PP.tif',0)
# Read in your image
# edges = cv2.Canny(img,0, 30)
# kernel = np.ones((40,40),np.uint8)

# edges = cv2.Canny(img, 100, 210)
# kernel = np.ones((95, 95), np.uint8)


def auto_canny(image, sigma = 0.2):
    v = np.median(image)
    lower = int(max(5,(1.0-sigma)*v))
    upper = int(min(250,(1.0+sigma)*v))
    edged = cv2.Canny(image, lower, upper)
    return image


edges = auto_canny(img)
kernel = np.ones((95, 95), np.uint8)

erosion = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
plt.subplot(1,3,1),plt.imshow(erosion,'gray')
plt.subplot(1,3,2),plt.imshow(edges, 'gray')
image, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
x, y, w, h = cv2.boundingRect(cnt)
# img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
crop_img = img[y:y+h, x:x+w]


plt.subplot(1,4,1),plt.imshow(img,'gray')
plt.subplot(1,4,2),plt.imshow(edges,'gray')
plt.subplot(1,4,3),plt.imshow(erosion,'gray')
plt.subplot(1,4,4),plt.imshow(crop_img,'gray')


plt.show()
print 'done'

