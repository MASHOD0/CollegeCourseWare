# FirstYearProject
College courseware is a web application which helps streamline and modernise the
way classes are conducted in this pandemic , we have four core modules
● Registration
● Scheduling and course delivery
● Attendance
● Grading

## Registration
This module has three different parts to it
● Teacher Registration
● Student Registration
● Administration
Each part has its own way of creating users, storing the credentials and authenticating
their identity while login.

## Scheduling and course delivery
This module can be split into two
● Faculty end
● Student end
On the faculty end the profs. can schedule classes for a given day and they get notified
of their classes
On the student end students can access the classes assigned by the faculty

## Attendance
This module can also be split into two
● Faculty end
● student end
On the faculty end profs. can mark the attendance of a given class. And receive
insights from this in their newsletter
On the student end students can view their attendance .

## Grading
This module can also be split into two
● Faculty end
● student end
On the faculty end profs. can upload the marks of a particular class. And receive
insights from this in their newsletter
On the student end students can view their grades.

# Installation Guide 
## step 0: Clone This repository
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

