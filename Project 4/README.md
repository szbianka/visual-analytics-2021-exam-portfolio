# Project 4 (self-assigned)- Style transfer 

## Assignment description
This project was inspired by session11, where we used Tensorflow hub to create stylized images. That is, overlaying two pictures, so that it seems as one appears in the style of another.

## Methods
In order to perform style transfer on an image, first it needs to be prepared (e.g. resized), which was done with the help of the Tensorflow hub module. Then the picture we want to convert to a specific style should be defined along with the picture whose style we wish to transfer. Finally, all images - that is, the original image, we wish to transfer, the image, whose style we wish to transfer, and the newly stylized image are printed out into the command line.

## Usage (reproducing results)
The linked GitHub repository contains:
- style_transfer.py script that can be run from the command line
- a requirements.txt file listing the required Python libraries for being able to run the script
- a venv_venv.sh script for setting up a virtual environment for running the script (recommended) - NB: for MAC users
- utils folder with utility functions used in the script (written by Ross Deans Kristensen-McLachlan)
- data folder containing some images that can be used
In order to run this script, open your terminal and:
1. Clone this repo with `git clone https://github.com/szbianka/visual-analytics-2021-exam-portfolio` 
2. Navigate to the appropriate directory (Project2) 
`cd visual-analytics-2021-exam-portfolio/Project2`
3. activate a virtual environment (recommended) by:
(NB: The only reason I did not include the already made virtual environment in this repository is because the file was too big on my Windows computer.)
On Windows:
If you have not used virtual environments before, you might need to run the following command first `py -m pip install --user virtualenv`
Make a folder for the virtual environment `mkdir envs`
Navigate to the env folder by `cd envs`
Create the virtual environment by `virtualenvs venv`
Activate the environment by `venv\Scripts\activate`
Navigate to the env folder by `cd env` 
Activate the environment by `edge\Scripts\activate`
On MAC or Worker02:
`python3 -m venv edge` 
`source edge/bin/activate
4. Navigate back to the appropriate folder (Project1) by `cd ..`
5. Install the necessary libraries by `pip install -r requirements.txt`
6. Navigate to the appropriate folder (src) by `cd src`
7. Run the scripts one by one (as in after each other): 
Windows: `python image_search.py`
Mac: `python3 image_search.py`
NB: the script is interactive: type `python image_search.py --help`  or open and inspect the script for receiving guidelines on which arguments can be modified and how. Default values are set, so it is not necessary to change the arguments. An example on modifying output file name: python style_transfer.py --image *name-of-your-choosing*
8. deactivate virtual environment by `deactivate`


## Discussion of results
This project was made with the mere purpose of showing that producing scripts should not always be very serious and AI-like and therefore can be used by people whose interests lie in more humanistic/artistic domains. It is to show that even with rather basic computational skills, we can make almost any picture found on the internet or taken by us appear in a style of a famous painter or artificial style. Of course, not all images will align perfectly with each other, and some can look somewhat strange, but others will appear quite artistic. In conclusion, this project was made to have fun experiments with.
