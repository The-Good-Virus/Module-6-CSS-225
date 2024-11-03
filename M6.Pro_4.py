# Lela Parks
# Nov 1, 2024
# Problem 4: Calculate the factorial using the math module and manually

import math

# Get user input
number = int(input("Enter a non-negative integer to calculate its factorial: "))

# Calculate factorial using the math module
math_factorial = math.factorial(number)

# Calculate factorial manually
manual_factorial = 1
for i in range(1, number + 1):
    manual_factorial *= i

# Print the results
print(f"Factorial calculated using math module: {math_factorial}")
print(f"Factorial calculated manually: {manual_factorial}")

# Compare results
if math_factorial == manual_factorial:
    print("Both methods give the same result.")
else:
    print("There is a discrepancy in the results.")
