import cv2
import numpy as np
from scipy import ndimage
from scipy.ndimage import label, generate_binary_structure
from PIL import Image

global object1
object1 = (list([]),list([]))

def flood_fill(imageSegment, imageOrig, x, y, replace_value):
    #imageSegment = [list(line) for line in cv2.split(imageSegment)]
    width, height = len(imageSegment[0]), len(imageSegment)
    print (imageSegment)
    print (y)
    print (x)
    print (imageSegment.dtype)
    to_replace = imageSegment[y][x]
    to_fill = set()
    to_fill.add((x, y))
    while to_fill:
        x, y = to_fill.pop()
        if not (0 <= x < width and 0 <= y < height):
            continue
        value = imageSegment[y][x]
        if value.all != to_replace.all:
            continue
        imageOrig[y][x] = replace_value
        to_fill.add((x-1, y))
        to_fill.add((x+1, y))
        to_fill.add((x, y-1))
        to_fill.add((x, y+1))
    return '\n'.join(''.join(line) for line in imageSegment)
def my_filler(imageSegment, imageOrig, x, y, replace_value):
    global object1
    global x_cords
    global y_cords
    print("con same 1")
    print(object1[1])
    #object1 holds two arrays 1 holds x cordinates of boxes 0 holds y cordinates
    x_cords = list(object1[1])
    y_cords = list(object1[0])
    x_cords.append(x)
    y_cords.append(y)
    object1 = (y_cords,x_cords)
    print("after")
    print(object1)
    #object.insert[0,y]
    #object.insert[1,x]
    x_counter = 0

    print(replace_value)
    print(imageSegment[y, x+x_counter])
    while(np.array_equal(replace_value, imageSegment[y, x+x_counter])):
        x_cords.append(x+x_counter)
        y_cords.append(y)
        object1 = (y_cords,x_cords)
        x_counter += 1

    object1 = (y_cords,x_cords)
    imageOrig[object1] = imageSegment[object1]

    return


# mouse callback function
def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #cv2.circle(imgOrig,(x,y),50,(10,50,0),-1)
        selected_area = np.where(np.all( imgSeg == imgSeg[y,x], axis=-1))
        print(selected_area)
        print(type(selected_area))
        #imgOrig[selected_area] = imgSeg[selected_area]
        seed = imgSeg[y,x]
        my_filler(imgSeg, imgOrig, x, y, seed)


# Pick an image to load in a window and bind the function to the window
imgOrig = cv2.imread('frame1073.jpg')
imgSeg  = cv2.imread('segmentation1.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)


while(1):
    cv2.imshow('image',imgOrig)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
