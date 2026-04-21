# What is Python? - Python is a high-level, interpreted, general-purpose
#  programming language known for its clean, readable syntax that emphasizes simplicity.

# Key traits:

# Interpreted — runs line by line, no compilation step
# Dynamically typed — variable types are determined at runtime
# Multi-paradigm — supports procedural, object-oriented, and functional styles
# Large standard library — "batteries included" philosophy
# Widely used — web dev, data science, automation, AI/ML, scripting

# Python Syntax — Learn by Running

# ── 1. Code runs top to bottom ──────────────────────────────────────────────

print("Start")
print("Middle")
print("End")

# ── 2. Indentation defines blocks (no {}) ───────────────────────────────────

x = 10
if x > 5:
    print("Inside the block")  # indented → belongs to if
print("Outside the block")  # not indented → always runs

# ── 3. Colon starts a block ──────────────────────────────────────────────────

if x > 10:
    print("High")
elif x > 5:
    print("Medium")  # this one runs
else:
    print("Low")

# ── 4. Loops ─────────────────────────────────────────────────────────────────

for i in range(3):
    print("for loop:", i)  # prints 0, 1, 2

count = 3
while count > 0:
    print("while loop:", count)  # prints 3, 2, 1
    count -= 1

# ── 5. Functions group reusable logic ────────────────────────────────────────


def add(a, b):
    return a + b


print("2 + 3 =", add(2, 3))  # 2 + 3 = 5

# ── 6. Data structures ───────────────────────────────────────────────────────

numbers = [1, 2, 3]  # list — ordered, changeable
user = {"name": "John"}  # dict — key/value pairs

print(numbers[0])  # 1
print(user["name"])  # John

# ── 7. f-strings (modern string formatting) ──────────────────────────────────

name = "John"
print(f"Hello, {name}!")

# ── 8. Errors stop execution at that line ────────────────────────────────────

# Uncomment to see: Python prints "Before" but never "After"
# print("Before")
# print(1 / 0) # ZeroDivisionError: division by zero
# print("After")

# ── 9. Bytecode & __pycache__ ────────────────────────────────────────────────

# When you run: python syntax.py
# Python does 3 steps:
#   1. Parse  — checks indentation, colons, balanced parentheses
#   2. Compile — converts code to bytecode (stored in __pycache__/*.pyc)
#   3. Execute — Python Virtual Machine runs bytecode instruction by instruction

# The "line-by-line" feeling comes from step 3, but it's really bytecode, not raw text.
