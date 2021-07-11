'''
Created on Jul 11, 2021
@author: nicomp

Adapted from https://stackoverflow.com/questions/61758071/how-to-blackout-area-outside-circle-with-opencv-python
'''
import cv2
import numpy as np

    
def addCircleToImage(fileName, extension):
    
    # read image
    img = cv2.imread(fileName + "." + extension)
    
    # Grab height and width
    hh, ww = img.shape[:2]
    
    # Compute center point
    hh2 = hh // 2
    ww2 = ww // 2
    
    # define circle parameters
    radius = hh2
    yc = hh2
    xc = ww2
    
    print ("height = " + str(hh) + ", width = " + str(ww))
    print ("x center = " + str(ww2) + ", y center = " + str(hh2))
    
    # draw filled circle in white on black background as mask
    mask = np.zeros_like(img)
    mask = cv2.circle(mask, (xc,yc), radius, (255,255,255), -1)
    
    # apply mask to image
    result = cv2.bitwise_and(img, mask)
    
    # save results
    cv2.imwrite(fileName + '_mask' + '.' + extension, mask)
    cv2.imwrite(fileName + '_masked' + '.' + extension, result)
    
#   cv2.imshow('image', img)
#   cv2.imshow('mask', mask)
    cv2.imshow('masked image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
#   addCircleToImage("rhino", "jpg")    
#    addCircleToImage("SiriusAndViolet", "jpg")
    addCircleToImage("IMAG9758", "jpg")
    
    