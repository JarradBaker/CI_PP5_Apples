# **Apple Detector**

* [Live website](https://apple-detector-74c5c198fe4b.herokuapp.com/)



![Apple Image](assets/apple-readme.png)

## Table of Contents
  - [Summary](#summary)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
    - [Business Requirement 1 - Patterns in Dataset](#business-requirement-1---patterns-in-dataset)
    - [Business Requirement 2 - Prediction of Apple or Orange](#business-requirement-2---prediction-of-apple-or-orange)
  - [Project Hypothesis](#project-hypothesis)
  - [Map of Business Requirements to Data Analytics Tasks](#map-of-business-requirements-to-data-analytics-tasks)
    - [Business Requirement 1](#business-requirement-1)
    - [Business Requirement 2](#business-requirement-2)
  - [ML Business Case](#ml-business-case)
    - [Predict Apple](#predict-apple)
    - [Predict Orange](#predict-orange)
  - [Dashboard Design](#dashboard-design)
    - [Page 1: Quick Project Summary](#page-1)
    - [Page 2: ](#page-2)
    - [Page 3: ](#page-3)
    - [Page 4: ](#page-4)
    - [Page 5: ML: Predict Apple](#page-5)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
  - [Data Analysis and Machine Learning Libraries](#data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)

<hr> 

## Summary

<a href="https://apple-detector-74c5c198fe4b.herokuapp.com/">Apple Detector</a> is a dashboard application that allows a juicing company to detect whether the harvested fruit is an apple, or an orange, ready for production. The project was agreed to achieve the following objectives for the company:

- gives the company visual insight into what differentiates apples from oranges.
- allows the company to separate apples from oranges, ready for juicing and production.

[Back to top](#table-of-contents)
<hr>

## Dataset Content
<img src="assets/apple-diagram.jpg" height=300px float=left/> 

The dataset was sourced from the <a href="https://www.kaggle.com/datasets/varadmurtymohod/apple-vs-orange-image-classification" target="_blank" rel="noreferrer">Apple VS Orange Classification dataset</a> on <a href="https://www.kaggle.com" target="_blank" rel="noreferrer">kaggle</a>. 


[Back to top](#table-of-contents)
<hr>

## Business Requirements

The client for this project is a juicing company that grow both apples and oranges. All fruit gets collected from the same orchard, but they have problems differentiating between the apples and oranges on mass. They would like a solution to determine whether the selected fruit is an apple or orange, and it will then be passed to the relevant juicers.


### Business Requirement 1 - Patterns in Dataset
- The client would like a visual insight into what separates apples from oranges. Things like colour would initially help to do a primary sorting of the two fruits.

### Business Requirement 2 - Prediction of Apple or Orange
- The client would like to determine whether a given fruit is an apple or an orange. This would be much cheaper having a soultion to do the predicting for them, and much less error prone.

[Back to top](#table-of-contents)
<hr>

## Project Hypothesis

- Apples and Oranges collecting in vast majorities are extremely mundane and tedious to separate by eye. This leads to many human errors when performing this process. I set out to build a solution that detects whether the given fruit is an apple or an orange, so it could be much faster, and less error prone than humans.

<hr>

## Map of Business Requirements to Data Analytics Tasks

- ### Business Requirement 1
  - **Data visualization and correlation study**
  - We will inspect the data of the apples and oranges.
  - We will plot the main variables that correlate to visual insights.

- ### Business Requirement 2
  - **Classification analysis**
  - We want to predict if a given fruit is an apple or orange. We will build a binary classifier.

[Back to top](#table-of-contents)
<hr>

## ML Business Case

### **Predict Apple**

#### Classification Model

- We want an ML model to predict if a fruit is an apple or orange based on historical data provided of apples and oranges by the company. It is a supervised, double-labelled classification model with outputs of 0 (apple) or 1 (orange).

[Back to top](#table-of-contents)
<hr>

## Dashboard Design

### Page 1: Quick Project Summary

- Quick summary of the project
  - Project terminology
  - Description of the dataset


### Page 2: Apple Visualizer

- Visualizes the data


### Page 3: Apple Detector

- Runs the actual prediction for an apple or orange.


### Page 4: Project Hypotheses and Validation

- Shows the  Image montage
  

### Page 5: ML: Predict Edible

- Shows the graphs and ML model


[Back to top](#table-of-contents)
<hr>

## Unfixed Bugs

- There are no known unfixed bugs in the project.

[Back to top](#table-of-contents)
<hr>

## Deployment

### Heroku

- The App live link is: https://apple-detector-74c5c198fe4b.herokuapp.com/
- The project was deployed to Heroku from Github using the following steps.

1. Go to Heroku and Sign in
2. Create a new app
3. Select location and app name
4. select deploy from github, and search for your repo
5. Select the main branch, and select deploy

You will need to ensure the following:
1. Ensured a Procfile with the line `web: sh setup.sh && streamlit run app.py` is in the main directory of the repo
2. Ensured all libraries used in the streamlit app page scripts are included in requirements.txt in the main directory of the repo


7. On command prompt, ran `heroku login`, prompting the browser popup to authorize logging into the CLI

8. In the CLI, ran `heroku stack:set heroku-20 -a mushroom-safety` to set the stack to heroku-20.



<hr>

### Fork Repository 
To fork the repository, perform the following steps:

1. Go to the [GitHub repository](https://github.com/JarradBaker/CI_PP5_Apples)
2. Click the fork button in the upper right hand corner

<hr>

### Clone Repository
To clone the repository, perform the following steps:

1. Go to the [GitHub repository](https://github.com/JarradBaker/CI_PP5_Apples)
2. Locate the Code button on the upper right hand corner
3. Select preference of cloning using HTTPS, SSH, or Github CLI, then click the copy button to copy the URL to the clipboard
4. Open Git bash
5. Change the working directory to where you wish to clone the repo to
6. Type `git clone` followed by pasting the URL from your clipboard
7. Hit enter to run the command and create the local clone

[Back to top](#table-of-contents)
<hr>

## Data Analysis and Machine Learning Libraries

- The libraries used in this project:

	- `numpy` - for general usage on array-based data structures
	- `pandas` - for creating DataFrames to store the dataset in and operating various data cleaning, feature engineering, modelling and model assessment tasks
	- `matplotlib` - for plotting data to visualize insights
	- `seaborn` - for plotting data to visualize insights
	- `ydata-profiling` - for using the `ProfileReport` class to assess the datasets composition
	- `plotly` - for plotting parallel plots of mushrooms variables with respect to edibility
	- `ppscore` - for generating correlation coefficients of different variables in the dataset to the target
	- `streamlit` - for implementing the dashboard application
	- `feature-engine` - for various feature engineering tasks
	- `imbalanced-learn` - for performing SMOTE on the training data to ensure a balanced proportion of targets
	- `scikit-learn` - for implementing ML models
	- `xgboost` - for implementing ML models
	- `yellowbrick` - for assessing clustering model performance by visualizing silhouette scores
	- `category_encoders` - for using the `TargetEncoder` class to perform target encoding on the dataset

[Back to top](#table-of-contents)
<hr>

## Credits

### Content

- This project heavily relied on the Kaggle dataset mentioned above: Apples Vs Oranges


### Media

- The images from the dataset

[Back to top](#table-of-contents)

<hr>

## Acknowledgements

I would like to thank my partner for her continued support and encouragement. 

[Back to top](#table-of-contents)
