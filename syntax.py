# Python Syntax — The Only Things You Actually Need to Know

# What Actually Happens When You Run Python Code

# When you run:

# python file.py

# Python does 3 main steps internally.

# Parse, Read & Check Syntax

# Python reads your entire file and checks:

# * Is indentation correct?
# * Are colons present?
# * Are parentheses balanced?

# If something is wrong → you get SyntaxError or OtherError before anything runs.

# So it doesn't execute each line blindly.

# Compile to Bytecode

# Python converts your code into something called bytecode.

# Not machine code.
# Not raw text.
# But an intermediate format.

# Example:

print("Hello")

# Gets translated internally into bytecode instructions.

# This bytecode may be stored in:

# __pycache__/

# You’ll see files like:

# main.cpython-312.pyc
# Execute via Python Virtual Machine (PVM)

# The Python Virtual Machine runs that bytecode instruction by instruction.

# This is where the “line-by-line” feeling comes from.

# It executes sequentially unless control flow changes:

# if
# for
# while
# function calls
# exceptions
# So, Is it souds like Line-by-Line?
# Conceptually → Yes
# Technically → It executes bytecode instruction by instruction

# Big difference.

# Example
print("Start")
a = 10
y = 0

print(a / y)  # This will error, but you see "Start" printed first.
print("End")  # This will never run because of the error above.


# Code reads top → bottom


print("Start")
print("End")


# Indentation = structure must be indented to show it belongs to the block above


x = 10
if x > 5:
    print("Inside")

print("Outside")

# No `{}`
# No guessing
# Wrong spacing = broken code


# Use `:` to start a block

if x > 5:
    print("Big")


# Colon means:

# “Start a block → indent next lines”


# Conditions (decision making)

if x > 10:
    print("High")
elif x > 5:
    print("Medium")
else:
    print("Low")


# Loops (repeat things)

for i in range(3):
    print(i)


while x > 0:
    x -= 1


# Functions (reusable logic)


def add(a, b):
    return a + b


# Call it:

add(2, 3)


# Data structures (containers)

numbers = [1, 2, 3]  # list
user = {"name": "John"}  # dict

# Strings (modern way)

name = "John"
print(f"Hello {name}")


# The Real Rule (Everything Else Is Noise)

# Python syntax is basically:

# “Use indentation to group logic, and write readable code.”

# That’s it.

#  You should be writing code until syntax becomes second nature.


# Minimal Model of Python Syntax

# 1. Code runs top to bottom
# 2. `:` starts a block
# 3. Indentation defines the block
# 4. Functions group logic
# 5. Lists/dicts store data
