# ──────────────────────────────────────────────
# Python Tuples — A Rigorous, Practical Explanation
# ──────────────────────────────────────────────

import sys
from collections import namedtuple
from itertools import zip_longest

# 1. What a Python Tuple Actually Is

# A Python tuple is:
#   - Ordered sequence → position matters (t[0] ≠ t[1])
#   - Immutable        → cannot change after creation
#   - Heterogeneous    → can hold different types

# Key properties:
#   - Ordered       → position matters (t[0] ≠ t[1])
#   - Immutable     → cannot be modified after creation
#   - Allows duplicates
#   - Heterogeneous → can hold different types
#
# A tuple is not about "storage." It's about guarantees.
# When you use a tuple, you're saying:
# "This structure must never change — not by me, not by any function, not by accident."
# That's a design decision, not just a syntax choice.

t = (1, "hello", 3.14)
point = (10, 20)
rgb = (255, 128, 0)


# 2. Memory Model

# A tuple stores references (pointers) — same as a list.
# The difference: those references are locked after creation.
# You cannot add, remove, or replace them.

# ─────────────────────────────────────────────────────────────
#  HOW A TUPLE STORES DATA IN MEMORY
# ─────────────────────────────────────────────────────────────
#
#  t = (1, 2, 3)
#
#  Stack (names)        Heap (objects)
#  ┌──────────┐         ┌─────────────────────────────┐
#  │    t    ─┼────────►│  tuple object  (immutable)  │
#  └──────────┘         │  ┌──────┬──────┬──────┐     │
#                       │  │ ptr0 │ ptr1 │ ptr2 │     │
#                       │  └──┬───┴──┬───┴──┬───┘     │
#                       └─────┼──────┼──────┼─────────┘
#                             │      │      │
#                             ▼      ▼      ▼
#                           int(1) int(2) int(3)
#
#  The tuple does NOT contain 1, 2, 3.
#  It contains three pointers — and those pointers are frozen.
# ─────────────────────────────────────────────────────────────
#
#  ALIASING — b = a  (two names, one object — same as lists)
#
#  Stack                Heap
#  ┌───┐                ┌─────────────────────────┐
#  │ a ┼───────────────►│ tuple (ptr0, ptr1, ptr2)│
#  ├───┤                └─────────────────────────┘
#  │ b ┼───────────────►   (same object ↑)
#  └───┘
#
#  a is b  →  True
#  But since tuples are immutable, no method can mutate the shared object.
#  Aliasing is safe for tuples — unlike lists.
# ─────────────────────────────────────────────────────────────
#
#  MUTABLE CONTENTS TRAP
#
#  t = ([1, 2], [3, 4])
#
#  Stack                Heap
#  ┌───┐                ┌───────────────────────────┐
#  │ t ┼───────────────►│ tuple [ptr0, ptr1]        │
#  └───┘                └────┬──────────┬───────────┘
#                            │          │
#                            ▼          ▼
#                       [1, 2]        [3, 4]   ← mutable lists
#
#  t[0] = []    ❌  TypeError — can't change the slot (ptr0)
#  t[0][0] = 9  ✅  Allowed  — changes the list object ptr0 points to
#
#  The tuple's slots are frozen. What lives inside them is not.
# ─────────────────────────────────────────────────────────────

a = (1, 2, 3)
b = a
print(a is b)  # True — both names point to the same tuple object


# 3. Creating Tuples — Where People Get Sloppy

# Basic syntax
t = (1, 2, 3)

# Without parentheses — parentheses are optional (tuple packing):
t = 1, 2, 3

# The trap: single-element tuples
not_a_tuple = 1  # WRONG → this is just int
single = (1,)  # CORRECT → tuple
also_single = (1,)  # CORRECT → also a tuple

print(type(not_a_tuple))  # <class 'int'>
print(type(single))  # <class 'tuple'>
print(type(also_single))  # <class 'tuple'>

# Parentheses are not what define a tuple — commas are.
# That matters when reading real-world code.

empty = ()
from_iterable = tuple("abc")  # ('a', 'b', 'c')
from_range = tuple(range(5))  # (0, 1, 2, 3, 4)
print(f"From string: {from_iterable}")
print(f"From range:  {from_range}\n")


# 4. Accessing and Slicing

# Indices work exactly like lists — 0-based, negative indices count from the end.
# Slicing returns a new tuple — not a view.

t = (10, 20, 30, 40, 50)

print(t[0])  # 10
print(t[-1])  # 50
print(t[1:3])  # (20, 30) — new tuple
print(t[::-1])  # (50, 40, 30, 20, 10) — reversed

dimensions = (1920, 1080)
print(f"\nScreen resolution: {dimensions[0]} x {dimensions[1]}")

coordinates = ("Paris", 48.8566, 2.3522)
print(f"City: {coordinates[0]}")
print(f"Latitude: {coordinates[1]}")
print(f"Longitude: {coordinates[2]}\n")

planets = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
)
print(f"First planet: {planets[0]}")
print(f"Last planet:  {planets[-1]}")
print(f"Inner planets: {planets[:4]}")
print(f"Outer planets: {planets[4:]}\n")


# 5. Immutability — Stop Oversimplifying It

t = (1, 2, 3)
# t[0] = 10  # ❌ TypeError — the tuple slot is immutable

# But here's where weak understanding fails:
t = ([1, 2], [3, 4])
t[0][0] = 99  # ✅ This works — the list inside is still mutable
print(f"Mutable contents in a tuple: {t}")
# t[0] = []  # ❌ TypeError — can't replace the slot

# Tuple immutability applies to the REFERENCES, not the objects they point to.
# If you don't internalize this, you'll introduce bugs in state management.

config = (["debug", "verbose"], {"host": "localhost"})
config[0].append("trace")  # ✅ modifying the list inside
config[1]["port"] = "8080"  # ✅ modifying the dict inside
print(f"Config after mutation: {config}\n")


# 6. Tuple Packing and Unpacking — This Is Where Power Starts

# Packing — wrap multiple values into a tuple
coordinates = 48.8566, 2.3522
print(f"Packed coordinates: {coordinates}")

# Unpacking — extract values directly into variables
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Swap two variables without a temp variable:
x, y = 10, 20
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Extended unpacking — * collects the rest into a list
first, *rest = (1, 2, 3, 4, 5)
print(f"First: {first}, Rest: {rest}")  # rest is a list, not a tuple

head, *middle, last = ("a", "b", "c", "d", "e")
print(f"Head: {head}, Middle: {middle}, Last: {last}")

# Unpacking in a loop
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"  x={x}, y={y}")
print()

# Nested unpacking
record = ("Alice", (28, "Engineer"), "New York")
name, (age, role), city = record
print(f"Name: {name}, Age: {age}, Role: {role}, City: {city}\n")


# 7. Returning Multiple Values from Functions

# Python functions that "return multiple values" are actually returning one tuple.


def min_max(numbers):
    return min(numbers), max(numbers)  # returns a tuple


result = min_max([3, 1, 4, 1, 5, 9])
print(f"As tuple:       {result}")

low, high = min_max([3, 1, 4, 1, 5, 9])
print(f"Unpacked:       low={low}, high={high}")


def get_user():
    return "Alice", 30, "alice@example.com"


name, age, email = get_user()
print(f"User: {name}, age {age}, email {email}")


def divmod_custom(a, b):
    return a // b, a % b


quotient, remainder = divmod_custom(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}\n")


# 8. Tuples as Dictionary Keys — Hashability

# Dict keys must be hashable — their hash must never change.
# Tuples are hashable if all their contents are hashable.
# Lists are never hashable.

# ─────────────────────────────────────────────────────────────
#  WHAT IS A HASH?
#
#  A hash is a fixed-size integer computed from an object's value.
#  Python uses hashes to quickly locate dict keys and set members.
#
#    hash(42)      →  42
#    hash("hello") →  some large integer
#    hash((1, 2))  →  some integer
#    hash([1, 2])  →  ❌ TypeError: unhashable type: 'list'
#
#  Hashable  → immutable types: int, str, float, tuple
#  Unhashable → mutable types:  list, dict, set
#
#  If a list could be a dict key and you mutated it,
#  its hash would change and Python could never find it again.
#  So Python forbids it upfront.
# ─────────────────────────────────────────────────────────────

grid = {(0, 0): "origin", (1, 0): "right", (0, 1): "up"}
print(f"Grid at (0,0): {grid[(0, 0)]}")
print(f"Grid at (1,0): {grid[(1, 0)]}")

# Real-world: cache with a tuple key
cache = {}
cache[("fibonacci", 10)] = 55
cache[("fibonacci", 20)] = 6765
print(f"\nCache: {cache}")

# Graph adjacency using tuple keys
edges = {(1, 2): 5.0, (2, 3): 3.0, (1, 3): 8.0}
for (start, end), weight in edges.items():
    print(f"  Edge {start}→{end}: weight={weight}")
print()


# 9. Tuple Methods — Almost None (and that's intentional)

t = (1, 2, 3, 2, 4, 2)

# count(value) → int
# Returns the number of times value appears in the tuple.
print(f"count(2):    {t.count(2)}")  # 3
print(f"count(99):   {t.count(99)}")  # 0  — no error when value is absent

# index(value[, start[, stop]]) → int
# Returns the index of the FIRST occurrence of value within t[start:stop].
# Raises ValueError if not found (unlike list.count / str.find, there is no -1 fallback).
print(f"index(3):           {t.index(3)}")  # 2  — first position of 3
print(f"index(2):           {t.index(2)}")  # 1  — first 2 is at index 1
print(
    f"index(2, 2):        {t.index(2, 2)}"
)  # 3  — first 2 at or after index 2
print(
    f"index(2, 2, 5):     {t.index(2, 2, 5)}"
)  # 3  — first 2 in slice t[2:5]
# t.index(99)        # ❌ ValueError: tuple.index(x): x not in tuple
# t.index(2, 4, 5)   # ❌ ValueError: 2 not found in t[4:5] = (4,)

# Tuples intentionally have only these two methods.
# Fewer operations = fewer ways to break invariants.

seasons = ("spring", "summer", "autumn", "winter")
print(f"\nSeasons count: {len(seasons)}")
print(f"'summer' appears {seasons.count('summer')} time(s)")
print(f"'autumn' is at index {seasons.index('autumn')}")
print(f"'autumn' searched from index 1: {seasons.index('autumn', 1)}\n")


# 10. Iterating Over Tuples

dimensions = (200, 50, 75)
print("Dimensions:")
for d in dimensions:
    print(f"  {d}")
print()

foods = ("pizza", "falafel", "carrot cake", "ice cream", "cannoli")
print("Menu:")
for food in foods:
    print(f"  - {food.title()}")
print()

# Enumerate gives index + value:
players = ("Alice", "Bob", "Charlie", "Diana")
print("Team roster:")
for i, player in enumerate(players, start=1):
    print(f"  {i}. {player}")
print()

# Zip two tuples together:
names = ("Alice", "Bob", "Charlie")
scores = (95, 87, 92)
print("Leaderboard:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")
print()


# 11. Tuple Comprehension? No — Generator Expressions

# There is no tuple comprehension syntax.
# (x**2 for x in range(5)) is a generator, not a tuple.

gen = (x**2 for x in range(5))
print(f"Generator type: {type(gen)}")

# To get a tuple, wrap with tuple():
squares = tuple(x**2 for x in range(1, 6))
print(f"Squares tuple: {squares}")

evens = tuple(x for x in range(1, 11) if x % 2 == 0)
print(f"Even numbers:  {evens}\n")


# 12. Named Tuples — Readable Positional Data

# Regular tuple — position-based, unreadable:
p = (3, 4)
# p[0]? p[1]? No context.

# Named tuple — position + name:
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"Point: {p}")
print(f"x={p.x}, y={p.y}")
print(f"Still indexable: p[0]={p[0]}")
print(f"Still a tuple:   {isinstance(p, tuple)}")

Color = namedtuple("Color", ["red", "green", "blue"])
white = Color(255, 255, 255)
black = Color(0, 0, 0)
red = Color(255, 0, 0)
print(f"\nWhite: {white}")
print(f"Black: {black}")
print(f"Red:   {red.red}, Green: {red.green}, Blue: {red.blue}")

Employee = namedtuple("Employee", ["name", "department", "salary"])
engineers = [
    Employee("Alice", "Engineering", 120_000),
    Employee("Bob", "Engineering", 110_000),
    Employee("Charlie", "Engineering", 130_000),
]
print("\nEngineering team:")
for emp in engineers:
    print(f"  {emp.name}: ${emp.salary:,}")
print()


# 13. Performance Reality

# Tuples are:
#   - Faster to create than lists
#   - More memory-efficient
#   - Safer to share across code
#
# Why? Python can intern small tuples; no mutation tracking needed.
#
# But don't exaggerate: if performance is your only reason to use tuples,
# you're optimizing prematurely. The real reason is DATA INTEGRITY.

lst = [1, 2, 3, 4, 5]
tpl = (1, 2, 3, 4, 5)
print(f"List size:  {sys.getsizeof(lst)} bytes")
print(f"Tuple size: {sys.getsizeof(tpl)} bytes\n")


# 14. Why Tuples Exist — When Lists Are the Wrong Tool

# Use tuples when:

# 1. Data should not change
location = (48.8566, 2.3522)  # Paris — should never mutate

# 2. Fixed structure / meaning by position
user = ("Alice", 30, "alice@example.com")  # each index has a contract

# 3. Dictionary key
visited = {(48.8566, 2.3522): "Paris", (51.5074, -0.1278): "London"}

# 4. Returning multiple values from a function
# (see section 7)


# 5. Data integrity in APIs and pipelines
def process(record):
    # Caller cannot accidentally mutate what was passed in
    name, value = record
    return name.upper(), value * 2


result = process(("temperature", 36.6))
print(f"Processed: {result}")

print("\nVisited cities:")
for coords, city in visited.items():
    print(f"  {city} at {coords}")
print()


# 15. Common Mistakes

# Mistake 1: Using tuples when structure may evolve
user = ("Alice", 30)
# Later you want email → you've boxed yourself in.
# When your structure needs to grow, prefer a dataclass or dict.

# Mistake 2: Positional access on complex data
order = (123, "paid", 99.99)
# order[1] — what is this? Unreadable without context.
# Prefer: namedtuple("Order", ["id", "status", "total"])

# Mistake 3: Confusing immutability with deep safety
t = ([1, 2], [3, 4])
t[0].append(99)  # still works — tuple only locks its slots
print(f"Mutable contents modified: {t}")

# Mistake 4: Forgetting the trailing comma in single-element tuples
x = 42  # int, NOT a tuple
y = (42,)  # tuple ✅
print(f"type(42):  {type(x)}")
print(f"type(42,): {type(y)}\n")


# 16. When You Should NOT Use Tuples

# - If data evolves                  → use list or dataclass
# - If meaning isn't obvious         → use namedtuple or dataclass
# - If mutation is required          → tuple is the wrong tool
# - If you need sorting or filtering → list is more practical


# 17. Practical Examples

dimensions = (200, 50)
print(f"Width: {dimensions[0]}, Height: {dimensions[1]}")
# dimensions[0] = 250  # ❌ TypeError

# Reassigning is fine — you create a new tuple, not mutate the old:
dimensions = (250, 50)
print("\nUpdated dimensions:")
for d in dimensions:
    print(f"  {d}")

dimensions = (400, 100)
print("\nNew dimensions:")
for d in dimensions:
    print(f"  {d}")
print()

menu = ("pizza", "falafel", "carrot cake", "ice cream", "cannoli")
print("The restaurant offers:")
for item in menu:
    print(f"  - {item.title()}")
print()

# "Replacing" items by building a new tuple from slices:
updated_menu = ("sushi", "ramen") + menu[2:]
print("Updated menu:")
for item in updated_menu:
    print(f"  - {item.title()}")
print()

# Tuple of RGB colors
palette = (
    ("red", 255, 0, 0),
    ("green", 0, 200, 0),
    ("blue", 0, 0, 255),
)
print("Color palette:")
for name, r, g, b in palette:
    print(f"  {name.title()}: rgb({r}, {g}, {b})")
print()


# 18. zip, unzip, and zip_longest with Tuples

# ── Does zip belong to tuples? ─────────────────────────────────────────────
# zip() works with any iterable, but tuples are the natural output type
# when pairing structured, immutable records — coordinates, configs, DB rows.

# ── zip() ────────────────────────────────────────────────────────────
# zip() produces tuples — each element it yields is a tuple of one item
# from each iterable. It stops at the shortest.

cities = ("London", "Tokyo", "New York")
countries = ("UK", "Japan", "USA")

paired = list(zip(cities, countries))
print(f"Zipped: {paired}\n")  # [('London', 'UK'), ('Tokyo', 'Japan'), ...]

# Real world: pairing column names with row values from a database query.
columns = ("id", "username", "email")
row = (42, "alice", "alice@example.com")
record = dict(zip(columns, row))
print(f"DB record: {record}\n")

# Real world: iterating two tuples in parallel without index arithmetic.
latitudes = (51.5074, 35.6762, 40.7128)
longitudes = (-0.1278, 139.6503, -74.0060)
for city, (lat, lon) in zip(cities, zip(latitudes, longitudes)):
    print(f"  {city}: ({lat}, {lon})")
print()

# Zip three tuples at once:
names_t = ("Alice", "Bob", "Carol")
scores_t = (95, 87, 72)
grades_t = ("A", "B", "C")
for name, score, grade in zip(names_t, scores_t, grades_t):
    print(f"  {name}: {score} ({grade})")
print()

# ── unzip ────────────────────────────────────────────────────────────
# zip(*iterable) reverses a zip. No built-in unzip() exists — this IS the idiom.
# The * unpacks the list/tuple of pairs into individual arguments for zip().

pairs = (("London", "UK"), ("Tokyo", "Japan"), ("New York", "USA"))
cities_out, countries_out = zip(*pairs)
print(f"Cities:    {cities_out}")  # tuple
print(f"Countries: {countries_out}\n")  # tuple

# Real world: separating keys and values from a list of config tuples.
config_pairs = (("host", "localhost"), ("port", "5432"), ("db", "myapp"))
keys, values = zip(*config_pairs)
print(f"Config keys:   {keys}")
print(f"Config values: {values}\n")

# ── zip_longest ───────────────────────────────────────────────────────
# zip() silently drops extras when tuples differ in length.
# zip_longest keeps everything, filling missing positions with a default.

home_team = ("Alice", "Bob", "Carol")
guest_team = ("Dave", "Eve")  # one short
for h, g in zip_longest(home_team, guest_team, fillvalue="(bye)"):
    print(f"  {h} vs {g}")
print()

# ── Extended unpacking recap in a tuple context ────────────────────────
# * always collects into a list, even when unpacking a tuple.
# This is a deliberate Python design choice: the result is always mutable.

first, *rest = (10, 20, 30, 40)
print(
    f"first={first}, rest={rest}, type={type(rest).__name__}"
)  # rest is a list

head, *middle, last = ("a", "b", "c", "d", "e")
print(f"head={head}, middle={middle}, last={last}\n")

# Real world: consuming the first element of a pipeline result tuple,
# keeping the remainder for further processing.
status, *payload = (200, "user", "alice", "admin")
print(f"Status: {status}")
print(f"Payload fields: {payload}\n")


# 19. Mental Model Upgrade

# Stop thinking:  "Tuple = immutable list"
# Start thinking: "Tuple = fixed contract of values"
#
# A Python tuple is:
#   A fixed-length sequence of references, immutable slots,
#   hashable by default (if contents are hashable), and
#   designed to express a guarantee — not just save memory.
#
# That shift separates:
#   beginner code  → data thrown together
#   engineered code → data with invariants


# ──────────────────────────────────────────────
# Final Challenge (Don't skip this)
# ──────────────────────────────────────────────
# Answer these without running code:

# 1.
t = ([1, 2], [3, 4])
t[0].append(99)
print(t)
# What prints? Why?

# 2.
a = (1, 2, 3)
b = a
print(a is b)
# True or False? What does it mean?

# 3.
x = (5,)
y = 5
print(type(x), type(y))
# What are x and y?

# 4.
first, *rest = (10, 20, 30, 40)
print(first, rest)
# What is the type of rest?

# If any answer surprised you, re-read the section it tests.

# 12. Practical Examples

dimentions = (
    200,
    50,
)
print(dimentions[0])  # 200
print(dimentions[1])  # 50
# dimentions[0] = (
#     250  # ❌ TypeError: 'tuple' object does not support item assignment
# )

# Looping through all values in a tuple
for dimension in dimentions:
    print(dimension)

# Writing over a tuple is not allowed, but you can reassign the variable to a new tuple
dimentions = (250, 50)
print("\nOriginal dimensions:")
for dimension in dimentions:
    print(dimension)

dimentions = (400, 100)
print("\nModified dimensions:")
for dimension in dimentions:
    print(dimension)

foods = ("pizza", "falafel", "carrot cake", "ice cream", "cannoli")
print("\nThe restaurant offers the following five foods:")
for food in foods:
    print(food)

# foods[0] = (
#     "sushi"  # ❌ TypeError: 'tuple' object does not support item assignment
# )

replace_two_items_in_foods = (
    "sushi",
    "ramen",
    foods[2:],
)
print("\nModified menu:")
for food in replace_two_items_in_foods:
    if isinstance(food, tuple):
        for sub_food in food:
            print(sub_food)
    else:
        print(food)


# Packing — assign multiple values to one tuple without parentheses
point = 10, 20
color = 255, 128, 0
print(f"\nPacked point:  {point}")
print(f"Packed color:  {color}")

# Unpacking — extract tuple values directly into variables
x, y = point
r, g, b = color
print(f"Unpacked point: x={x}, y={y}")
print(f"Unpacked color: r={r}, g={g}, b={b}")

# Extended unpacking — * collects remaining values into a list
first, *rest = (10, 20, 30, 40)
print(f"\nfirst={first}, rest={rest}  # rest is a list, not a tuple")

head, *middle, last = (1, 2, 3, 4, 5)
print(f"head={head}, middle={middle}, last={last}")

# Swap without a temp variable (classic tuple pack/unpack in one line)
a, b = 100, 200
a, b = b, a
print(f"\nAfter swap: a={a}, b={b}")

# Unpacking in a loop
screen_sizes = [(1920, 1080), (2560, 1440), (3840, 2160)]
for width, height in screen_sizes:
    print(f"  {width}x{height}")


# Final Stress Test

# If you can't answer these instantly, your understanding isn't solid:

# 1. Why can a tuple be a dictionary key but a list cannot?
#    Dict keys must be hashable — their hash must never change. Tuples are immutable
#    so Python can compute a stable hash. Lists are mutable; their contents can change
#    at any time, making a stable hash impossible.
#
#    💡 What is a hash?
#    A hash is a fixed-size integer that represents an object's value, computed by a hash function.
#      hash(42)      → 42
#      hash("hello") → some large integer
#      hash((1, 2))  → some integer
#      hash([1, 2])  → ❌ TypeError: unhashable type: 'list'
#
#    Hashable means an object can produce a hash that never changes during its lifetime.
#    Python uses it to quickly locate dict keys and set members (like a filing system by number).
#    Immutable types are hashable: int, str, tuple, float
#    Mutable types are not: list, dict, set
#    If a list could be a dict key and you mutated it, its hash would change and Python
#    could never find it again — so Python forbids it upfront.
#
# 2. Why does (1) not create a tuple?
#    Parentheses are just grouping syntax. What defines a tuple is the comma.
#    (1) evaluates to int 1. The correct single-element tuple is (1,).
#
# 3. Why can a tuple still contain mutable data?
#    Tuple immutability applies only to the references it holds, not the objects
#    those references point to. The tuple's slots are frozen; what lives inside them is not.
#    t = ([1, 2], [3, 4]); t[0][0] = 99  # ✅ modifies the list, not the tuple's reference
#                          t[0] = []      # ❌ tries to change the tuple's slot — TypeError
#
# 4. When would a tuple be a bad design choice?
#    - When data needs to grow or change → use a list
#    - When position-based access is unreadable (order[2] — what is that?) → use a dataclass or dict
#    - When you need to sort, filter, or append → tuple has no methods for that
#    - When the structure needs named fields → namedtuple or dataclass is clearer
#    - When the structure needs to be immutable → use a tuple
