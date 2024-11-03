# Lela Parks
# Oct 31, 2024
# Problem 3: Simulate a coin flip with a given probability for heads

import random

# Set the probability for heads
X = 70  # For example, heads will appear 70% of the time
tails_probability = 100 - X

# Create a list to store results
results = []

# Simulate 1000 coin flips
for _ in range(1000):
    if random.randint(1, 100) <= X:
        results.append('heads')
    else:
        results.append('tails')

# Calculate the percentage of heads
heads_count = results.count('heads')
heads_percentage = (heads_count / len(results)) * 100

# Print results
print(f"Out of 1000 flips, heads appeared {heads_count} times, which is {heads_percentage:.2f}%.")