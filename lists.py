# ──────────────────────────────────────────────
# Python Lists — A Rigorous, Practical Explanation
# ──────────────────────────────────────────────

# 1. What a Python List Actually Is
#
# A Python list is:
#   - Ordered sequence of elements
#   - Mutable
#   - A dynamic array-like data structure
#
# Key properties:
#   Ordered       → position matters (numbers[0] ≠ numbers[1])
#   Mutable       → can change after creation
#   Allows duplicates
#   Heterogeneous → can hold different types
#
# If you think "list = array," you're already making a mistake.
# Python lists are resizable arrays with references, not fixed memory blocks like in C.

numbers = [1, 2, 3, 4]
mixed = [1, "hello", 3.14, True]


# 2. Memory Model (This is where most people fail)
#
# A list does NOT store values directly — it stores references (pointers).
# This is not optional knowledge. If you don't understand this, you will:
#   - Introduce bugs in APIs
#   - Corrupt shared state
#   - Fail in interviews

a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]  — both a and b point to the same list object


# 3. Creating Lists

empty = []
numbers = [1, 2, 3]
from_range = list(range(5))  # [0, 1, 2, 3, 4]

# List comprehension (critical skill):
# Not syntactic sugar — it's faster, more expressive, and expected in production Python.
squares = [x**2 for x in range(5)]


# 4. Accessing Elements
#
# Indices start at 0. Negative indices count from the end (-1 is last).
# Slicing creates a new list — not a view into the original.

lst = [10, 20, 30]
print(lst[0])  # 10
print(lst[-1])  # 30

lst[0:2]  # [10, 20]
lst[::-1]  # reverse

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(f"{bicycles}\n")

print(bicycles[0].capitalize())  # index 0  → first item
print(bicycles[2].upper())  # index 2  → third item
print(bicycles[-1])  # index -1 → last item
message = f"My first bicycle was a {bicycles[0].title()}."
print(f"{message}\n")

# Using index values in f-strings:
names = ["Alice", "Bob", "Charlie", "Diana"]
print(names[0])
print(names[1])
print(names[2])
print(f"{names[3]}\n")

# Building personalised messages:
message = f"Hello, {names[0]}!"
print(message)
message = f"Hello, {names[1]}!"
print(message)
message = f"Hello, {names[2]}!"
print(message)
message = f"Hello, {names[3]}!"
print(f"{message}\n")

# Negative indexing in an f-string:
motorcycles = ["honda", "yamaha", "harley-davidson"]
print(motorcycles)
message = f"I would like to own a {motorcycles[-1].title()} motorcycle."
print(f"{message}\n")


# 5. Mutability — The Core Feature
#
# You can modify lists in-place with append, insert, remove, pop, and direct assignment.
# But don't just memorize — understand the cost (see section 6).

lst = [1, 2, 3]
lst[0] = 100
lst.append(4)
lst.insert(1, 99)
lst.remove(99)
lst.pop()

motorcycles[0] = "jawa"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

motorcycles.insert(1, "ducati")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")
motorcycles = ["honda", "yamaha", "suzuki", "harley-davidson"]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.\n")

too_expensive = "harley-davidson"
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.\n")

guests = ["Alice", "Bob", "Charlie", "Diana"]
invite_message = "You are invited to dinner, "
print(f"{invite_message}{guests[0]}.")
print(f"{invite_message}{guests[1]}.")
print(f"{invite_message}{guests[2]}.")
print(f"{invite_message}{guests[3]}.\n")

guests[1] = "John"
print(f"{invite_message}{guests[0]}.")
print(f"{invite_message}{guests[1]}.")
print(f"{invite_message}{guests[2]}.")
print(f"{invite_message}{guests[3]}.\n")

guests.insert(0, "Emily")
guests.insert(2, "Michael")
guests.append("Sarah")
print(f"Guests: {guests}\n")
print(f"{invite_message}{guests[0]}.")
print(f"{invite_message}{guests[1]}.")
print(f"{invite_message}{guests[2]}.")
print(f"{invite_message}{guests[3]}.")
print(f"{invite_message}{guests[4]}.")
print(f"{invite_message}{guests[5]}.")
print(f"{invite_message}{guests[6]}.\n")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
print(f"{guests}\n")

del guests[1]
del guests[0]
print(f"Guests list: {guests}\n")


# 6. Time Complexity (Where engineers separate from beginners)
#
# Operation         Complexity
# Access index      O(1)
# Append            O(1)*
# Insert (middle)   O(n)
# Delete (middle)   O(n)
# Search            O(n)
#
# *Append is amortized O(1) due to resizing.
# If you're inserting at the front frequently, use collections.deque instead.

lst = [1, 2, 3]
lst.insert(0, 99)  # O(n) — shifts every element


# 7. Organising a List
#
# sort()    → modifies the list in-place, permanently
# sorted()  → returns a new sorted list, original unchanged
# reverse() → reverses in-place

# Custom sorting:
pairs = [(1, "b"), (2, "a")]
pairs.sort(key=lambda x: x[1])

cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original cars list: {cars}")
cars.sort()
print(f"Sorted cars: {cars}")
cars.sort(reverse=True)
print(f"Reverse sorted cars: {cars}\n")

cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original cars list: {cars}")
print(f"Temporarily sorted cars: {sorted(cars)}")
print(f"Original cars list after sorted(): {cars}")
cars.reverse()
print(f"Cars in reverse order after reverse(): {cars}\n")

places = ["paris", "new york", "tokyo", "sydney", "rome"]
print(f"Original places list: {places}")
print(f"Temporarily sorted places: {sorted(places)}")
print(f"Original places list after sorted(): {places}")
print(f"Temporarily reverse sorted places: {sorted(places, reverse=True)}")
print(f"Original places list after reverse sorted(): {places}")
places.reverse()
print(f"Places in reverse order after reverse(): {places}")
places.sort()
print(f"Places sorted permanently: {places}")
places.sort(reverse=True)
print(f"Places reverse sorted permanently: {places}\n")


# 8. Finding the Length of a List

cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Number of cars: {len(cars)}\n")

mountains = ["everest", "k2", "kangchenjunga", "lhotse", "makalu"]
print(f"Original mountains list: {mountains}")
mountains.append("cho oyu")
print(f"Mountains after append(): {mountains}")
mountains.insert(2, "manaslu")
print(f"Mountains after insert(): {mountains}")
del mountains[1]
print(f"Mountains after del: {mountains}")
popped_mountain = mountains.pop()
print(f"Mountains after pop(): {mountains}")
print(f"Popped mountain: {popped_mountain}")
mountains.remove("manaslu")
print(f"Mountains after remove(): {mountains}")
mountains.sort()
print(f"Mountains after sort(): {mountains}")
mountains.sort(reverse=True)
print(f"Mountains after reverse sort(): {mountains}")
mountains.reverse()
print(f"Mountains after reverse(): {mountains}")
print(f"Number of mountains: {len(mountains)}\n")


# 9. Iteration
#
# Avoiding Index Errors — never access an index that doesn't exist.
# Use len() to guard, or prefer iterating directly over the list.

for item in lst:
    print(item)

for i, value in enumerate(lst):
    print(i, value)

motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles[3])  → IndexError: list index out of range
print(motorcycles[-1])  # safe: last item
motorcycles = []
# print(motorcycles[-1]) → IndexError on empty list

magicians = ["alice", "bob", "charlie"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!\n")

pizzas = ["pepperoni", "mushroom", "extra cheese"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
    print(f"{pizza.title()} pizza is my favorite!\n")
print("I really love pizza!\n")

animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!\n")

# Using range():
for value in range(1, 5):
    print(value, end=" ")
print()

numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(f"Squares from 1 to 10: {squares}\n")


# 10. List Comprehensions
# Syntax: [expression for item in iterable if condition]

squares = [value**2 for value in range(1, 11)]
print(f"Squares from 1 to 10 using list comprehension: {squares}")
even_squares = [value**2 for value in range(1, 11) if value % 2 == 0]
print(f"Even squares from 1 to 10 using list comprehension: {even_squares}\n")

list_of_one_to_twenty = list(range(1, 21))
print("Numbers from 1 to 20:")
for number in list_of_one_to_twenty:
    print(f"{number} ", end="")
print("\n")

list_of_one_to_twenty = [number for number in range(1, 21)]  # pylint: disable=unnecessary-comprehension
print("Numbers from 1 to 20 using list comprehension:")
print(f"{list_of_one_to_twenty}\n")

numbers = list(range(1, 1_000_001))
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}\n")

odds = list(range(1, 21, 2))
print("Odd numbers from 1 to 20:")
for number in odds:
    print(f"{number} ", end="")
print("\n")

odds = [number for number in range(1, 21) if number % 2 != 0]
print("Odd numbers from 1 to 20 using list comprehension:")
print(f"{odds}\n")

threes = list(range(3, 31, 3))
print("Threes from 3 to 30:")
for number in threes:
    print(number, end=" ")
print("\n")

threes = [number for number in range(3, 31) if number % 3 == 0]
print("Threes from 3 to 30 using list comprehension:")
print(f"{threes}\n")

cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(f"Cubes from 1 to 10: {cubes}\n")

cubes = [value**3 for value in range(1, 11)]
print(f"Cubes from 1 to 10 using list comprehension: {cubes}\n")


# 11. Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Digits: {digits}")
print(f"Minimum digit: {min(digits)}")
print(f"Maximum digit: {max(digits)}")
print(f"Sum of digits: {sum(digits)}\n")


# 12. Slicing a List
#
# Slicing creates a new list, not a view.

players = ["charles", "martina", "michael", "florence", "eli"]
print(f"Players: {players}")
print(f"First three players: {players[:3]}")
print(f"Players from index 1 to 3: {players[1:4]}")
print(f"Players from index 2 to the end: {players[2:]}")
print(f"Last three players: {players[-3:]}\n")

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print("\n")

buses = ["volvo", "mercedes", "scania", "man", "iveco"]
print(buses[:3])
print(buses[1:4])
print(f"{buses[-3:]}\n")


# 13. Copying Lists (Critical Trap)
#
# Wrong — both names point to the same object:
#   b = a
#
# Correct shallow copy:
#   b = a.copy()
#   b = a[:]
#
# Deep copy for nested lists:
#   b = copy.deepcopy(a)
#
# If you don't know the difference, your system will eventually break.

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print(f"My favorite foods: {my_foods}")
print(f"My friend's favorite foods: {friend_foods}\n")

my_pizzas = ["pepperoni", "mushroom", "extra cheese"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("hawaiian")
friend_pizzas.append("veggie")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")
print("\n")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
print("\n")

print("My foods are:")
for food in my_foods:
    print(f"- {food}")
print("\n")

print("My friend's foods are:")
for food in friend_foods:
    print(f"- {food}")
print("\n")


# 14. Nested Lists

matrix = [[1, 2], [3, 4]]
matrix[0][1]  # 2

# Dangerous pattern — all rows reference the SAME inner list:
matrix = [[0] * 3] * 3
# Modifying one row modifies all. Use a comprehension instead:
matrix = [[0] * 3 for _ in range(3)]


# 15. When NOT to Use Lists
#
# Use alternatives when appropriate:
#   set        → fast membership checks
#   tuple      → immutable data
#   deque      → fast insert/remove at both ends
#   NumPy array → numerical computation


# 16. Real-World Use Cases
#
# Lists are used for:
#   - API payload construction
#   - Iterating database results
#   - Building pipelines
#   - Collecting intermediate results
#
# But they become dangerous when:
#   - Shared across layers without copying
#   - Used as queues incorrectly
#   - Misused for large-scale data


# 17. Subtle Pitfalls (You should recognize these instantly)
#
# Mutable default argument — accumulates state across calls:
def func(lst=[]):  # pylint: disable=dangerous-default-value
    lst.append(1)
    return lst


# Modifying a list while iterating over it — dangerous:
lst = [1, 2, 3]
for x in lst:
    # skips elements; use a copy or list comprehension instead
    lst.remove(x)  # pylint: disable=modified-iterating-list


# 18. Mental Model (If you remember nothing else)
#
# A Python list is:
#   A dynamic array of references with O(1) indexing,
#   mutable state, and hidden resizing cost.
#
# If your mental model is weaker than this, you're guessing — not engineering.

# ──────────────────────────────────────────────
# Final Challenge (Don't skip this)
# ──────────────────────────────────────────────
# Answer this without running code:

a = [1, 2, 3]
b = a[:]
b.append(4)

print(a)

# If your answer is wrong, you don't understand lists yet.
