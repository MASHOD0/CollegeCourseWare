# FirstYearProject
# Installation Guide 
## Step 1: Postrges
Install postgres from [here](https://www.postgresql.org/download/)
## Step 2: Create A database
Create a database with the name `fyp-ver1` with this [schema](src/sql/schema.sql) \
Note: if you create a database with another name, change the name of the database [here](src/DB/db.py)\
while you are at it check the username and password also. 

## Step 3: Install all the dependencies 
For this run this command in your terminal
```
pip install -r src/requirements.txt
```
for windows 
```
pip3 install -r src/requirements.txt
```
for mac and linux
## Step 4: Run the `main.py` file to start the application 
This will start running your application on [localhost:5000](http://localhost:5000/)

