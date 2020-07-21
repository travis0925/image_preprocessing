import os
import numpy as np
import scipy.ndimage as ndimage
import matplotlib
import matplotlib.pyplot as plt
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


def frac_eq_to(image, value=0):
    return (image == value).sum() / float(np.prod(image.shape))


def extract_patches(image, patchshape, overlap_allowed=0.9, cropvalue=None,
                    crop_fraction_allowed=0.4):
    """
    Given an image, extract patches of a given shape with a certain
    amount of allowed overlap between patches, using a heuristic to
    ensure maximum coverage.

    If cropvalue is specified, it is treated as a flag denoting a pixel
    that has been cropped. Patch will be rejected if it has more than
    crop_fraction_allowed * prod(patchshape) pixels equal to cropvalue.
    Likewise, patches will be rejected for having more overlap_allowed
    fraction of their pixels contained in a patch already selected.
    """
    jump_cols = int(patchshape[1] * overlap_allowed)
    jump_rows = int(patchshape[0] * overlap_allowed)

    # Restrict ourselves to the rectangle containing non-cropped pixels
    if cropvalue is not None:
        rows, cols = np.where(image != cropvalue)
        rows.sort();
        cols.sort()
        active = image[rows[0]:rows[-1], cols[0]:cols[-1]]
    else:
        active = image

    rowstart = 0;
    colstart = 0

    # Array tracking where we've already taken patches.
    covered = np.zeros(active.shape, dtype=bool)
    patches = []

    while rowstart < active.shape[0] - patchshape[0]:
        # Record whether or not e've found a patch in this row,
        # so we know whether to skip ahead.
        got_a_patch_this_row = False
        colstart = 0
        while colstart < active.shape[1] - patchshape[1]:
            # Slice tuple indexing the region of our proposed patch
            region = (slice(rowstart, rowstart + patchshape[0]),
                      slice(colstart, colstart + patchshape[1]))

            # The actual pixels in that region.
            patch = active[region]

            # The current mask value for that region.
            cover_p = covered[region]
            if cropvalue is None or \
                    frac_eq_to(patch, cropvalue) <= crop_fraction_allowed and \
                    frac_eq_to(cover_p, True) <= overlap_allowed:
                # Accept the patch.
                patches.append(patch)

                # Mask the area.
                covered[region] = True

                # Jump ahead in the x direction.
                colstart += jump_cols
                got_a_patch_this_row = True
                # print "Got a patch at %d, %d" % (rowstart, colstart)
            else:
                # Otherwise, shift window across by one pixel.
                colstart += 1

        if got_a_patch_this_row:
            # Jump ahead in the y direction.
            rowstart += jump_rows
        else:
            # Otherwise, shift the window down by one pixel.
            rowstart += 1

    # Return a 3D array of the patches with the patch index as the first
    # dimension (so that patch pixels stay contiguous in memory, in a
    # C-ordered array).
    return np.concatenate([pat[np.newaxis, ...] for pat in patches], axis=0)
patch_shape = [175,175]
labelFile = '/home/travis/data/grey_scale_dataset/kaggle_patch_label.txt'
annotation_path = '/home/travis/data/fundus_img/trainLabels.csv'
img_path = '/home/travis/data/grey_scale_dataset/training1'
destination = '/home/travis/data/grey_scale_dataset/training2/'
images = []
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
        # label1.append(line[2])
        label1.append(line[1])
csvfile.close()
fobj = open(labelFile,'a')
for j in range(num_of_img):
    temp = os.path.basename(images[j])
    temp1 = os.path.splitext(temp)[0]
    temp2 = temp1 + '.tif'
    ix = name.index(temp2)
    # ix = name.index(temp1)
    label = label1[ix]
    img = cv2.imread(images[j])
    patches = extract_patches(img, patch_shape)
    num_of_patch = len(patches)
    for k in range(num_of_patch):
        cv2.imwrite(destination+temp1+str(k)+'.jpg', patches[k][:,:,1])
        fobj.write(temp1+str(k)+'.jpg'+' '+label+'\n')
        print(temp1+str(k)+'.jpg'+' '+label+'writes to the file successfully')

fobj.close()
