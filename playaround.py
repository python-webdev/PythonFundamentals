# 1. What a Python String Actually Is

# In Python, strings are a data structure with behavior,
# constraints, and performance implications.

# A string in Python is a sequence of Unicode characters.

text = "Hello"

# Key implications you should not ignore:
#   - Ordered    → position matters (s[0] ≠ s[1])
#   - Immutable  → cannot be changed in-place
#   - Indexed    → you can access characters directly
#   - Iterable   → you can loop through it

# If you think of it as "just text," you'll miss how powerful—and dangerous—it is.

# 2. String Creation (More Subtle Than It Looks)
a = "Hello"
b = "Hello"
c = """Hello"""

# All valid—but:
# Single and double quotes are interchangeable
# Triple quotes are for multi-line strings
msg = """Line 1
Line 2
Line 3"""
# Escape Characters
quote = 'He said "Hello"'
path = "C:\\Users\\Name"

# If you don't understand escaping, your strings will silently break.

# 3. Immutability (This Will Bite You)
s = "hello"
# s[0] = "H"  # ❌ ERROR

# Strings cannot be modified.

# Instead:

s = "hello"
s = "H" + s[1:]
# Why this matters

# Every modification creates a new string in memory.

# So this is inefficient:

result = ""
for c in "hello":
    result += c

# Better:

result = "".join(["h", "e", "l", "l", "o"])

# If you ignore this, your code becomes slow without you realizing it.

# 4. Indexing and Slicing (Core Mechanics)
# Indexing
text = "Python"

text[0]  # 'P'
text[-1]  # 'n'
# Slicing
text[0:4]  # 'Pyth'
text[:4]  # 'Pyth'
text[2:]  # 'thon'
text[::-1]  # reverse

# If you can't slice confidently, you're not in control of string manipulation.

# 5. Iteration
for char in "Python":
    print(char)

# Strings behave like lists—but don't forget: you can't modify them during iteration.

# 6. Essential String Methods (Know These Cold)

# You don't "memorize everything"—you master patterns.

# Case Handling
"hello".upper()  # 'HELLO'
"HELLO".lower()  # 'hello'
"title case".title()  # 'Title Case'
# Cleaning Data
"  hello  ".strip()  # 'hello'
"hello\n".rstrip()  # 'hello'
# Searching
"text".find("e")  # index or -1
"text".index("e")  # index or ERROR

# If you don't know the difference between find and index, you will crash programs.

# Replace
"text".replace("t", "T")
# Splitting and Joining
"a,b,c".split(",")  # ['a', 'b', 'c']

"-".join(["a", "b", "c"])  # 'a-b-c'

# This is fundamental for data processing, APIs, and parsing.

# 7. String Formatting (Stop Using Old Methods)
# f-strings (modern, preferred)
name = "Murod"
age = 67

f"My name is {name} and I am {age}"
# format()
"My name is {} and I am {}".format(name, age)
# Why f-strings matter
# Faster
# Cleaner
# Easier to debug

# If you're still using %, you're outdated.

# 8. Membership Testing
"Py" in "Python"  # True
"Java" not in "Python"  # True

# This is how you validate input and parse logic efficiently.

# 9. String Comparison
"apple" == "apple"  # True
"apple" < "banana"  # True

# Comparison is lexicographical (dictionary order).

# This matters in sorting and validation.

# 10. Advanced Concepts You Should Not Ignore
# Unicode Awareness
len("é")  # 1

# But:

len("é")  # may be 2 (different representation)

# If you're building real systems (APIs, DBs), ignoring Unicode = bugs.

# Raw Strings
r"C:\Users\Name"  # pylint: disable=pointless-string-statement

# Critical for file paths and regex.

# Multiline + Formatting
name = "John"

text = f"""
Hello {name},
Welcome to Python.
"""
# 11. Performance Reality (Where Most Beginners Fail)

# This is inefficient:

s = ""
for i in range(10000):
    s += str(i)

# This is correct:

parts = []
for i in range(10000):
    parts.append(str(i))

s = "".join(parts)

# If you ignore this, your backend code will choke under load.

# 12. Strings in Real Backend Work

# You're not learning strings for toy examples.

# You'll use them for:
#   Parsing JSON
#   Building API responses
#   Handling user input
#   Logging
#   SQL queries (careful—SQL injection risk)

# Example:

user_input = "admin' OR 1=1 --"

# If you blindly inject this into SQL, you've just broken your system.

# Final Reality Check

# If you truly understand strings, you should be able to answer:
#   Why is string concatenation expensive?
#   When should you use join()?
#   What happens if Unicode is mishandled?
#   Why does immutability matter for concurrency and safety?

# If you can't answer those without guessing—you don't understand strings yet.
