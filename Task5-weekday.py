# A program that outputs whether or not day is a weekday
# Author : Michelle O'Connor

# https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html

import datetime

# define weekday

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html

# use if statement to define outcome

today = datetime.datetime.today().strftime("%A")
if today in weekday:
    print ("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")

