# pylint: disable=duplicate-value, useless-else-on-loop
# ============================================================
# LOOPS IN PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. FOR LOOP
# Iterates over any iterable: list, string, range, tuple, etc.
# ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

# Tuple
coordinates = 10, 20, 30
for value in coordinates:
    print(value)
# 10  20  30

# Set (order is not guaranteed)
unique_numbers = {3, 1, 4, 1, 5}  # duplicates are removed
for num in unique_numbers:
    print(num)
# 1  3  4  5  (some order, but not necessarily insertion order)

# Dictionary — iterates over keys by default
person = {"name": "Alice", "age": 25, "city": "NY"}

for key in person:
    print(key)
# name  age  city

for key, value in person.items():  # key-value pairs
    print(key, "->", value)
# name -> Alice
# age  -> 25
# city -> NY

for value in person.values():  # values only
    print(value)
# Alice  25  NY

# String
for char in "hello":
    print(char)
# h  e  l  l  o


# ------------------------------------------------------------
# 2. WHILE LOOP
# Runs as long as the condition is True.
# ------------------------------------------------------------

count = 0
while count < 5:
    print(count)
    count += 1
# 0  1  2  3  4

# Infinite loop (use break to exit — see below)
# while True:
#     user_input = input("Type 'quit' to exit: ")
#     if user_input == "quit":
#         break


# ------------------------------------------------------------
# 3. BREAK, CONTINUE, PASS
# ------------------------------------------------------------

# break — exits the loop immediately
for num in range(10):
    if num == 5:
        break
    print(num)
# 0  1  2  3  4

# continue — skips the rest of this iteration, moves to the next
for num in range(6):
    if num == 3:
        continue
    print(num)
# 0  1  2  4  5  (3 is skipped)

# pass — does nothing; a placeholder so the block isn't empty
for num in range(3):
    pass  # loop runs but nothing happens — useful when stubbing code


# ------------------------------------------------------------
# 4. RANGE()
# Generates a sequence of numbers. Syntax: range(start, stop, step)
# stop is exclusive (not included in the sequence).
# ------------------------------------------------------------

list(range(5))  # [0, 1, 2, 3, 4]
list(range(2, 8))  # [2, 3, 4, 5, 6, 7]
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]   (step = 2)
list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  (countdown)

for i in range(1, 6):
    print(i)
# 1  2  3  4  5


# ------------------------------------------------------------
# 5. ENUMERATE()
# Loops over an iterable and gives both the index and the value.
# Avoids manually tracking a counter variable.
# ------------------------------------------------------------

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)
# 0 red
# 1 green
# 2 blue

# Custom start index
for index, color in enumerate(colors, start=1):
    print(index, color)
# 1 red
# 2 green
# 3 blue


# ------------------------------------------------------------
# 6. FOR...ELSE / WHILE...ELSE
# The else block runs only if the loop finished WITHOUT hitting break.
# ------------------------------------------------------------

# for...else
numbers = [1, 3, 5, 7]
for n in numbers:
    if n % 2 == 0:
        print("Found even:", n)
        break
else:
    print("No even numbers found")  # runs because break was never hit
# No even numbers found

# while...else
count = 0
while count < 3:
    count += 1
else:
    print(
        "Loop completed normally"
    )  # runs because condition became False, not break
# Loop completed normally


# ------------------------------------------------------------
# 7. NESTED LOOPS
# A loop inside another loop — the inner loop runs fully for each outer iteration.
# ------------------------------------------------------------

rows = [1, 2, 3]
cols = ["A", "B", "C"]

for row in rows:
    for col in cols:
        print(f"{row}{col}", end="  ")
    print()
# 1A  1B  1C
# 2A  2B  2C
# 3A  3B  3C

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
# 1  2  3
# 2  4  6
# 3  6  9


# ------------------------------------------------------------
# 8. ZIP()
# Iterates over two (or more) iterables in parallel, pair by pair.
# Stops at the shortest iterable.
# ------------------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
scores = [95, 82, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 95
# Bob: 82
# Charlie: 78

# Zip three iterables together
cities = ["NY", "LA", "SF"]
for name, score, city in zip(names, scores, cities):
    print(f"{name} from {city} scored {score}")
# Alice from NY scored 95
# Bob from LA scored 82
# Charlie from SF scored 78


# ------------------------------------------------------------
# 9. LIST COMPREHENSION
# A concise one-line way to build a list from a for loop.
# Syntax: [expression for item in iterable if condition]
# ------------------------------------------------------------

# Syntax:
# [expression for item in iterable if condition]
#  ──────────  ────  ────────────  ─────────────
#      │         │       │               │
#      │         │       │               └── optional filter
#      │         │       └── any iterable (list, range, string...)
#      │         └── loop variable
#      └── what to put in the new list

# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(squares)  # [1, 4, 9, 16, 25]

# Basic — no condition
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition (filter)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Transform + filter together
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Transforming strings
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words if len(w) > 4]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Nested — flattens a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]


# ------------------------------------------------------------
# PRACTICAL EXAMPLES
# ------------------------------------------------------------

# Sum numbers 1–100 using range()
total = 0
for n in range(1, 101):
    total += n
print(total)  # 5050

# Find the first even number in a list using break
numbers = [1, 3, 7, 4, 9, 6]
for n in numbers:
    if n % 2 == 0:
        print("First even:", n)  # First even: 4
        break

# Print only odd numbers using continue
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)
# 1  3  5  7  9

# Build a numbered menu using enumerate()
menu = ["Start Game", "Load Game", "Settings", "Quit"]
for i, option in enumerate(menu, start=1):
    print(f"{i}. {option}")
# 1. Start Game
# 2. Load Game
# 3. Settings
# 4. Quit

# Countdown using while + range alternative
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Go!")
# 3  2  1  Go!
