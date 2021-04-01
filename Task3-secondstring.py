# Topic Variables - Weekly Tasks 03
# This program is to ask a user to input a string and the output is every second letter in reverse order
# Author : Michelle O'Connor

# Defined the input with the prefix of 'str' to ensure string format
words = str(input("Please enter a sentence : "))

# To reverse the order of the input use [::-1]
# To get every 2nd letter use [::2]

print (words [::-1][::2])
