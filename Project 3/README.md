# Project 3 - Image search (class assignment 2)

## Assignment description
Project 3 is equivalent to class Assignment 2 in the Visual Analytics course 2021. The assignment was to create an ‘image search engine’ by choosing a ‘target image’ from the data and comparing it to all the other images in the dataset one-by-one based on their color histogram.

## Methods
To solve this task first I defined my target image. Then I split the image into color channels and created a histogram using the cv2.compareHist() function to compare the 3D color histogram of the target image to each of the other images in the corpus one-by-one. In particular, the Chi-square distance method was used for the comparison, which showed the distance between the target image and each of the other images. The results from this comparison were saved as a single .csv file in the output folder showing the filename for every image in the dataset (except for the target image) and the distance metric between each image and the target.

## Usage (reproducing results)
The linked GitHub repository contains:
image_search.py script that can be run from the command line
- a requirements.txt file listing the required Python libraries for being able to run the script
- a venv_venv.sh script for setting up a virtual environment for running the script (recommended) - NB: for MAC users
- utils folder with utility functions used in the script (written by Ross Deans Kristensen-McLachlan)
- output folder containing the output files (Already contains outputs from the test run, if run again with the same parameters, the files will be overwritten. The nn_confusion_matrix.txt contains the confusion matrix run with 1 epoch for time-saving reasons.)
### Data
Can be downloaded from here: https://www.robots.ox.ac.uk/~vgg/data/flowers/17/ by clicking on 'Dataset images'
- For Windows users the .zip folder needs to be manually unzipped to a folder named 'data' which should be placed inside the 'Project 3' folder
- For MAC users this code can be executed from the terminal for unzipping (I recommend doing this after step 2 below before running the script): 
-   (first create a folder called 'data' by `mkdir data`,
-    then change directory to that folder by `cd data`) 
-    now you can unzip the file by: `unzip '17flowers.zip'`

In order to run this script, open your terminal and:
1. Clone this repo with `git clone https://github.com/szbianka/visual-analytics-2021-exam-portfolio` 
2. Navigate to the appropriate directory (Project2) 
`cd visual-analytics-2021-exam-portfolio/Project2`
3. activate a virtual environment (recommended) by:
(NB: The only reason I did not include the already made virtual environment in this repository is because the file was too big on my Windows computer.)
On Windows:
- If you have not used virtual environments before, you might need to run the following command first `py -m pip install --user virtualenv`
- Make a folder for the virtual environment mkdir envs
- Navigate to the env folder by cd envs
- Create the virtual environment by virtualenvs venv
- Activate the environment by venv\Scripts\activate
- Navigate to the env folder by `cd env` 
- Activate the environment by `edge\Scripts\activate`
On MAC or Worker02:
`python3 -m venv edge` 
`source edge/bin/activate
4. Navigate back to the appropriate folder (Project1) by `cd ..`
5. Install the necessary libraries by `pip install -r requirements.txt`
6. Navigate to the appropriate folder (src) by `cd src`
7. Run the scripts one by one (as in after each other): 
- Windows: `python image_search.py`
- Mac: `python3 image_search.py`
NB: the script is interactive: type `python image_search.py --help`  or open and inspect the script for receiving guidelines on which arguments can be modified and how. Default values are set, so it is not necessary to change the arguments. An example on modifying output file name: python lr-mnist.py --image *name-of-your-choosing*

8. deactivate virtual environment by `deactivate`

## Discussion of results
As mentioned above, the aim of this script is to compare images to each other based on their color histogram. This means - as can be seen from the two images printed on the terminal - that it is not necessarily the flowers themselves that will be detected as similar to each other, instead it only informs us about how well two color histograms match with each other. As a concrete example, the same image with different lighting parameters can be classified as not-very-similar with this method. For classifying the flowers that are indeed identical or similar to each other, I recommend using machine-learning approaches.
