# Topic 'Variables' - Weekly Task 03
# This program is to ask a user to input a string and the output is every second letter in reverse order
# Author : Michelle O'Connor

# Defined the input with the prefix of 'str' to ensure string format
words = str(input("Please enter a sentence : "))

# To reverse the order of the input use [::-]
# To get every 2nd letter use [::2]
# Combining the reversing action [::-] with every 2nd letter action [::2] condenses the code

print (words [::-2])

# References:
# https://www.w3schools.com/python/python_howto_reverse_string.asp
# https://stackoverflow.com/questions/33470227/how-do-i-reverse-the-letters-in-a-string-in-python   
# https://docs.python.org/2/whatsnew/2.3.html#extended-slices   
