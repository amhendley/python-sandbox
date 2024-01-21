from functools import partial

# Using partial with the built-in pow function
square = partial(pow, exp=2)

# Testing the new function
print(square(4)) # Outputs: 16
print(square(5)) # Outputs: 25
