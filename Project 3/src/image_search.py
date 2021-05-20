#!/usr/bin/env python
# coding: utf-8

#system stuff
import os
import sys
sys.path.append(os.path.join(".."))
from pathlib import Path
import pandas as pd
import csv
import glob
import argparse

import cv2
import numpy as np

from utils.imutils import jimshow
import matplotlib.pyplot as plt

#defining main() function
def main():
    #argument parser
    ap = argparse.ArgumentParser()
    #command line arguments to define
    #defining image to work with
    ap.add_argument("-i",  
                "--image", 
                required=False,  
                type=str,
                default= "image_0245.jpg",
                help="str, name of the image of your choosing, default is: image_0245.jpg")

    #defining data path
    data_path = os.path.join("..", "data", "jpg")
    
    #parse arguments
    args = vars(ap.parse_args())
    
    #defining the variable name that can be defined in the command line
    image_of_choice = args["image"]
    
    #unzipping the zip file on mac
    #os.chdir(os.path.join("..", "data"))
    #!unzip '17flowers.zip'

    #defining image I want to work with
    main_image = cv2.imread(os.path.join("..", "data", "jpg", image_of_choice))

    #showing image
    jimshow(main_image, "Flower of your choice")

    #creating empty list for distance
    distance= []

    #creating a for loop for comparing each image in the list to the main image
    for image in Path(data_path).glob("*.jpg"):
        #cv2 and pathlib don't play nicely together so
        image_path = str(image)
        #read image 
        image = cv2.imread(image_path)
        #get image_name from image_path
        filename = _, image_name = os.path.split(image_path) #_ is a dummy variable
        #split channels
        channels = cv2.split(image)
        #create histogram
        hist= cv2.calcHist([image], [0,1,2], None, [8,8,8], [0, 256, 0, 256, 0, 256])
        #defining main image histogram
        hist1 = cv2.calcHist([main_image], [0,1,2], None, [8,8,8], [0, 256, 0, 256, 0, 256])
        #then compare them one by one using chi-square distance method, rounding to 2 decimal places
        chi_sq = round(cv2.compareHist(hist, hist1, cv2.HISTCMP_CHISQR), 2)

        #appending the empty distance list with the chi-square values
        distance.append(chi_sq)

    #making a list of filenames
    filenames = [os.path.basename(image_name) for image_name in Path(data_path).glob("*.jpg")]

    #creating csv file with filenames and distance
    df = pd.DataFrame(data={"filename": filenames, "distance": distance})

    #creating new df without main image and its distance value, since I don't want to compare it to itself
    df = df[df.filename != image_of_choice]

    #saving df as .csv file in output folder
    outpath = os.path.join("..", "output", "image_distance.csv")
    df.to_csv(outpath, sep=',', index= False)

    #looking for lowest distance (most similar image)
    min_distance = df.min()["distance"]

    #locatinging the closest image name and assigning it to a df
    closest_filename_df = pd.DataFrame(df.loc[df["distance"] == min_distance])
    #extracting closest image name
    closest_image_name = closest_filename_df["filename"].values[0]
    
    #print the file name of the closest image with text
    print(f"Closest image is {closest_image_name} to the flower of your choice.")
    #showing the closest image
    closest_image = cv2.imread(os.path.join("..", "data", "jpg", closest_image_name))
    jimshow(closest_image, "Closest flower")

#defining behaviour when called from command line
if __name__=="__main__":
    main()