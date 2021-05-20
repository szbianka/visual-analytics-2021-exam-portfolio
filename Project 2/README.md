# Project 2 - Classification benchmarks (class assignment 4)

## Assignment description
Project 2 is equivalent to class Assignment 4 in the Visual Analytics course 2021. The assignment was to create two command-line tools which can be used to perform a simple classification task on the MNIST data and print the output to the terminal. The two scripts can be used to provide easy-to-understand benchmark scores for evaluating these models.

## Methods
In order to inspect the performance of two different models, two separate Python scripts were created. The first one takes the full MNIST data set, trains a Logistic Regression Classifier, and prints the evaluation metrics to the terminal, as well as saves the confusion matrix to the output folder as a .txt file. The other script similarly takes the full MNIST dataset, but then trains a neural network classifier, and prints the evaluation metrics to the terminal, as well as saves the confusion matrix in a similar manner. 

## Usage (reproducing results)
The linked GitHub repository contains:
- lr-mnist.py Logistic Regression Classifier script that can be run from the command line
- nn-mnist.py Neural Network Classifier script that can be run from the command line
- a requirements.txt file listing the required Python libraries for being able to run the script
- a venv_venv.sh script for setting up a virtual environment for running the script (recommended) - NB: for MAC users
- an env folder for setting up a virtual environment for running the script (recommended) -NB: for Windows users
- utils folder with utility functions used in the script (written by Ross Deans Kristensen-McLachlan)
- output folder containing the output files (Already contains outputs from the test run, if run again with the same parameters, the files will be overwritten. The nn_confusion_matrix.txt contains the confusion matrix run with 1 epoch for time-saving reasons.)

In order to run this script, open your terminal and:
1. Clone this repo with `git clone https://github.com/szbianka/visual-analytics-2021-exam-portfolio` 
2. Navigate to the appropriate directory (Project2) 
`cd visual-analytics-2021-exam-portfolio/Project2`
3. activate a virtual environment (recommended) by:
(NB: The only reason I did not include the already made virtual environment in this repository is because the file was too big on my Windows computer.)
On Windows:
If you have not used virtual environments before, you might need to run the following command first `py -m pip install --user virtualenv`
Make a folder for the virtual environment mkdir envs
Navigate to the env folder by cd envs
Create the virtual environment by virtualenvs venv
Activate the environment by venv\Scripts\activate
Navigate to the env folder by `cd env` 
Activate the environment by `edge\Scripts\activate`
On MAC or Worker02:
`python3 -m venv edge` 
`source edge/bin/activate
4. Navigate back to the appropriate folder (Project1) by `cd ..`
5. Install the necessary libraries by `pip install -r requirements.txt`
6. Navigate to the appropriate folder (src) by `cd src`
7. Run the scripts one by one (as in after each other): 
Windows: 

1. `python lr-mnist.py`

2. `python nn-mnist.py`

Mac:

1. `python3  lr-mnist.py`

2.`python3  nn-mnist.py`

NB: the scripts are interactive: type `python lr-mnist.py --help`  or open and inspect the scripts for receiving guidelines on which arguments can be modified and how. Default values are set, so it is not necessary to change the arguments. An example on modifying output file name: python lr-mnist.py --outfile *name-of-your-choosing*

8. deactivate virtual environment by `deactivate`

## Discussion of results
When classifying the hand-written digits in the dataset, the Logistic Regression classifier achieved a weighted average accuracy of 92%. The Neural Network classifier also achieved a weighted average accuracy of 92% with only one epoch, however after 4 epochs it approaches a 96% of weighted average accuracy. While this result is a slight improvement from the Logistic Regression classifier, it also takes a significantly longer time to run (a few seconds vs. hours) and therefore is computationally more expensive. Therefore, I would argue that in this case the improvement in performance is not worth the time spent on running the script.
