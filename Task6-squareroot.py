# Topic 'Functions' - Weekly Task 06
# Take a positive floating point number as the input and output an approximation of its square root
# Author : Michelle O'Connor

# Newton formula r = x + (n / x) / 2
# or r = x + (n / x) * 0.5

# Positive Integar (n) = 14.5						
							
#	                x	       number	     x	      n/x	          2	      Root	                        Iteration Change
# Iteration 1	 14.50000 	 14.50000 	 14.5000 	 1.00000 	 2.0000 	 7.75000 	r = (x + n / x) / 2     
# Iteration 2	 7.75000 	 14.50000 	 7.75000 	 1.87097 	 2.0000 	 4.81048 	r = (x + n / x) / 2     2.93952
# Iteration 3	 4.81048 	 14.50000 	 4.81048 	 3.01425 	 2.0000 	 3.91237	r = (x + n / x) / 2     0.89812
# Iteration 4	 3.91237 	 14.50000 	 3.91237 	 3.70620 	 2.0000 	 3.80928	r = (x + n / x) / 2     0.10309
# Iteration 5	 3.80928 	 14.50000 	 3.80928 	 3.80649 	 2.0000 	 3.80789 	r = (x + n / x) / 2     0.00139
# Iteration 6	 3.80789 	 14.50000 	 3.80789 	 3.80789 	 2.0000 	 3.80789	r = (x + n / x) / 2     0.00000
# Iteration 7	 3.80789 	 14.50000 	 3.80789 	 3.80778 	 2.0000 	 3.80789	r = (x + n / x) / 2     0.00000

# Defined my inputs with the prefix of 'float' to ensure the number is a real number
number = float(input("Please enter a positive number: "))

# Set a tolerance level on the iteration change.  
# The program will continue the formula calculation until the iteration change is less than what I set it to the tolerance level
toleranceLevel = 0.1

def squareRoot(number, toleranceLevel) :

	# For the first calculation of the formula, x and number must equal each other
	x = number

	# Start the count the number of iterations
	count = 0

# Since we don't know the number of iterations it will take us, we need to use a while loop
	while (1) :
		count += 1

		# Newton method square root formula calculation
		root = (x + (number / x)) * 0.5

		# Check if the iteration change is less the tolerance level I set.  
        # Used abs to return absolute value.
        # On the first iteration the absolute value of the iteration change 6.75 (7.75-14.5) is greater than our tolerance level of 0.1.
		# Therefore the outcome is false.
		if (abs(root - x) < toleranceLevel) :
			# The while loop will break when the iteration change is less than the tolerance level of 0.1, i.e true 			
			break
			
		# If the result of the above formula is false (i.e the iteration change is higher than the tolerance level)
		# I make x equal to the root and loop back to the start of the while function
		x = root

	return root

# round the square root to 1 decimal place as per the expected result
print ("The square root of 14.5 is approx", round(squareRoot(number, toleranceLevel),1))

# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
# https://www.youtube.com/watch?v=-5e2cULI3H8
# https://surajregmi.medium.com/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64
# https://en.wikipedia.org/wiki/Newton%27s_method

