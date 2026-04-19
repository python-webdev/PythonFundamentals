# Python Variables
# What is a variable?
# A box that stores a value in memory.
pythonname = "John"  # string
age = 25
is_active = True

# Naming Rules

# Must start with a letter or underscore (_)
# Can contain letters, numbers, underscores
# Case-sensitive (name ≠ Name)
# Use snake_case by convention

pythonuser_name = "Jane"  # valid
_private = 42         
2fast = "no" # can't start with a number 


# Multiple Assignment
pythona = b = c = 0          # all three = 0
x, y, z = 1, 2, 3     # unpack


# Swapping Variables
a = 5
b = 10
a, b = b, a  # swap values
print(a)  # 10
print(b)  # 5

# Constants (by convention)
# Python has no true constants — we will use ALL_CAPS as a signal to other developers:
pythonMAX_RETRIES = 3
BASE_URL: str = "https://api.example.com"

