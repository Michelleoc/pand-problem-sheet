# Calculate BMI - Weekly Tasks 02
# Author : Michelle O'Connor

# REFERENCES TO BE ADDED

Weight = int(input("Enter your weight in kg : "))
Height = int(input("Enter your height in cm : "))

HeightinM2 = (Height/100 * Height/100)
BMI = (Weight / HeightinM2)

print ('Your BMI is {}' .format(BMI))