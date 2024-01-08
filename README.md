# weather_prediction

## Problem Statement:
Weather forecasting is an important science. Accurate forecasting can help to save lives and minimize property damage. It’s also crucial for agriculture, allowing farmers to track when it’s best to plant or helping them protect their crops. And it will only become more vital in the coming years.

## Data Description:
Using the Columns :
* precipitation
* temp_max
* temp_min
* wind
* date
#### We are going to predict the weather condition :
* drizzle
* rain
* sun
* snow
* fog

#### dataset link: https://www.kaggle.com/datasets/ananthr1/weather-prediction/data

## Data Preprocessing:
Before we could start building the model, we had to preprocess the data. This involved checking for missing values, removing any unnecessary features, and normalizing the data. We used pandas libraries to perform these tasks.

## Exploratory Data Analysis:
Next, we performed some exploratory data analysis to gain insights into the relationships between the different features and the target variable, i.e., Weather. We used the matplotlib and Seaborn libraries to visualize the data and understand any patterns or correlations in the dataset. We also computed some summary statistics to understand the central tendency and variability of the data.

## Model Building:
we started building the machine learning models. We trained and test various Machine Learning Models, logistic Regression, naive bayes classifier, Random Forest Classifier and Support vector Classification.
random forest classifer has highest Accuracy rate which is 84.35972629521017 %
,so We choose to use a random forest classifer Machine Learning model to Predict the Weathers.

### I Combined all the machine learning Algorithms to make prediction better using ensemble technique
 #### Combine the models using majority voting and Accuracy is :  84.35972629521017 %
 #### Create a stacking ensemble and Accuracy is : 75.43 %
 #### Create a bagging ensemble and Accuracy is : 96.30 %

## Application Development
1. Built a conda Environment
2. Building and hosting a Flask web app on Azure Cloud Plateform.
3. Build the web app using Flask API
4. Install the necessary dependencies and libraries
5. Get the customer information from Web app
6. Display the prediction
7. Upload the project on GitHub
8. Create a project image using Docker hub as Containerize the app
9. Deploy the project on Azure Cloud Plateform.

## Initialize the Git Repositry
     git init
     git add .
     git commit -m "first commit"
     git branch -M main
     git remote add origin <github_url>
     git push -u origin main

 ### To update the modification or modification on github repositry
      git add .
      git commit -m "proper message"
      git push -u origin main

## Create a file "Dockerfile" with below content
     FROM python:3.9
     COPY . /app
     WORKDIR /app
     RUN pip install -r requirements.txt
     ENTRYPOINT [ "python" ]
     CMD [ "app.py" ]


## To Build the Docker Image on DockerHub
docker build -t "docker_profile_name/app_name": latest .

## To run the container Image
  docker container run -d -p "port number:EX-5000" "docker_profile_name/app_name": latest

## To Upload the Docker Image on DockerHub
  docker push "docker_profile_name/app_name": latest

## Create a "Procfile" with following content
web:gunicorn main:app
      