# What a Data Type Actually Is

# A data type answers three questions:

# These three questions form a mental model for truly understanding any type,
# not just memorizing syntax.

# ── 1. What values are allowed? ───────────────────────────────────────────────
# Every type has a valid range or set of values it can hold.
#   bool  → only True or False
#   int   → any whole number (no decimals, no size limit in Python)
#   str   → any sequence of Unicode characters
#   list  → any ordered collection of objects
# Putting an invalid value in either raises an error or silently coerces it.

# ── 2. What operations are valid? ────────────────────────────────────────────
# Each type supports a specific set of operations — knowing this prevents errors.

print("hello" + " world")  # ✅ string concatenation → ‘hello world’
print("hello" * 3)  # ✅ repetition           → ‘hellohellohello’
# "hello" - "h"             # ❌ TypeError: subtraction not defined for str

print([1, 2] + [3, 4])  # ✅ list concatenation   → [1, 2, 3, 4]
# [1, 2] + 3                # ❌ TypeError: can’t add int to list

# tuple has no .append() because it is immutable — different operations, different type.

# ── 3. How is it stored and used in memory? ───────────────────────────────────
# This determines performance and behaviour when values are passed around.
#
# Immutable types (int, str, tuple):
#   Once created the value in memory never changes.
#   Reassigning a variable just points it at a new object.
#
# Mutable types (list, dict, set):
#   The object in memory can be modified in-place.

a = [1, 2, 3]
b = a  # b points to the SAME list in memory
b.append(4)
print(a)  # [1, 2, 3, 4] — a changed too!

x = "hello"
y = x
y += " world"
print(x)  # ‘hello’ — x unchanged; y got a brand-new string object

# Practical consequence:
# Passing a list into a function CAN mutate the original.
# Passing an int into a function NEVER can.


# ── Numeric ──────────────────────────────────────────────────────────────────
integer = 42
negative = -7
big = 10**100  # Python ints have unlimited size

floating = 3.14
scientific = 1.5e-3  # 0.0015

complex_num = 2 + 3j
print(complex_num.real, complex_num.imag)  # 2.0  3.0

# ── String ─────────────────────────────────────────────────────────────────────
greeting = "Hello, World!"
multiline = """Line one
Line two"""

print(greeting.upper())  # HELLO, WORLD!
print(greeting[0:5])  # Hello
print(greeting.replace("World", "Python"))  # Hello, Python!

# ── Boolean ──────────────────────────────────────────────────────────────────
is_active = True
is_done = False

print(True + True)  # 2  (bool is a subclass of int)
print(int(False))  # 0

# ── List  (ordered, mutable, allows duplicates) ───────────────────────────────
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0] = "avocado"
print(fruits)  # ['avocado', 'banana', 'cherry', 'date']

# ── Tuple  (ordered, immutable) ───────────────────────────────────────────────
coordinates = (10.0, 20.0)
x, y = coordinates  # unpacking
print(x, y)  # 10.0  20.0

# ── Set  (unordered, no duplicates) ──────────────────────────────────────────
unique = {1, 2, 2, 3, 3, 3}  # pylint: disable=duplicate-value
print(unique)  # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # intersection → {2, 3}
print(a | b)  # union        → {1, 2, 3, 4}

# ── Dict  (key-value pairs, ordered since Python 3.7) ────────────────────────
person = {"name": "Alice", "age": 30}
person["city"] = "NY"  # add key
print(person["name"])  # Alice
print(person.get("missing", "default"))  # default

for key, value in person.items():
    print(f"{key}: {value}")  # results in:
# name: Alice
# age: 30
# city: NY

# ── NoneType ─────────────────────────────────────────────────────────────────
result = None
print(result is None)  # True

# ── Type checking & conversion ────────────────────────────────────────────────
print(type(42))  # <class 'int'>
print(isinstance(3.14, float))  # True

print(int("42"))  # 42
print(float(7))  # 7.0
print(str(100))  # '100'
print(list((1, 2, 3)))  # [1, 2, 3]
print(tuple([4, 5, 6]))  # (4, 5, 6)
print(set([1, 1, 2]))  # {1, 2}


# The Mistake Beginners Make

# They think:

# “Which data type should I use?”

# Wrong question.

# The real question is:

# What constraints does my data need?

# Example:
# If order matters → list/tuple
# If uniqueness matters → set
# If key-based lookup matters → dict
# If safety matters → tuple over list

# Answer this without guessing:

# ── Why can a tuple be used as a dict key but a list cannot? ─────────────────
# Dict keys must be hashable — Python computes a fixed hash to store/look up the key.
# tuple is immutable → contents never change → hash is stable → safe as a key.
# list  is mutable   → could change after use → hash would shift → dict can’t find it.

coords = (40.7, -74.0)
locations = {coords: "New York"}  # ✅ works
# tags = ["python", "backend"]
# data = {tags: "value"}            # ❌ TypeError: unhashable type: ‘list’

# Rule: mutable = unhashable = cannot be a dict key.

# ── Why is a list of dicts often a design smell in backend systems? ───────────
# users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
# Problems:
#   Lookup is O(n)   — finding id=99 scans the entire list.
#   No uniqueness    — two dicts with the same id coexist silently.
#   No schema        — one dict can have "name", another "username"; Python won’t complain.
#
# Better: index by the key you look up.

users = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
}
print(users[1])  # O(1) lookup, KeyError if missing — explicit and fast.

# ── When does a set outperform a list significantly? ─────────────────────────
# Membership testing:  x in collection
#   list → scans every element → O(n)
#   set  → computes hash, checks one slot → O(1)

haystack_list = list(range(100_000))
haystack_set = set(range(100_000))

print(99_999 in haystack_list)  # slow  — up to 100k comparisons
print(99_999 in haystack_set)  # instant — one hash lookup

# Use a set when: membership testing, deduplication, or fast union/intersection (&, |, -).
# Use a list when: order matters or duplicates are needed.
