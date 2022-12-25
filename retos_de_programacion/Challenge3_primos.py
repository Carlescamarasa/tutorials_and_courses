import math

def prime(a):     # Define function
  if a <= 1:      # We exclude 1, which is not prime 
    return False  
  elif a <= 3:    # If it's minor or equal to 3 (but not negative, 0 or 1), it's prime
    return True
  for i in range(2, int(math.sqrt(a)) + 1): # Loop through the range from 2 to the square root of "a"
      if a % i == 0:
        return False
  return True      #  If the loop ends without finding a divisor, "a" is prime
    
x = int(input("Insert number: ")) # Ask the user to enter a number

if prime(x):                      # Check wheter prime(x) is True (prime) or False (not prime)
    print("It's prime!")
else:
    print("It's not prime...")

