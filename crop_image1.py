from skimage import data, segmentation
from skimage import filter
import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('/home/travis/data/data1/messidor/contrast/base11_contrast/20051019_38557_0100_PP.tif',0)
mask = img > filter.threshold_otsu(img)
clean_border = segmentation.clear_border(mask).astype(np.int)

img_edges = segmentation.mark_boundaries(img, clean_border)

plt.figure(figsize=(8,3.5))
plt.subplot(121)
plt.imshow(clean_border, cmap='gray')
plt.axis('off')
plt.subplot(122)
plt.imshow(img_edges)
plt.axis('off')

plt.tight_layout()
plt.show()
