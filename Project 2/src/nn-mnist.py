#!/usr/bin/env python
# coding: utf-8

#importing libraries
import sys,os
sys.path.append(os.path.join(".."))
import argparse
import numpy as np

from utils.neuralnetwork import NeuralNetwork
from sklearn import metrics
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets


#defining main() function
def main():
    #argument parser
    ap = argparse.ArgumentParser()
    
    #command line arguments to define
    #define filename
    ap.add_argument("-o", 
                    "--outfile", 
                    required=False, 
                    type= str, 
                    default= "nn_confusion_matrix.txt", 
                    help="str, output filename , default is: nn_confusion_matrix.txt")
    #specifying a random-state value
    ap.add_argument("-rs",  
                "--random_state", 
                required=False,  
                type=int,
                default=9,
                help="int, random state value of the model, default is: 9")
    #specifying size of test set in the model
    ap.add_argument("-ts", 
                "--test_size", 
                required=False, 
                type=float,
                default=0.2, 
                help="float, percentage of test set (must be number between 0 and 1, so e.g. 20% should be defined as 0.2, default is: 0.2)")
    #specifying the epoch iterations
    ap.add_argument("-ep", "--epoch", 
                    required = False, 
                    default = 5, 
                    type = float, 
                    help = "define epoch iterations, default is: 10")
    #specifying hidden layers in NN
    ap.add_argument("-hl1", "--hidden_layer1", 
                    required = False, 
                    default = 400, 
                    type = float, 
                    help = "define hidden layer 1 of the neural network, default is: 400")
     
    ap.add_argument("-hl2", "--hidden_layer2", 
                    required = False, 
                    default = 120, 
                    type = float, 
                    help = "define hidden layer of the neural network, default is: 120")
    
    #parse arguments
    args = vars(ap.parse_args())
    
    #defining the variable names that can be defined in the command line
    out_file_name = args["outfile"]
    random_state = args["random_state"]
    test_size = args["test_size"]
    epochs = args["epoch"]
    hidden_layer1 = args["hidden_layer1"]
    hidden_layer2 = args["hidden_layer2"]
    
    #fetching data, where X is the dataset and y is labels of the data
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)


    #converting data into numpy arrays and data type float, bc otherwise the model won't converge later
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)


    #predefining classes
    classes = sorted(set(y))
    nclasses = len(classes)


    # MinMax regularization
    X = (X - X.min())/(X.max() - X.min())


    #splitting data into training and test dataset
    X_train, X_test, y_train, y_test = train_test_split(X, #our data
                                                        y, #labels
                                                        random_state=random_state, #makes it reproducible
                                                        test_size= test_size) #splits by 80-20% by default, defined in args


    #converting labels from integers to vectors
    y_train = LabelBinarizer().fit_transform(y_train)
    y_test = LabelBinarizer().fit_transform(y_test)


    #training network (from 784 nodes to 10)
    print("[INFO] training network...")
    nn = NeuralNetwork([X_train.shape[1], 400, 120, 10])
    print("[INFO] {}".format(nn))
    nn.fit(X_train, y_train, epochs=epochs)


    #evaluating network
    print(["[INFO] evaluating network..."])
    predictions = nn.predict(X_test)
    predictions = predictions.argmax(axis=1)
    print(classification_report(y_test.argmax(axis=1), predictions))
    
    #saving the output as a txt file
    outpath = os.path.join("..", "output", out_file_name)
    file = open(outpath, "w")
    file.write(classification_report(y_test.argmax(axis=1), predictions))
    file.close()

#defining behaviour when called from command line
if __name__=="__main__":
    main()
