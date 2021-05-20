#!/usr/bin/env python
# coding: utf-8

#system setup
import os
import sys
sys.path.append(os.path.join(".."))

import cv2
import numpy as np

from utils.imutils import jimshow
from utils.imutils import jimshow_channel
import matplotlib.pyplot as plt

#defining whole script as main
def main():

    #defining image path
    filename = os.path.join("..", "data", "assignment3_pic.jpg")

    #reading in image
    image = cv2.imread(filename)

    #showing the picture for sanity check
    jimshow(image)

    #printing shape of the image to be able to make a guess about where the ROI should be
    image.shape

    #drawing a green rectangle on the image
    roi_image = cv2.rectangle(image, (1400, 880), (2900, 2800), (0,255,0), 3)
    #showing the ROI image for sanity check
    jimshow(roi_image, "ROI")

    #saving roi image to output folder
    outfile = os.path.join("..", "output", "image_with_ROI.jpg")
    cv2.imwrite(outfile, roi_image)

    #cropping original image to only roi
    cropped = image[880:2800, 1400:2900]
    #showing the cropped image for sanity check
    jimshow(cropped, "Cropped image")

    #saving cropped image to output file
    outfile = os.path.join("..", "output", "image_cropped.jpg")
    cv2.imwrite(outfile, cropped)

    #preparing canny edge detection on cropped image
    #first, making it a grey scale image
    grey_image = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    #defining threshold by looking at the histogram of the pixels
    plt.hist(grey_image.flatten(), 256, [0,256])
    plt.show()

    #blurring the image to prepare it for edge detection
    blurred = cv2.GaussianBlur(grey_image, (5,5), 0)

    #applying threshold (120) by setting all values above it to white and then inverting it
    (T_value, thresh_inverted) = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)
    #showing picture for sanity check
    jimshow_channel(thresh_inverted)

    #applying canny edge detection by defining min and max values manually (after playing around with it)
    canny = cv2.Canny(thresh_inverted, 70, 150)

    #plotting canny edge detection image
    jimshow_channel(canny, "Canny edge detection")

    #finding contours for the letters on a copied image
    (contours, _) = cv2.findContours(canny.copy(),
                     cv2.RETR_EXTERNAL,
                     cv2.CHAIN_APPROX_SIMPLE)

    #drawing the contours on the cropped image
    contoured = cv2.drawContours(cropped.copy(),
                     contours, #previously defined list of contours
                     -1, #all contours
                     (0,255,0), #green contour color
                     2) #contour pixel width

    #printing the contoured image for sanity check
    jimshow(contoured)

    #saving canny image
    outfile = os.path.join("..", "output", "image_letters.jpg")
    cv2.imwrite(outfile, contoured)

#defining behaviour when called from command line
if __name__=="__main__":
        main()

