# Topic 'Controlling the flow' - Weekly Task 04
# A program that asks a user to input any positive integer and outputs the successive values of the following calculation
# At each step, calculate the next value by taking the current value and if it is even, divide by two but if it is odd, multiply it by three and add one
# The program will end of the current value is one

# Author : Michelle O'Connor

# REFERENCES TO BE ADDED

# numberToEnd = 1

# Defined the input with the prefix of 'int' to ensure the number is a whole number

number = int(input ("Please enter a positive integer: "))

# Define my list as a 'list' [] type 
mylist = []

# while statement needed to run the code over and over again as long as the while statement’s condition is True, i.e. the value been greater than 1
# for each run of the code, we want the output to be added it to the list and used as the next input for the code

mylist.append(number)
while number != 1:
    if (number % 2) == 0:
        number = (number//2)
        mylist.append(number)
        # if the number is even divide by 2
        # add output to the list
    else:
        number = int(3*number +1)
        mylist.append(number)
        # if the number is not even (i.e odd) muliple by 3 and add one
        # add output to the list

print (mylist)


