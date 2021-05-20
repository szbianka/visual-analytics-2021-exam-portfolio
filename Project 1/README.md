# Edge detection
## Assignment description
Project 1 is equivalent to class Assignment 3 in the Visual Analytics course 2021.
The purpose of the assignment was to use computer vision to extract specific features from images. In particular, to find language-like objects, such as letters and punctuation.

## Methods
The task relates to recognizing specific features like text in images using computer vision. In order to solve this task, first, a green rectangular box was drawn outlining the main body of the text and the image was saved as image_with_ROI.jpg In the output folder. The area inside the green rectangle was defined as the region of interest (ROI). Then the image was cropped, so that only the ROI is shown. The cropped image was saved as image_cropped.jpg in the same folder. Lastly, in order to perform Canny edge detection on the image, some preprocessing steps needed to be made, such as grey-scaling the cropped image, defining a threshold and blurring the image with Gaussian blur to reduce noise. The threshold is applied in order to gain a black and while only picture, as it is more suitable for detecting edges. After applying the threshold, the colors were inverted. Finally, with Canny edge detection, the contours of the letters were found, which due to the preprocessing steps are almost equivalent to the edges of the letters.

## Usage (reproducing results)
The linked GitHub repository contains:
- edge_detection.py script that can be run from the command line
- a requirements.txt file listing the required Python libraries for being able to run the script
- a edge_venv.sh script for setting up a virtual environment for running the script (recommended) - NB: for MAC users
- a data folder, which contains the data used for this project
- utils folder with utility functions used in the script (written by Ross Deans Kristensen-McLachlan)
- output folder containing the output files
In order to run this script, open your terminal and:
1. Clone this repo with `git clone https://github.com/szbianka/visual-analytics-2021-exam-portfolio` 
2. Navigate to the appropriate directory (Project1) 
`cd visual-analytics-2021-exam-portfolio/Project1`
3. activate a virtual environment (recommended) by:
(NB: The only reason I did not include the already made virtual environment in this repository is because the file was too big on my Windows computer.)
On Windows:
- If you have not used virtual environments before, you might need to run the following command first `py -m pip install --user virtualenv`
- Make a folder for the virtual environment `mkdir envs`
- Navigate to the env folder by `cd envs`
- Create the virtual environment by `virtualenvs venv`
- Activate the environment by `venv\Scripts\activate`
On MAC or worker02:
`python3 -m venv edge` 
`source edge/bin/activate
4. Navigate back to the appropriate folder (Project1) by `cd ..`
5. Install the necessary libraries by `pip install -r requirements.txt`
6. Navigate to the appropriate folder (src) by `cd src`
7. Run the script by: 
Windows: `python edge_detection.py`
Mac:`python3 edge_detection.py`
8. deactivate virtual environment by `deactivate`

## Discussion of results
The above applied approach is just one of many possibilities and is not necessarily the model that best captures all the edges with the fewest artifacts. It simply serves as a visualization of the complexity of detecting edges for a computer. 
In the final output image there are apparently some remaining artifacts from detecting the edges of the stones, as well as not all letters were captured perfectly (e.g. the letters ‘O’ and ‘D’). When applying thresholds there often occurs trade-offs like this. The goal should always be to best keep a balance between the desired outcome and the remaining noise.
