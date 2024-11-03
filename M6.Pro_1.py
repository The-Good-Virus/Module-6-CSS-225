# Lela Parks
# Oct 30, 2024
# Problem 1: Generate 10 random integers between 25 and 35

import random

rand_nums = []  # List to store random numbers

# Generate 10 random integers
for _ in range(10):
    num = random.randrange(25, 36)  # Random integer between 25 and 35
    rand_nums.append(num)  # Append to the list
    print(num)  # Print each random number

print("List of random numbers:", rand_nums)  # Print the list of random numbers