# Topic 'Files' - Weekly Task 07
# Write a program that reads in a text file and outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author : Michelle O'Connor

# Allow for input of filename from an argument on the command line
filename = input("Enter file name : ")

# Task lists e as the letter to check for 
l = "e"

# or alternatively we could have asked the user to input their desired letter
# l=input("Enter letter to be searched:")
# https://www.sanfoundry.com/python-program-read-file-counts-number/

# c is our counter
c = 0 

# Open the file in read text mode using rt
with open(filename, "rt") as f:
    # A for loop is used to read through each line in the file
    for line in f:
        # I was originally working on the assumption that they want Upper and Lower case of the letter e
        # So I converted upper to lower case 
        # line = line.lower()
        # However from running the program with and without this line, it became apparent only counting the lower case 
        # was needed to get the expected outcome

        # Each line is split into a list of words using split ()
        words = line.split()
        # A loop is used to work through the words and another loop to work through the letters in the word
        for i in words:
            for letter in i:
                # If the letter equals our input letter of "e" then the letter count is increased by one
                if(letter==l):
                    c=c+1
                    
print("Occurrences of the letter:", c)

# https://www.sanfoundry.com/python-program-read-file-counts-number/
# https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# https://stackoverflow.com/questions/36726767/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python
# https://stackoverflow.com/questions/7033987/python-get-files-from-command-line
# https://docs.python.org/3/library/fileinput.html
# https://www.w3schools.com/python/ref_string_split.asp


