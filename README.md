# Pixie ML POC Test - Tutorial

## Pre-requisites

In order to run the examples in this pack, the pre requisites are listed below:

#### 1) Install Python
Install Python 3.7, preferably [Anaconda](https://www.anaconda.com/distribution/) distribution. Installation tutorial [here](https://docs.anaconda.com/anaconda/install/).

To verify if Anaconda was successfully installed, try to open an [Anaconda Prompt](https://docs.anaconda.com/anaconda/install/verify-install/#conda). On Anaconda Prompt, type:

<code>python --version</code>

to verify Python's version installed and:

<code>conda --version</code>

to verify Conda version. If no errors displayed, the installation was successfull.

#### 2) Install pip
Pip is a famous package installer/manager for Python. Anaconda usually installs pip by default, but if you want to verify its installation by yourself, open an Anaconda Prompt and run the command:

<code>pip --version</code>

Pip version and directory location should be correctly displayed. Otherwise, if any error occurs, to install pip using conda:

<code>conda install -U pip</code>

#### 3) Download the project 

Download the compressed project folder named "Pixie_AI_POC_examples.7z", then extract it to a directory.

#### 4) Install Specific dependencies

To install specific dependencies required for the project:

1. Open an Anaconda Prompt.

2. Change directory to the previously extracted folder "Pixie_AI_POC_examples".

3. 3.	Run the following line of code to install all packages listed on "requirements.txt", and wait for the success message:

    <code>pip install -r requirements.txt</code>

## Command Line Script

The command line script demo provides a straightforward application of the ML solution developed during POC phase. It provides a Python script that receives an input ".jpg" image, apply the designed ML solution, then save the resulting image into a given directory and file. This resulting image contains a bounding box around the detected baby and its classification: (lying on) back or stomach.

To run it:

1. Open an Anaconda Prompt.

2. Change directory to the previously extracted folder "Pixie_AI_POC_examples".

3. Run the following line of code, passing the path to any image as the following:

    <code>python run_position_detection.py --in TEST_IMAGES/test_1.jpg</code>

    or

    <code>python run_position_detection.py -i TEST_IMAGES/test_1.jpg</code>

    where input argument is a path to any image in a local directory. This command will generate the respective image resulted with name "output.jpg" on the same directory.

    To choose an output directory and/or filename:

    <code>python run_position_detection.py --in test_image.jpg --out C:\path\to\output_img.jpg</code>

    As an example of choosing output image path and name:
    
    <code>python run_position_detection.py -–in TEST_IMAGES/test_2.jpg --out TEST_RESULTS/result_2.jpg</code>

For any help regarding "run_position_detection.py", run:

<code>python run_position_detection.py --help</code>

## Standalone Flask Server

This section contains a tutorial on running a simple Flask application that simulates the baby detection/classification workflow designed for the POC. The Flask application simulates an API, which receives the link to an internet ".jpg" image, and return a JSON structure containing the evaluation made by the ML model: coordinates for the baby bounding box, the classification label ("back" or "stomach") and its score. Note that the application does not suit for running on production environment, only for test/simulation purposes.

To run it:

1. Open an Anaconda Prompt.

2. Change directory to the previously extracted folder "Pixie_AI_POC_examples".

3. Run the following code to start the Flask app (do not close the prompt):

    <code>python flask_sample_yolo.py</code>

4. Open a web browser and navigate to: http://127.0.0.1:5000/ . The message "Is this baby sleeping safely?" shall be displayed.

5. For testing with an internet image, use the link: http://127.0.0.1:5000/api/v1/is_baby_safe_yolo?baby_url= \<Link to image here\>.

    For example: http://127.0.0.1:5000/api/v1/is_baby_safe_yolo?baby_url=https://www.todaysparent.com/wp-content/uploads/2017/01/tips-for-getting-baby-to-sleep-in-crib-during-naptime.jpg 

6. The response to this request, should be a JSON: 

        [
            {
                "box": [118, 74, 903, 1018], 
                "predicted_class": "back", 
                "score": 0.9945157766342163
            }
        ]