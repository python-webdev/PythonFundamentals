from collections import Counter, defaultdict, namedtuple

# =============================================================================
# PYTHON DATA STRUCTURES — Comprehensive Guide
# =============================================================================
# Python provides four built-in collection types, each with distinct
# characteristics around mutability, ordering, and uniqueness.
#
#   | Type       | Ordered | Mutable | Duplicates | Syntax     |
#   |------------|---------|---------|------------|------------|
#   | list       | Yes     | Yes     | Yes        | [...]      |
#   | tuple      | Yes     | No      | Yes        | (...)      |
#   | dict       | Yes*    | Yes     | Keys: No   | {...: ...} |
#   | set        | No      | Yes     | No         | {...}      |
#
#   * dicts preserve insertion order since Python 3.7


# =============================================================================
# 1. LIST — Ordered, Mutable Sequence
# =============================================================================
# Use when you need an ordered collection that changes over time.

fruits = ["apple", "banana", "cherry"]

# --- Indexing & Slicing ---
print(fruits[0])        # "apple"   — zero-based index
print(fruits[-1])       # "cherry"  — negative index counts from end
print(fruits[0:2])      # ["apple", "banana"]  — slice [start:stop] (stop excluded)
print(fruits[::2])      # ["apple", "cherry"]  — slice with step [start:stop:step]

# --- Common Methods ---
fruits.append("date")           # add to end              → [..., "date"]
fruits.insert(1, "avocado")     # insert at index 1
fruits.remove("banana")         # remove first occurrence by value
popped = fruits.pop()           # remove & return last item
popped_at = fruits.pop(0)       # remove & return item at index 0
fruits.sort()                   # sort in-place (ascending)
fruits.sort(reverse=True)       # sort in-place (descending)
sorted_fruits = sorted(fruits)  # returns a NEW sorted list, original unchanged
fruits.reverse()                # reverse in-place
fruits.extend(["fig", "grape"]) # merge another iterable into the list
index = fruits.index("cherry")  # find index of first occurrence
count = fruits.count("cherry")  # count occurrences
fruits_copy = fruits.copy()     # shallow copy
fruits.clear()                  # remove all items

# --- List Comprehension — concise way to build lists ---
squares = [x ** 2 for x in range(1, 6)]          # [1, 4, 9, 16, 25]
evens   = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]
matrix  = [[i * j for j in range(1, 4)] for i in range(1, 4)]  # nested

# --- Unpacking ---
a, b, c = ["x", "y", "z"]
first, *rest = [1, 2, 3, 4, 5]   # first=1, rest=[2, 3, 4, 5]

# --- Useful Built-ins with Lists ---
numbers = [3, 1, 4, 1, 5, 9, 2]
print(len(numbers))     # 7     — number of items
print(min(numbers))     # 1     — smallest value
print(max(numbers))     # 9     — largest value
print(sum(numbers))     # 25    — sum of all values
print(list(enumerate(numbers)))   # [(0,3),(1,1),...] — index-value pairs
print(list(zip([1,2,3], ["a","b","c"])))  # [(1,"a"),(2,"b"),(3,"c")]


# =============================================================================
# 2. TUPLE — Ordered, Immutable Sequence
# =============================================================================
# Use for fixed collections of items (coordinates, DB rows, function returns).
# Immutability makes tuples hashable — they can be used as dict keys or set items.

point = (10, 20)
rgb   = (255, 128, 0)
single_item = (42,)         # trailing comma required for single-element tuple
empty_tuple = ()

# --- Indexing & Slicing (same as list) ---
print(point[0])         # 10
print(point[-1])        # 20
print(rgb[:2])          # (255, 128)

# --- Immutability ---
# point[0] = 99         # ← TypeError: tuples do not support item assignment

# --- Unpacking ---
x, y = point
lat, lon = 40.7128, -74.0060    # parentheses optional during assignment

# --- Named Tuple — tuple with field names (readable, memory-efficient) ---
Color = namedtuple("Color", ["red", "green", "blue"])
sky   = Color(red=135, green=206, blue=235)
print(sky.red)          # 135 — access by name
print(sky[0])           # 135 — still works by index
print(sky._asdict())    # OrderedDict of fields

# --- Tuple Methods ---
coords = (1, 2, 3, 2, 4, 2)
print(coords.count(2))  # 3   — number of occurrences
print(coords.index(3))  # 2   — index of first occurrence


# =============================================================================
# 3. DICTIONARY — Key-Value Map (Ordered since Python 3.7)
# =============================================================================
# Use when you need fast lookup by a meaningful key rather than a position.
# Keys must be hashable (strings, numbers, tuples). Values can be anything.

person = {
    "name":  "Alice",
    "age":   30,
    "email": "alice@example.com",
}

# --- Accessing Values ---
print(person["name"])               # "Alice" — raises KeyError if missing
print(person.get("phone"))          # None    — safe; no KeyError
print(person.get("phone", "N/A"))   # "N/A"  — default value when key absent

# --- Adding & Updating ---
person["city"] = "New York"         # add new key
person["age"]  = 31                 # update existing key
person.update({"age": 32, "country": "USA"})  # merge multiple keys at once

# --- Removing Items ---
del person["email"]                 # remove key (KeyError if missing)
city = person.pop("city")           # remove & return value
person.popitem()                    # remove & return last inserted (key, value)
person.clear()                      # empty the dict

# --- Iterating ---
config = {"host": "localhost", "port": 5432, "db": "myapp"}

for key in config:                          # iterates keys
    print(key)

for value in config.values():              # iterates values
    print(value)

for key, value in config.items():          # iterates (key, value) pairs
    print(f"{key} = {value}")

# --- Membership Test ---
print("host" in config)             # True  — checks keys
print("localhost" in config.values())  # True — checks values

# --- Dict Comprehension ---
squares_map  = {x: x**2 for x in range(1, 6)}         # {1:1, 2:4, 3:9, 4:16, 5:25}
filtered_map = {k: v for k, v in squares_map.items() if v > 4}  # {3:9, 4:16, 5:25}

# --- Merging Dicts (Python 3.9+) ---
defaults = {"color": "blue", "size": "medium"}
overrides = {"size": "large", "weight": "heavy"}
merged = defaults | overrides       # {"color":"blue","size":"large","weight":"heavy"}

# --- defaultdict — auto-initialises missing keys ---
word_count = defaultdict(int)       # missing key defaults to 0
for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
    word_count[word] += 1
print(dict(word_count))             # {"apple":3, "banana":2, "cherry":1}

groups = defaultdict(list)          # missing key defaults to []
for name, dept in [("Alice","Eng"),("Bob","HR"),("Carol","Eng")]:
    groups[dept].append(name)

# --- Counter — frequency counting ---
votes  = ["Alice","Bob","Alice","Alice","Bob","Carol"]
tally  = Counter(votes)
print(tally)                        # Counter({"Alice":3,"Bob":2,"Carol":1})
print(tally.most_common(2))         # [("Alice",3),("Bob",2)]


# =============================================================================
# 4. SET — Unordered Collection of Unique Items
# =============================================================================
# Use when uniqueness matters or when you need fast membership tests and
# mathematical set operations (union, intersection, difference).

colors = {"red", "green", "blue"}
empty_set = set()       # NOT {} — that creates an empty dict!

# --- Adding & Removing ---
colors.add("yellow")            # add one item (no effect if already present)
colors.update(["pink","white"]) # add multiple items from any iterable
colors.discard("purple")        # remove if present — NO error if missing
colors.remove("red")            # remove — raises KeyError if missing
popped_color = colors.pop()     # remove & return an arbitrary item

# --- Membership Test — O(1) average, faster than list ---
print("green" in colors)        # True
print("red" in colors)          # False (was removed)

# --- Set Operations ---
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)            # {1,2,3,4,5,6,7,8}  — union (all items)
print(a & b)            # {4, 5}              — intersection (common items)
print(a - b)            # {1, 2, 3}           — difference (in a, not in b)
print(b - a)            # {6, 7, 8}           — difference (in b, not in a)
print(a ^ b)            # {1,2,3,6,7,8}       — symmetric difference (not in both)

# --- Subset / Superset ---
print({4, 5}.issubset(a))       # True  — {4,5} ⊆ a
print(a.issuperset({4, 5}))     # True  — a ⊇ {4,5}
print(a.isdisjoint({6, 7}))     # True  — no common elements

# --- Set Comprehension ---
unique_squares = {x**2 for x in range(-3, 4)}   # {0, 1, 4, 9}

# --- frozenset — immutable set (hashable, usable as dict key) ---
immutable = frozenset([1, 2, 3])
lookup = {frozenset(["a","b"]): "group1", frozenset(["c","d"]): "group2"}


# =============================================================================
# 5. CHOOSING THE RIGHT DATA STRUCTURE
# =============================================================================
#
#   Need ordered, changeable collection with duplicates?  → list
#   Fixed data that shouldn't change / needs to be a key? → tuple
#   Fast lookup by name/key?                              → dict
#   Unique items / set math / fast membership test?       → set
#
# Performance at a glance (n = number of elements):
#
#   Operation              | list     | dict/set
#   -----------------------|----------|---------
#   Access by index        | O(1)     | N/A
#   Search (x in ...)      | O(n)     | O(1)*
#   Insert at end          | O(1)*    | O(1)*
#   Insert at beginning    | O(n)     | N/A
#   Delete by value        | O(n)     | O(1)*
#                                       * amortised average


# =============================================================================
# 6. NESTING & COMBINING STRUCTURES
# =============================================================================

# List of dicts — very common for tabular data / API responses
students = [
    {"name": "Alice", "grade": 90, "subjects": ["Math", "Science"]},
    {"name": "Bob",   "grade": 85, "subjects": ["English", "History"]},
]

top_students = [s["name"] for s in students if s["grade"] >= 90]

# Dict of lists — grouping
schedule = {
    "Monday":    ["Math", "Physics"],
    "Tuesday":   ["English", "History"],
    "Wednesday": ["Math", "Chemistry"],
}

# Dict of dicts — nested records / config trees
servers = {
    "web":  {"host": "10.0.0.1", "port": 80,   "active": True},
    "db":   {"host": "10.0.0.2", "port": 5432,  "active": True},
    "cache":{"host": "10.0.0.3", "port": 6379,  "active": False},
}
active_hosts = [cfg["host"] for cfg in servers.values() if cfg["active"]]
