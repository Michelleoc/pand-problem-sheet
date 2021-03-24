## This readme file details the weekly tasks of the 2021 Programming and Scripting module

**_Weekly Task number 1:_**
_ _ _ 

This was our for first task and introduction into programming, scripting and GitHub. 

The actions were as follows:
1. I had to install the required software on my laptop
    - Outcome : Installed Cmder, Notepadd ++, Anaconda (Python) and VScode installed
2. Pull the sample code in Andrew's repository to my machine
    - Outcome : Cloned andreawbeattycourse/pands2021 onto my machine
3. Create a GitHub account and repository
    - Outcome : 'myWork' repository created in my GitHub account
4. Commit and push a file to new repository 
    - Outcome : 'hello.py' file pushed to 'myWork' repository


**_Weekly Task number 2:_**
_ _ _ 

For the Statements topic in week 2, I had to write a program that calculates somebody's Body Mass Index (BMI). 
* The inputs are the person's height in centimetres and weight in kilograms.
* The output is their weight divided by their height in metres squared.

I defined my inputs with the prefix of 'int' to ensure the number is a whole number.
 
I referenced the below link for a BMI formula using centimetres in the calculation.  
BMI formula link: https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/childrens_bmi_formula.html  
The formula for BMI is weight in kilograms divided by height in meters squared.  
If height has been measured in centimeters, divide by 100 to convert this to meters

To round the result to 2 decimal places I referenced w3schools  
https://www.w3schools.com/python/ref_func_round.asp

**_Weekly Task number 3:_**
_ _ _ 

For the Variables topic in week 3, I had to write a program that asks a user to input a string and outputs every second letter in reverse order.

String input is "The quick brown fox jumps over the lazy dog"

Defined the input with the prefix of 'str' to ensure string format  
    words = str(input("Please enter a sentence : "))

To reverse the order of the input use [::-1]

    https://www.w3schools.com/python/python_howto_reverse_string.asp

To get every 2nd letter use [::2]

Researching on the stackoverflow, there was a link about extended slices on docs.python page where it showed how to get every 2nd letter of input   

    https://stackoverflow.com/questions/33470227/how-do-i-reverse-the-letters-in-a-string-in-python   
    https://docs.python.org/2/whatsnew/2.3.html#extended-slices   


**_Weekly Task number 5:_**
_ _ _ 

For the Data topic in week 5, I had to write a program that outputs whether or not today is a weekday.
We had to search the web to find how you work out what day it is
An example of running this program on a Thursday is as follows:  
    Yes, unfortunately today is a weekday.

An example of running it on a Saturday is as follows:  
    It is the weekend, yay!

Date in Python is not a data type of its own. We must import a module name __datetime__ to work with dates as date objects
    https://www.w3schools.com/python/python_datetime.asp
    https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html

Calling datatime.datetime.today() returns a datetime object of today
    Automate the boring stuff with python - The datatime Module

To format the output of the date we use strftime Method  
strftime is a method for formatting date objects into readable strings  
It takes one parameter, format, to specify the format of the returned string  
%A is full weekday name format, e.g. Wednesday  
    Automate the boring stuff with python - Converting datetime Objects into Strings  



