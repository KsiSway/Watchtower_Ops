---
sourceFile: "Convert excel serial date to datetime - Python - GeeksforGeeks"
exportedBy: "Kortex"
exportDate: "2026-05-20T06:50:17.305Z"
---

# Convert excel serial date to datetime - Python - GeeksforGeeks

d5610d02-7a10-452b-87e0-4890e094e0f6

Convert excel serial date to datetime - Python - GeeksforGeeks

736c6481-2bd7-4468-8e1f-7ca8a60a4140

https://www.geeksforgeeks.org/python/python-convert-excel-serial-date-to-datetime/

Python - Convert excel serial date to datetime - GeeksforGeeks

https://www.geeksforgeeks.org/python/python-convert-excel-serial-date-to-datetime/

https://www.geeksforgeeks.org/python/python-convert-excel-serial-date-to-datetime/

Interview Prep

https://www.geeksforgeeks.org/python/python-convert-excel-serial-date-to-datetime/

Python Tutorial

https://www.geeksforgeeks.org/python/python-programming-language-tutorial/

https://www.geeksforgeeks.org/python/python-data-types/

Interview Questions

https://www.geeksforgeeks.org/python/python-interview-questions/

https://www.geeksforgeeks.org/python/python-programming-examples/

https://www.geeksforgeeks.org/python/python-quizzes/

https://www.geeksforgeeks.org/dsa/python-data-structures-and-algorithms/

Data Science

https://www.geeksforgeeks.org/data-science/data-science-with-python-tutorial/

https://www.geeksforgeeks.org/python/numpy-tutorial/

https://www.geeksforgeeks.org/pandas/pandas-tutorial/

https://www.geeksforgeeks.org/dsa/geeksforgeeks-practice-best-online-coding-platform/

Python - Convert excel serial date to datetime

Last Updated : 14 Sep, 2021

This article will discuss the conversion of an excel serial date to DateTime in Python.

The Excel "serial date" format is actually the number of days since 1900-01-00 i.e., January 1st, 1900. For example, the excel serial date number 43831 represents January 1st, 2020, and after converting 43831 to a DateTime becomes 2020-01-01.

By using \*\* xlrd.xldate\_as\_datetime()\*\* function this can be achieved. The

xlrd.xldate\_as\_datetime()

function is used to convert excel date/time number to datetime.datetime object.

xldate\_as\_datetime (xldate, datemode)

#### Parameters:

#### This function accepts two parameters that are illustrated below:

This is the specified excel date that will converted into datetime.

This is the specified datemode in which conversion will be performed.

#### Return values:

This function returns the datetime.datetime object.

First, call xlrd.xldate\_as\_datetime(date, 0) function to convert the specified Excel date to a datetime.datetime object. Then, call datetime.datetime.date() function on the returned datetime.datetime object to return the date as a datetime.date object. Lastly, call datetime.date.isoformat() function to convert the returned datetime.date object to a ISO format date string.

#### Let's see some examples to illustrate the above algorithm:

Python program to convert excel serial date to string date

Loading Playground... \`

# Python3 code to illustrate the conversion
# of excel serial date to datetime

# Importing xlrd module
import xlrd

# Initializing an excel serial date
xl\_date = 43831

# Calling the xldate\_as\_datetime() function to
# convert the specified excel serial date into
# datetime.datetime object
datetime\_date = xlrd.xldate\_as\_datetime(xl\_date, 0)

# Calling the datetime\_date.date() function to convert
# the above returned datetime.datetime object into
# datetime.date object
date\_object = datetime\_date.date()

# Calling the isoformat() function to convert the
# above returned datetime.date object into the
# ISO format date string
string\_date = date\_object.isoformat()

# Getting the converted date string as output
print(string\_date)

# Getting the type of returned date format
print(type(string\_date))

2020-01-01
<class 'str'>

Python program to convert excel serial number to DateTime

Loading Playground... \`

# Python3 code to illustrate the conversion
# of excel serial date to datetime

# Importing xlrd module
import xlrd

# Initializing an excel serial date
xl\_date = 43831

# Calling the xldate\_as\_datetime() function to
# convert the specified excel serial date into
# datetime.datetime object
datetime\_date = xlrd.xldate\_as\_datetime(xl\_date, 0)

# Calling the datetime\_date.date() function to convert
# the above returned datetime.datetime object into
# datetime.date object
date\_object = datetime\_date.date()

# Getting the converted date date as output
print(date\_object)

# Getting the type of returned date format
print(type(date\_object))

2020-01-01
<class 'datetime.date'>

https://www.geeksforgeeks.org/user/Kanchan\_Ray/

Kanchan\_Ray

https://www.geeksforgeeks.org/user/Kanchan\_Ray/

#### Article Tags:

#### Article Tags:

https://www.geeksforgeeks.org/category/programming-language/python/

Python-excel

https://www.geeksforgeeks.org/tag/python-excel/

Python-datetime

https://www.geeksforgeeks.org/tag/python-datetime/

Python Fundamentals

Introduction 1 min read

https://www.geeksforgeeks.org/python/introduction-to-python/

Input & Output 2 min read

https://www.geeksforgeeks.org/python/input-and-output-in-python/

Variables 4 min read

https://www.geeksforgeeks.org/python/python-variables/

Operators 4 min read

https://www.geeksforgeeks.org/python/python-operators/

Keywords 2 min read

https://www.geeksforgeeks.org/python/python-keywords/

Data Types 4 min read

https://www.geeksforgeeks.org/python/python-data-types/

Conditional Statements 3 min read

https://www.geeksforgeeks.org/python/conditional-statements-in-python/

Loops 3 min read

https://www.geeksforgeeks.org/python/loops-in-python/

Functions 4 min read

https://www.geeksforgeeks.org/python/python-functions/

Python Data Structures

String 4 min read

https://www.geeksforgeeks.org/python/python-string/

List 4 min read

https://www.geeksforgeeks.org/python/python-lists/

Tuples 3 min read

https://www.geeksforgeeks.org/python/python-tuples/

Dictionary 3 min read

https://www.geeksforgeeks.org/python/python-dictionary/

Set 5 min read

https://www.geeksforgeeks.org/python/python-sets/

Arrays 6 min read

https://www.geeksforgeeks.org/python/python-arrays/

Advanced Python

OOP Concepts 3 min read

https://www.geeksforgeeks.org/python/python-oops-concepts/

Exception Handling 5 min read

https://www.geeksforgeeks.org/python/python-exception-handling/

File Handling 4 min read

https://www.geeksforgeeks.org/python/file-handling-python/

Python Database 4 min read

https://www.geeksforgeeks.org/python/python-database-tutorial/

MongoDB 3 min read

https://www.geeksforgeeks.org/python/python-mongodb-tutorial/

MySQL 8 min read

https://www.geeksforgeeks.org/python/python-mysql/

Packages 4 min read

https://www.geeksforgeeks.org/python/python-packages/

Modules 3 min read

https://www.geeksforgeeks.org/python/python-modules/

DSA Libraries 5 min read

https://www.geeksforgeeks.org/python/python-dsa-libraries/

Python GUI 3 min read

https://www.geeksforgeeks.org/python/python3-gui-application-overview/

Data Science with Python

Numpy 3 min read

https://www.geeksforgeeks.org/python/numpy-tutorial/

Pandas 4 min read

https://www.geeksforgeeks.org/pandas/pandas-tutorial/

Matplotlib 3 min read

https://www.geeksforgeeks.org/python/matplotlib-tutorial/

Seaborn 3 min read

https://www.geeksforgeeks.org/python/python-seaborn-tutorial/

StatsModel 2 min read

https://www.geeksforgeeks.org/data-science/statsmodel-library-tutorial/

Model Building 6 min read

https://www.geeksforgeeks.org/machine-learning/learning-model-building-scikit-learn-python-machine-learning-library/

TensorFlow 2 min read

https://www.geeksforgeeks.org/deep-learning/tensorflow/

PyTorch 5 min read

https://www.geeksforgeeks.org/deep-learning/pytorch-tutorial-2/

Web Development with Python

Flask 3 min read

https://www.geeksforgeeks.org/python/flask-tutorial/

Django 5 min read

https://www.geeksforgeeks.org/python/django-tutorial/

Django ORM 4 min read

https://www.geeksforgeeks.org/python/django-orm-inserting-updating-deleting-data/

Jinja2 Templating 5 min read

https://www.geeksforgeeks.org/python/templating-with-jinja2-in-flask/

Django Templates 5 min read

https://www.geeksforgeeks.org/python/django-templates/

REST API 3 min read

https://www.geeksforgeeks.org/python/python-build-a-rest-api-using-flask/

Build API with DRF 4 min read

https://www.geeksforgeeks.org/python/how-to-create-a-basic-api-using-django-rest-framework/

Python Practice

Quiz 1 min read

https://www.geeksforgeeks.org/python/python-quizzes/

Practice Problems 1 min read

https://www.geeksforgeeks.org/python/python-coding-practice-problems/

Interview Q & A 15+ min read

https://www.geeksforgeeks.org/python/python-interview-questions/

Python Courses

Python Programming Course 2 min read

https://www.geeksforgeeks.org/courses/master-python-complete-beginner-to-advanced

Data Analytics Course with AI 2 min read

https://www.geeksforgeeks.org/courses/data-analytics-training-program-excel-sql-python-powerbi

Tech Interview 101 Course | DSA and System Design 2 min read

https://www.geeksforgeeks.org/courses/interviewe-101-data-structures-algorithm-system-design

#### Corporate & Communications Address:

A-143, 7th Floor, Sovereign Corporate Tower, Sector- 136, Noida, Uttar Pradesh (201305)

#### Registered Address:

K 061, Tower K, Gulshan Vivante Apartment, Sector 137, Noida, Gautam Buddh Nagar, Uttar Pradesh, 201305

https://in.linkedin.com/company/geeksforgeeks

https://www.instagram.com/geeks\_for\_geeks/

https://twitter.com/geeksforgeeks

https://www.facebook.com/geeksforgeeks.org/

https://www.youtube.com/geeksforgeeksvideos

https://www.geeksforgeeks.org/about/

https://www.geeksforgeeks.org/legal/

Privacy Policy

https://www.geeksforgeeks.org/legal/privacy-policy/

https://www.geeksforgeeks.org/about/contact-us/

Advertise with us

https://www.geeksforgeeks.org/advertise-with-us/

GFG Corporate Solution

https://www.geeksforgeeks.org/gfg-corporate-solution/

Campus Training Program

https://www.geeksforgeeks.org/campus-training-program/

https://www.geeksforgeeks.org/problem-of-the-day

https://practice.geeksforgeeks.org/events/rec/job-a-thon/

https://www.geeksforgeeks.org/category/blogs/?type=recent

Nation Skill Up

https://www.geeksforgeeks.org/nation-skill-up/

Programming Languages

https://www.geeksforgeeks.org/computer-science-fundamentals/programming-language-tutorials/

https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/

Web Technology

https://www.geeksforgeeks.org/web-tech/web-technology/

AI, ML & Data Science

https://www.geeksforgeeks.org/machine-learning/ai-ml-and-data-science-tutorial-learn-ai-ml-and-data-science/

https://www.geeksforgeeks.org/devops/devops-tutorial/

CS Core Subjects

https://www.geeksforgeeks.org/gate/gate-exam-tutorial/

Interview Preparation

https://www.geeksforgeeks.org/aptitude/interview-corner/

Software and Tools

https://www.geeksforgeeks.org/websites-apps/software-and-tools-a-to-z-list/

ML and Data Science

https://www.geeksforgeeks.org/courses/category/machine-learning-data-science

DSA and Placements

https://www.geeksforgeeks.org/courses/category/dsa-placements

Web Development

https://www.geeksforgeeks.org/courses/category/development-testing

Programming Languages

https://www.geeksforgeeks.org/courses/category/programming-languages

DevOps & Cloud

https://www.geeksforgeeks.org/courses/category/cloud-devops

https://www.geeksforgeeks.org/courses/category/gate

Trending Technologies

https://www.geeksforgeeks.org/courses/category/trending-technologies/

https://www.geeksforgeeks.org/videos/category/sde-sheet/

https://www.geeksforgeeks.org/videos/category/python/

https://www.geeksforgeeks.org/videos/category/java-w6y5f4/

https://www.geeksforgeeks.org/videos/category/c/

Web Development

https://www.geeksforgeeks.org/videos/category/web-development/

Data Science

https://www.geeksforgeeks.org/videos/category/data-science/

CS Subjects

https://www.geeksforgeeks.org/videos/category/cs-subjects/

Preparation Corner

Interview Corner

https://www.geeksforgeeks.org/interview-prep/interview-corner/

https://www.geeksforgeeks.org/aptitude/aptitude-questions-and-answers/

https://www.geeksforgeeks.org/aptitude/puzzles/

https://www.geeksforgeeks.org/courses/gfg-160-series

System Design

https://www.geeksforgeeks.org/system-design/system-design-tutorial/

@GeeksforGeeks, Sanchhaya Education Private Limited

https://www.geeksforgeeks.org/

All rights reserved

https://www.geeksforgeeks.org/copyright-information/

