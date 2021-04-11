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
    
    https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/childrens_bmi_formula.html  
    https://www.w3schools.com/python/ref_func_round.asp   
  
   
**_Weekly Task number 3:_**
_ _ _ 

For the Variables topic in week 3, the task was to write a program that asks a user to input a string and outputs every second letter in reverse order.
* String input is "The quick brown fox jumps over the lazy dog"
* Output to be .o zletrv pu o wr cu h  

Code: 

    words = str(input("Please enter a sentence : "))
    print(words [::-2])
    
Code Explanation:  
Defined the input with the prefix of 'str' to ensure string format  
To reverse the order of the input used [::-1] as outlined on w3schools.  
In order to get every 2nd letter use [::2] as outlined on stackoverflow and docs.python.org.  

Originally had "__print (words [::-1][::2])__" as the code, but it was highligthed to me this could have been done with one [ ], I tried multiple verisons to get the desired result of [::-2].    
[::-] reverses the input and [::2] takes every 2nd ouput so combining these 2 commands into [::-2] gives every second letter in reverse.

References:

    https://www.w3schools.com/python/python_howto_reverse_string.asp
    https://stackoverflow.com/questions/33470227/how-do-i-reverse-the-letters-in-a-string-in-python   
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

For even numbers (if (number % 2) == 0), we need to divide by 2 and add output to the list.  
For all other numbers (use else), we multiply it by three and add one and add output to the list.  

If the output is great than 1,the while statement will restart again.    


References:  

        Automate the boring stuff with python - Flow control - while Loop Statements
        https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
        https://www.geeksforgeeks.org/program-to-print-collatz-sequence/
        


**_Weekly Task number 5:_**
_ _ _ 

For the Data topic in week 5, the task was to write a program that outputs whether or not today is a weekday.  

* No user input required.  

* Output  
    An example of running this program on a Thursday is as follows:  
    - Yes, unfortunately today is a weekday. 
 
    An example of running it on a Saturday is as follows:  
    - It is the weekend, yay!


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

Entered a definition of weekday. 

Entering datatime.datetime.today() returns a datetime object of today.  
To format the output of the date we use strftime Method.  
strftime is a method for formatting date objects into readable strings.  
It takes one parameter, format, to specify the format of the returned string, %A is full weekday name format, e.g. Wednesday   

I used an if statement to define the outcome if true and then used an else condition to show the outcome of the if statement when it is false, i.e not a weekday.

References:

    https://www.w3schools.com/python/python_datetime.asp
    https://www.pythonprogramming.in/get-the-day-of-week-from-given-a-date-in-python.html
    Automate the boring stuff with python - Converting datetime Objects into Strings  
    Automate the boring stuff with python - The datatime Module


**_Weekly Task number 6:_**
_ _ _ 

For the Functions topic in week 6, the task was to write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 

* Input is prompting the user to enter a positive number, in this task it is 14.5  

* Output is The square root of 14.5 is approx. 3.8.  

Researched Newton raphson method, which is a way to quickly find an approximation of the square root value based upon a defined value of precision. 
Newton method square root formula calculation is root = (x + (n / x)) * 0.5  

Code:   

    number = float(input("Please enter a positive number: "))
    toleranceLevel = 0.1
    def squareRoot(number, toleranceLevel) :
	x = number
	count = 0
	while (1) :
		count += 1
		root = (x + (number / x)) * 0.5
		if (abs(root - x) < toleranceLevel) :
			break
		x = root
	return root
    print ("The square root of 14.5 is approx", round(squareRoot(number, toleranceLevel),1))

Code Explanation: 

Defined my inputs with the prefix of 'float' to ensure the number is a real number.  
I set a tolerance level on the iteration change to 0.1.  
The program will continue the formula calculation until the iteration change is less than what I set the tolerance level to be.

For the first calculation of the formula, __r = x + (n / x) * 0.5__ , x and n must equal each other. 

Since we don't know the number of iterations it will take us, we need to use a while loop. 

After the first formula calculation, we check if the iteration change (root minus x) is less than the tolerance level I set.  
I used 'abs' to return absolute value.  

On the first iteration, the absolute value of iteration change 6.75 (7.75-14.5) is greater than my tolerance level of 0.1. 
Therefore the result is false and I need to continue the while loop.  I make x equal to the root and loop back to the start of the while function.

When the absolute value of the iteration change is less than my tolerance level of 0.01, we break the while loop and return the square root. 

Finally I round the square root to 1 decimal place as per the expected result.  

References:  

    https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
    https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
    https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
    https://en.wikipedia.org/wiki/Newton%27s_method
    https://www.youtube.com/watch?v=-5e2cULI3H8
    https://surajregmi.medium.com/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64


**_Weekly Task number 7:_**
_ _ _ 

For the Files topic in week 7, the task was to write a program that reads in a text file "moby-dick.txt" and outputs the number of e's it contains.  
The program should take the filename from an argument on the command line.

* Input is moby-dick.txt

* Output is 116960  

Code:   

    filename = input("Enter file name : ")
    l = "e"
    c = 0 
    with open(filename, "rt") as f:
        for line in f:
            words = line.split()
            for i in words:
                for letter in i:
                    if(letter==l):
                        c=c+1
    print("Occurrences of the letter:", c)


Code Explanation:   

I had to allow for input of filename from an argument on the command line, in this task it is "moby-dick.txt".  
Identify the letter to check using l = "e".  
An alternative would be to ask the user to input their desired letter to check **l=input("Enter letter to be searched:")**. 

Start a counter with zero, c=0.  

Open the file in read text mode using rt "with open(filename, "rt") as f:"

A for loop is used to read through each line in the file "for line in f:"  

I intially had code in to convert all upper case to lower case **line = line.lower()**.    
However after running the program, my output didn't match the expected output of 116960.   
Running the program just counting the lower case of the letter e gives the expected output of 116960.
  
Each line is split into a list of words using split (), "words = line.split()"  
A loop is used to work through the words and another loop to work through the letters in the word.  
If the letter equals our input letter of "e" then the letter count is increased by one.  

References:  

    https://www.sanfoundry.com/python-program-read-file-counts-number/  
    https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file  
    https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
    https://stackoverflow.com/questions/36726767/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python
    https://stackoverflow.com/questions/7033987/python-get-files-from-command-line
    https://docs.python.org/3/library/fileinput.html  
    https://www.w3schools.com/python/ref_string_split.asp
    


**_Weekly Task number 8:_**
_ _ _ 

For the Looking ahead topic in week 8, the task was to write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.  


Code:   

    import numpy as np
    import matplotlib.pyplot as plt
    x = np.array([0,4])
    f =x
    g =x**2
    h =x**3
    plt.plot(f, 'r') # red line
    plt.plot(g, 'b') # blue line
    plt.plot(h, 'g') # green line
    plt.plot(title = "Function Plot",
       xlabel = "X Axis", 
       ylabel = "Y Axis")
    plt.legend(['f(x)=x', 'g(x)=x2', 'h(x)=x3'])
    plt.savefig("Weekly_Task_Plot.png")
    plt.show()

Code Explanation:   
Imported numpy and matplotlib.  
Passed array in similar to how we did in the week 08 lectures  
Inserted functions as outlined in the task requirements, using **2 for squared (4*4) and # using **3 for cubed (4*4*4). 
Plotting f, g & h functions separately
formatting the plot 
passing the legend names in a list

References:  

    https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/customize-plot-colors-labels-matplotlib/
    https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html
    https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
    https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib
