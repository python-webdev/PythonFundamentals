# ──────────────────────────────────────────────
# Python Lists — A Rigorous, Practical Explanation
# ──────────────────────────────────────────────

import random
from itertools import zip_longest

# 1. What a Python List Actually Is

# A Python list is:
#   - Ordered sequence of elements
#   - Mutable
#   - A dynamic array-like data structure

# Key properties:
#   - Ordered       → position matters (numbers[0] ≠ numbers[1])
#   - Mutable       → can change after creation
#   - Allows duplicates
#   - Heterogeneous → can hold different types
#
# If you think "list = array," you're already making a mistake.
# Python lists are resizable arrays with references, not fixed memory blocks like in C.

numbers = [1, 2, 3, 4]
mixed = [1, "hello", 3.14, True]


# 2. Memory Model (This is where most people fail)

# A list does NOT store values directly — it stores references (pointers).
# This is not optional knowledge. If you don't understand this, you will:
#   - Introduce bugs in APIs
#   - Corrupt shared state
#   - Fail in interviews

# ─────────────────────────────────────────────────────────────
#  HOW A LIST STORES DATA IN MEMORY
# ─────────────────────────────────────────────────────────────
#
#  numbers = [1, 2, 3]
#
#  Stack (names)        Heap (objects)
#  ┌──────────┐         ┌─────────────────────────────┐
#  │ numbers ─┼────────►│  list object                │
#  └──────────┘         │  ┌──────┬──────┬──────┐     │
#                       │  │ ptr0 │ ptr1 │ ptr2 │     │
#                       │  └──┬───┴──┬───┴──┬───┘     │
#                       └─────┼──────┼──────┼─────────┘
#                             │      │      │
#                             ▼      ▼      ▼
#                           int(1) int(2) int(3)
#
#  The list does NOT contain 1, 2, 3.
#  It contains three pointers that each point to an int object.
# ─────────────────────────────────────────────────────────────
#
#  ALIASING — b = a  (both names, one object)
#
#  Stack                Heap
#  ┌───┐                ┌───────────────────────┐
#  │ a ┼───────────────►│  list [ptr0,ptr1,ptr2]│
#  ├───┤                └───────────────────────┘
#  │ b ┼───────────────►   (same object ↑)
#  └───┘
#
#  b.append(4) mutates the object — a sees it too.
#  a is b  →  True
# ─────────────────────────────────────────────────────────────
#
#  SHALLOW COPY — b = a[:]  or  b = a.copy()
#
#  Stack                Heap
#  ┌───┐                ┌───────────────────────┐
#  │ a ┼───────────────►│ list [ptr0,ptr1,ptr2] │
#  └───┘                └───────────────────────┘
#                              │      │      │
#                              ▼      ▼      ▼
#  ┌───┐                ┌───────────────────────┐
#  │ b ┼───────────────►│ list [ptr0,ptr1,ptr2] │  ← new list object
#  └───┘                └───────────────────────┘
#                              │      │      │
#                              └──────┼──────┘
#                              same int objects (shared)
#
#  Appending to b does NOT affect a (different list objects).
#  But if elements are mutable (e.g. dicts, lists), mutating
#  one element affects both a and b — they share the same pointers.
# ─────────────────────────────────────────────────────────────
#
#  NESTED LIST TRAP — [[0]*3]*3
#
#  matrix = [[0]*3]*3   ← WRONG
#
#  Heap
#  ┌─────────────────────────────────┐
#  │ outer list [ptr, ptr, ptr]      │
#  └──────┬──────┬──────┬────────────┘
#         │      │      │
#         └──────┴──────┘
#              all three point to the SAME inner list
#              │
#              ▼
#         [0, 0, 0]
#
#  matrix[0][1] = 9  →  matrix is now [[0,9,0],[0,9,0],[0,9,0]]
#
#  FIX: matrix = [[0]*3 for _ in range(3)]  ← each row is a new object
# ─────────────────────────────────────────────────────────────


# 3. Creating Lists

empty = []
numbers = [1, 2, 3]
from_range = list(range(5))  # [0, 1, 2, 3, 4]

# List comprehension (critical skill):
# Not syntactic sugar — it's faster, more expressive, and expected in production Python.
squares = [x**2 for x in range(5)]


# 4. Accessing Elements

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


# 5. List Methods — 11 Core Methods with Real-World Use Cases

# ── append(item) ──────────────────────────────────────────────
# Adds a single item to the end of the list. O(1) amortised.
# Real world: collecting validation errors before returning them to the user.

errors = []
if not "username":
    errors.append("Username is required.")
if not "email":
    errors.append("Email is required.")
errors.append("Password must be at least 8 characters.")
print(f"Form errors: {errors}\n")

# ── insert(index, item) ───────────────────────────────────────
# Inserts at a specific position. O(n) — every element after shifts right.
# Real world: bumping an urgent ticket to the front of a support queue.

task_queue = ["send invoice", "update profile", "generate report"]
task_queue.insert(0, "fix critical bug")
print(f"Task queue after urgent insert: {task_queue}\n")

# ── extend(iterable) ─────────────────────────────────────────
# Appends every item from an iterable. More efficient than looping append.
# Real world: merging paginated API results into a single list.

page_1 = ["user_1", "user_2", "user_3"]
page_2 = ["user_4", "user_5", "user_6"]
all_users = []
all_users.extend(page_1)
all_users.extend(page_2)
print(f"All users after pagination merge: {all_users}\n")

# ── remove(item) ──────────────────────────────────────────────
# Removes the first occurrence of a value. Raises ValueError if not found.
# Real world: unsubscribing a user from a notification list.

subscribers = ["alice@email.com", "bob@email.com", "carol@email.com"]
subscribers.remove("bob@email.com")
print(f"Subscribers after removal: {subscribers}\n")

# ── pop(index=-1) ─────────────────────────────────────────────
# Removes and returns an item (default: last). O(1) at end, O(n) in middle.
# Real world: processing the latest job off a LIFO work stack.

processing_stack = ["job_a", "job_b", "job_c"]
current_job = processing_stack.pop()
print(f"Processing: {current_job}")
print(f"Remaining stack: {processing_stack}\n")

# ── clear() ───────────────────────────────────────────────────
# Removes all items in-place. The list object itself is retained.
# Real world: resetting a shopping cart without reassigning the variable,
#             keeping all existing references to the same cart consistent.

cart = ["apple", "banana", "cherry"]
print(f"Cart before clear: {cart}")
cart.clear()
print(f"Cart after clear: {cart}\n")

# ── index(item, start=0, end=len) ─────────────────────────────
# Returns the index of the first matching value. Raises ValueError if absent.
# Real world: finding where a selected theme sits so prev/next can be offered.

themes = ["light", "dark", "high-contrast", "solarized"]
current_theme = "dark"
pos = themes.index(current_theme)
next_theme = themes[pos + 1] if pos + 1 < len(themes) else themes[0]
print(f"Current theme: '{current_theme}' at index {pos}")
print(f"Next theme: '{next_theme}'\n")

# ── count(item) ───────────────────────────────────────────────
# Returns how many times a value appears. O(n).
# Real world: analytics — counting how many times a product page was visited.

page_views = ["home", "product", "product", "cart", "product", "checkout"]
product_views = page_views.count("product")
print(f"Product page views: {product_views}\n")

# ── sort(key=None, reverse=False) ─────────────────────────────
# Sorts in-place using Timsort. Stable — equal elements keep relative order.
# Real world: ranking leaderboard entries by score, highest first.

leaderboard = [
    ("Alice", 4200),
    ("Bob", 8750),
    ("Carol", 3100),
    ("Diana", 8750),
]
leaderboard.sort(key=lambda entry: entry[1], reverse=True)
print(f"Leaderboard (sorted): {leaderboard}\n")

# ── reverse() ─────────────────────────────────────────────────
# Reverses the list in-place. O(n).
# Real world: displaying a chat history with newest messages at the top.

chat_history = ["Hello!", "How are you?", "Great, thanks!", "Talk later."]
chat_history.reverse()
print(f"Chat (newest first): {chat_history}\n")

# ── copy() ────────────────────────────────────────────────────
# Returns a shallow copy. Equivalent to lst[:].
# Real world: preserving the original playlist order while creating
#             a shuffled version for playback — both coexist independently.

playlist = ["song_a", "song_b", "song_c", "song_d"]
shuffled = playlist.copy()
random.shuffle(shuffled)
print(f"Original playlist: {playlist}")
print(f"Shuffled playlist:  {shuffled}\n")


# 6. Mutability — The Core Feature

# You can modify lists in-place with append, insert, remove, pop, and direct assignment.
# But don't just memorize — understand the cost (see section 7).

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


# 7. Time Complexity (Where engineers separate from beginners)

# Operation         Complexity
# Access index      O(1)
# Append            O(1)*
# Insert (middle)   O(n)
# Delete (middle)   O(n)
# Search            O(n)

# *Append is amortized O(1) due to resizing.
# If you're inserting at the front frequently, use collections.deque instead.

lst = [1, 2, 3]
lst.insert(0, 99)  # O(n) — shifts every element


# 8. Organising a List

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


# 9. Finding the Length of a List

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


# 10. Iteration

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


# 11. List Comprehensions
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


# 12. Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Digits: {digits}")
print(f"Minimum digit: {min(digits)}")
print(f"Maximum digit: {max(digits)}")
print(f"Sum of digits: {sum(digits)}\n")


# 13. Slicing a List

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


# 14. Copying Lists (Critical Trap)

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

# Reference identity — a and b point to the same list object in memory:
a = [1, 2, 3]
b = a
print(a is b)  # True — a and b reference the same list object
b.append(4)
print(a)  # [1, 2, 3, 4] — mutation via b is visible through a

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


# 15. Nested Lists

matrix = [[1, 2], [3, 4]]
matrix[0][1]  # 2

# Dangerous pattern — all rows reference the SAME inner list:
matrix = [[0] * 3] * 3
# Modifying one row modifies all. Use a comprehension instead:
matrix = [[0] * 3 for _ in range(3)]


# 16. When NOT to Use Lists

# Use alternatives when appropriate:
#   set        → fast membership checks
#   tuple      → immutable data
#   deque      → fast insert/remove at both ends
#   NumPy array → numerical computation


# 17. Real-World Use Cases
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


# 18. Subtle Pitfalls (You should recognize these instantly)


# Mutable default argument — accumulates state across calls:
def func(lst=[]):  # pylint: disable=dangerous-default-value
    lst.append(1)
    return lst


# Modifying a list while iterating over it — dangerous:
lst = [1, 2, 3]
for x in lst:
    # skips elements; use a copy or list comprehension instead
    lst.remove(x)  # pylint: disable=modified-iterating-list


# 19. Packing, Unpacking, and zip / unzip

# ── Does packing/unpacking belong to lists? ───────────────────────────────
# Unpacking is a general Python feature — it works with ANY iterable
# (list, tuple, string, generator, etc.).
# Lists are just the most common container you'll unpack in practice.

# Basic unpacking — left-hand side must match the length exactly:
rgb = [255, 128, 0]
r, g, b = rgb
print(f"Red: {r}, Green: {g}, Blue: {b}\n")  # Red: 255, Green: 128, Blue: 0

# ── Extended unpacking with * ─────────────────────────────────────────────
# The starred variable soaks up everything that doesn't match a named target.
# It always produces a list, regardless of the source iterable type.

scores = [98, 87, 76, 65, 54, 43]
top, *middle, bottom = scores
print(f"Top: {top}")  # 98
print(f"Middle: {middle}")  # [87, 76, 65, 54]
print(f"Bottom: {bottom}")  # 43

# Real world: ignoring all but the first element from an API response header.
status, *_ = ["200", "OK", "text/html", "gzip"]
print(f"Status: {status}\n")

# ── Packing ───────────────────────────────────────────────────────────────
# Collecting individual values into a list is just assignment — no special syntax.
# The * operator in a function call packs a list into positional arguments.

coords = [37.7749, -122.4194]
lat, lon = coords  # unpack
packed_again = [lat, lon]  # pack back into a list


def show_location(latitude, longitude):
    print(f"Location: {latitude}, {longitude}")


show_location(*coords)  # unpack list into positional args
print()

# ── Swap without a temp variable ──────────────────────────────────────────
# This is unpacking under the hood — Python builds a tuple on the right,
# then unpacks it into the names on the left.

a, b = 1, 2
a, b = b, a
print(f"After swap: a={a}, b={b}\n")

# ── zip() — pairing iterables element-by-element ─────────────────────────
# zip() stops at the shortest iterable.
# Returns a zip object (lazy iterator), not a list — convert if you need one.

names = ["Alice", "Bob", "Carol"]
scores_list = [95, 87, 72]
paired = list(zip(names, scores_list))
print(f"Zipped pairs: {paired}\n")

# Real world: building a dict from two lists — a very common pattern.
student_grades = dict(zip(names, scores_list))
print(f"Student grades: {student_grades}\n")

# Real world: iterating two lists in parallel without using index arithmetic.
for name, score in zip(names, scores_list):
    print(f"{name}: {score}")
print()

# zip with three iterables:
cities = ["London", "Tokyo", "New York"]
countries = ["UK", "Japan", "USA"]
timezones = ["GMT+0", "GMT+9", "GMT-5"]
for city, country, tz in zip(cities, countries, timezones):
    print(f"{city}, {country} ({tz})")
print()

# ── unzip — reversing a zip ───────────────────────────────────────────────
# There is no unzip() built-in. The idiom is zip(*zipped).
# The * unpacks the list of tuples into individual arguments for zip.

pairs = [("Alice", 95), ("Bob", 87), ("Carol", 72)]
names_out, scores_out = zip(*pairs)
print(f"Names:  {list(names_out)}")  # ['Alice', 'Bob', 'Carol']
print(f"Scores: {list(scores_out)}")  # [95, 87, 72]
print()

# ── zip_longest — when lengths differ ────────────────────────────────────
# zip() silently drops extras. Use itertools.zip_longest to keep them.

products = ["apple", "banana", "cherry"]
prices = [1.20, 0.50]  # intentionally shorter
for product, price in zip_longest(products, prices, fillvalue="N/A"):
    print(f"{product}: {price}")
print()

# ── enumerate() — index + value without range(len()) ─────────────────────
# enumerate() is the correct way to get both an index and a value.
# Never write: for i in range(len(lst)): value = lst[i]

menu_items = ["burger", "fries", "drink"]
for i, item in enumerate(menu_items, start=1):
    print(f"{i}. {item}")
print()


# 20. Mental Model (If you remember nothing else)

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
