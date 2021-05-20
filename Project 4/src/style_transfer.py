#!/usr/bin/env python
# coding: utf-8

#load libraries
import os, sys
sys.path.append(os.path.join(".."))

import numpy as np
from numpy.linalg import norm
from tqdm import tqdm

# tensorflow
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

# style utils 
from utils.styletransfer import *

# matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib inline

import argparse

#defining useful functions
def extract_features(img_path, model):
    """
    Extract features from image data using pretrained model (e.g. VGG16)
    """
    # Define input image shape - remember we need to reshape
    input_shape = (224, 224, 3)
    # load image from file path
    img = load_img(img_path, target_size=(input_shape[0], 
                                          input_shape[1]))
    # convert to array
    img_array = img_to_array(img)
    # expand to fit dimensions
    expanded_img_array = np.expand_dims(img_array, axis=0)
    # preprocess image - see last week's notebook
    preprocessed_img = preprocess_input(expanded_img_array)
    # use the predict function to create feature representation
    features = model.predict(preprocessed_img)
    # flatten
    flattened_features = features.flatten()
    # normalise features
    normalized_features = flattened_features / norm(features)
    return flattened_features

def get_file_list(root_dir):
    # define valid file extensions
    extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']
    # create empty file list
    file_list = []
    # initialise counter
    counter = 1
    # use os.walk to create a list of image filepaths
    for root, directories, filenames in os.walk(root_dir):
        for filename in filenames:
            # keep only those with valid extensions
            if any(ext in filename for ext in extensions):
                file_list.append(os.path.join(root, filename))
                # increment counter
                counter += 1
    return file_list

#defining main() function
def main():
    #argument parser
    ap = argparse.ArgumentParser()
    
    #command line arguments to define
    #specifying image of choice
    ap.add_argument("-i",  
                "--image", 
                required=False,  
                type=str,
                default= "ny.jpg",
                help="str, name of the image of your choosing, default is: ny.jpg")
    #specifying style image
    ap.add_argument("-st", 
                "--style", 
                required=False, 
                type=str,
                default="picasso.jpg", 
                help="str, name of the styling image of your choosing, default is: picasso.jpg")
    
    #defining data path
    path = os.path.join("..", "data")
                             
    #parse arguments
    args = vars(ap.parse_args())
    
    #defining the variable names that can be defined in the command line
    image_of_choice = args["image"]
    style_image = args["style"]
    
    #loading VGG16 model
    print(f"INFO: loading in VGG16 model...")
    model = VGG16(weights='imagenet', 
                      include_top=False, #we get rid of the fully connected network
                      pooling='avg', #average pooling
                      input_shape=(224, 224, 3))

    #extracting features from image of choice
    features = extract_features(image_of_choice, model)
    
    #preparing for style transfer
    #loading in the necessary Tensorflow-Hub module
    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)
    
    #loading in the content and the style image
    content_image = st_load(path, image_of_choice)
    style_image = st_load(path, style_image)
    #processing with the models
    outputs = hub_module(content_image, style_image)
    stylized_image = outputs[0]
    
    #print content, style and resulting stylized image
    show_n([content_image, style_image, stylized_image], 
           titles=['Original content image', 'Style image', 'Stylized image'])
    
#defining behaviour when called from command line
if __name__=="__main__":
    main()