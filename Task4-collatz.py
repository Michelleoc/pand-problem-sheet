# A program that asks a user to input any positive integer and outputs the successive values of the following calculation
# At each step, calculate the next value by taking the current value and if it is even, divide by tow but if it is odd, multiply it by three and add one
# The program will end of the current value is one

# Author : Michelle O'Connor

# REFERENCES TO BE ADDED

# numberToEnd = 1

mylist = []

number = int(input ("Please enter a positive integer: "))
mylist.append(number)
while number != 1:

    if (number % 2) == 0:
        number = (number//2)
        mylist.append(number)
        # return (print(int(number)))
    else:
        number = int(3*number +1)
        mylist.append(number)

print (mylist)


