# Topic Statements - Weekly Tasks 02
# This program calculates a person's Body Mass Index (BMI) using centimetres as input for height and kilograms as input for weight
# Author : Michelle O'Connor

# Defined my inputs with the prefix of 'int' to ensure the number is a whole number
Weight = int(input("Enter your weight in kg : "))
Height = int(input("Enter your height in cm : "))

# As the inputs for height are in centimetres, the height value needed to be divided by 100 for the BMI formula calculation
HeightinM2 = (Height/100 * Height/100)

# Rounded the BMI result to 2 decimal places
BMI = round((Weight / HeightinM2),2)

print ('Your BMI is {}' .format(BMI))