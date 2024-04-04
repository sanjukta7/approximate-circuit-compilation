import random

# Define the length of the list and the range for random values
list_length = 3

# Generate a list of random values with varying min and max values
random_values = [random.randint(min_value, max_value) for min_value, max_value in zip([3,4,5], [5,7,10])]

print(random_values)

a = [1,2,3]
b = [6,7,8]

print(a*b)