# Step 1 : Create and activate a new virtual environment

# Step 2 : Install django
+ pip install django

# Step 3 : Create a new Django project
+ django-admin startproject my_project .

# step 4 : Run project
+ python3 manage.py runserver

# step 5 : Create a new app
+ django-admin startapp my_app

# step 6 : Register app in the settings.py

# Step 7 : Update views folder
+ Using httpresponse

# Step 8 : create urls.py in the app

# Step 9 : Update the project url by registering app urls

# Step 10 : Create templates folder in the app folder

#### calling api

# Step 11 : API
+ pip install requests
+ create a request.py and import requests
+ create an .env file and add the api key
+ add the .env file to .gitignore
+ pip install python-decouple
+ Import the decouple module and use the config function to get the api key in the request.py
+ get the dictionary of the response
+ import your functions from request into your views
+ get the movies