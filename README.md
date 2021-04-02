# **2021 Programming and Scripting module** 

# Michelle O'Connor

## This readme file details the weekly tasks of the 2021 Programming and Scripting module  
  

**_Weekly Task number 1:_**
_ _ _ 

The first task was an introduction into programming, scripting and GitHub. 

The actions were as follows:
1. Install the required software on my laptop
    - Outcome : Installed Cmder, Notepadd ++, Anaconda (Python) and VScode
2. Pull the sample code in Andrew's repository to my machine
    - Outcome : Cloned andreawbeattycourse/pands2021 onto my machine
3. Create a GitHub account and repository
    - Outcome : 'myWork' repository created in my GitHub account
4. Commit and push a file to new repository 
    - Outcome : 'hello.py' file pushed to 'myWork' repository  
      

**_Weekly Task number 2:_**
_ _ _ 

For the Statements topic in week 2, the task was to write a program that calculates somebody's Body Mass Index (BMI). 
* The inputs are the person's weight in kilograms and height in centimetres  
    Weight : 65  
    Height : 180

* The output is their weight divided by their height in metres squared.  
    BMI : 20.06


Code: 

    Weight = int(input("Enter your weight in kg : "))  
    Height = int(input("Enter your height in cm : "))  
    HeightinM2 = (Height/100 * Height/100)  
    BMI = round((Weight / HeightinM2),2)  
    print ('Your BMI is {}' .format(BMI))

Code Explanation:  
While asking the user for their inputs, I defined my inputs with the prefix of 'int' to ensure the number is a whole number.  
The formula for BMI is weight in kilograms divided by height in meters squared. With the height input measured in centimeters, I needed to divide by 100 to convert this to meters.  
The output requirement was to be in 2 decimal places so used the round(x,2) to achieve this.  



References:  
1. BMI formula using centimetres 
  https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/childrens_bmi_formula.html  

2. To round the result to 2 decimal places I referenced w3schools  
https://www.w3schools.com/python/ref_func_round.asp   
  
   
**_Weekly Task number 3:_**
_ _ _ 

For the Variables topic in week 3, the task was to write a program that asks a user to input a string and outputs every second letter in reverse order.
* String input is "The quick brown fox jumps over the lazy dog"
* Output to be .o zletrv pu o wr cu h  

Code: 

    words = str(input("Please enter a sentence : "))
    print (words [::-1][::2])

Code Explanation:  
Defined the input with the prefix of 'str' to ensure string format  
To reverse the order of the input used [::-1] as outlined on w3schools.  
In order to get every 2nd letter use [::2] as outlined on stackoverflow and docs.python.org.  

References:
1. https://www.w3schools.com/python/python_howto_reverse_string.asp
2. https://stackoverflow.com/questions/33470227/how-do-i-reverse-the-letters-in-a-string-in-python   
    https://docs.python.org/2/whatsnew/2.3.html#extended-slices   


**_Weekly Task number 4:_**
_ _ _ 

For Controlling the flow topic in week 4, the task was to write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.  
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.  
The program was to end if the current value was one.  
* Input is prompting the user to enter a positive integar, in this task it is 10  
* Output to be 10, 5, 16, 8, 4, 2, 1 

Code:   

    number = int(input ("Please enter a positive integer: "))
    mylist = []
    while number != 1:
        if (number % 2) == 0:
            number = (number//2)
            mylist.append(number)
        else:
            number = int(3*number +1)
            mylist.append(number)       
    print (mylist)


Code Explanation:   

Defined the input with the prefix of 'int' to ensure the number is a whole number.  
Defined my list as a 'list' [ ] type.  

The basis of the program is a while statement. While statements are used when you don't know before starting the program how many iterations of the code are needed.    
The while statement allows a block of code to be executed over and over again as long as the while statement’s condition is True.  
Therfore where the output of the calculation is greater than 1 for each run of the code (while number != 1), we want the output to be added to the list (mylist.append(number)) and used as the input for the next run of the code.  

For even numbers (if (number % 2) == 0), we need to divide by 2.  
For all other numbers (use else), we multiply it by three and add one

References:  

        Automate the boring stuff with python - Flow control - while Loop Statements




**_Weekly Task number 5:_**
_ _ _ 

For the Data topic in week 5, the task was to write a program that outputs whether or not today is a weekday.  

No user input required.  

An example of running this program on a Thursday is as follows:  
    Yes, unfortunately today is a weekday.

An example of running it on a Saturday is as follows:  
    It is the weekend, yay!


Code:   

    import datetime
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    today = datetime.datetime.today().strftime("%A")  
    if today in weekday:
        print ("Yes, unfortunately today is a weekday.")
    else:
        print ("It is the weekend, yay!")  


Code Explanation:   

Date in Python is not a data type of its own.  
We must import a module name __datetime__ to work with dates as date objects.  
Entered a definition of weekeday. 

Entering datatime.datetime.today() returns a datetime object of today.  
To format the output of the date we use strftime Method.  
strftime is a method for formatting date objects into readable strings.  
It takes one parameter, format, to specify the format of the returned string, %A is full weekday name format, e.g. Wednesday   

    Automate the boring stuff with python - The datatime Module

    Automate the boring stuff with python - Converting datetime Objects into Strings  


References:
1. https://www.w3schools.com/python/python_datetime.asp
2. https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html
3. Automate the boring stuff with python - Converting datetime Objects into Strings  
4. Automate the boring stuff with python - The datatime Module

