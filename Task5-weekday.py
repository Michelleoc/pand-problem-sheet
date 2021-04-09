# Topic 'Data' - Weekly Task 05
# A program that outputs whether or not day is a weekday
# Author : Michelle O'Connor


# Date in Python is not a data type of its own. We must import a module name datetime to work with dates as date objects

import datetime

# define weekday

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Calling datatime.datetime.today() returns a datetime object of today
# To format the output of the date we use strftime Method 
# strftime is a method for formatting date objects into readable strings.
# It takes one parameter, format, to specify the format of the returned string:
# %A is full weekday name format, e.g. Wednesday

today = datetime.datetime.today().strftime("%A")

# use if statement to define outcome. 
# Defined the outcome if true and then used else to show the result of the if condition when it is false

if today in weekday:
    print ("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")


# https://www.w3schools.com/python/python_datetime.asp
# https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html
# Automate the boring stuff with python - Converting datetime Objects into Strings  
# Automate the boring stuff with python - The datatime Module