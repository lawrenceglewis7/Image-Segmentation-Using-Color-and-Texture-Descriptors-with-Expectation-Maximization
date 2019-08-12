import cv2
import numpy as np
from scipy import ndimage
from scipy.ndimage import label, generate_binary_structure
from PIL import Image

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #cv2.circle(imgOrig,(x,y),50,(10,50,0),-1)
        print("x=")
        print(x)
        print("y=")
        print(y)
        selected_area = np.where(np.all( imgSeg == imgSeg[y,x], axis=-1))
        imgOrig[selected_area] = imgSeg[selected_area]
        seed = imgSeg[y,x]

        #imgOrig[np.argwhere(labeled==ourlabel)] = imgSeg[np.argwhere(labeled==ourlabel)]

# Pick an image to load in a window and bind the function to the window
imgOrig = cv2.imread('factory.jpg')
imgSeg  = cv2.imread('segmentation1.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',imgOrig)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
