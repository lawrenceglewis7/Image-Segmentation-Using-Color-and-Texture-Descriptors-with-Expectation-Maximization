import cv2
from scipy import ndimage
from scipy.ndimage import label, generate_binary_structure
import numpy as np
from PIL import Image

# Load image and ensure RGB - just in case palettised
im = Image.open("segmentation1.png").convert("RGB")

# Make numpy array from image
npimage = np.array(im, dtype=np.uint8)

# Assume we were told to take pixel [17,483] as our seed
seed = npimage[17,483]

# If we had been given a seed colour instead, e.g. red, we would do
# seed = np.array((255,0,0), dtype=np.uint8)

# Make greyscale mask image, generally black but white where same colour as seed
mask = (np.all((npimage==seed),axis=-1)*255).astype(np.uint8)


# The default SE (structuring element) is for 4-connectedness, i.e. only pixels North, South, East and West of another are considered connected.
# Pixels in our wedge are 8-connected, i.e. N, NE, E, SE, S, SW, W, NW, so we need a corresponding SE
SE = generate_binary_structure(2,2)   

# Now run a labelling, or "Connected Components Analysis"
# Each "blob" of connected pixels matching our seed will get assigned a unique number in the new image called "labeled"
labeled, nr_objects = ndimage.label(mask, structure=SE)

print('Num objects found: {}'.format(nr_objects))

# Get label assigned to our blob, and its area
ourlabel = labeled[250,350]
area     = np.bincount(labeled.flat)[ourlabel:ourlabel+1]
print('Our blob got label: {} and has area: {}'.format(ourlabel,area))

# Now print list of pixels in our blob
print(*np.argwhere(labeled==ourlabel))
#while(1):
    #cv2.imshow('singleobjedt',mask)
    #if cv2.waitKey(20) & 0xFF == 27:
        #break
#cv2.destroyAllWindows()