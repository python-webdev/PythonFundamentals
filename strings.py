# =============================================================================
# PYTHON STRINGS — Comprehensive Guide
# =============================================================================
# A string is an immutable sequence of Unicode characters.
# Strings are one of Python's most-used built-in types.


# -----------------------------------------------------------------------------
# 1. CREATING STRINGS
# -----------------------------------------------------------------------------

single   = 'Hello, World!'
double   = "Hello, World!"
triple_s = '''This spans
multiple lines'''
triple_d = """This also spans
multiple lines"""

raw      = r"C:\Users\name\file.txt"   # raw: backslashes are literal
byte_str = b"bytes, not text"          # bytes literal (type: bytes, not str)
f_string = f"Value: {1 + 1}"          # f-string (evaluated at runtime)


# -----------------------------------------------------------------------------
# 2. INDEXING & SLICING
# -----------------------------------------------------------------------------
#
#  String:   H  e  l  l  o
#  Index:    0  1  2  3  4
#  Negative:-5 -4 -3 -2 -1

s = "Hello"

print(s[0])      # 'H'   — first character
print(s[-1])     # 'o'   — last character
print(s[1:4])    # 'ell' — slice [start:stop] (stop is exclusive)
print(s[:3])     # 'Hel' — from beginning to index 3
print(s[2:])     # 'llo' — from index 2 to end
print(s[::2])    # 'Hlo' — every 2nd character (step)
print(s[::-1])   # 'olleH' — reversed string


# -----------------------------------------------------------------------------
# 3. IMMUTABILITY
# -----------------------------------------------------------------------------
# Strings cannot be changed in place; operations return NEW strings.

s = "hello"
# s[0] = "H"   ← TypeError: 'str' object does not support item assignment
s = s.replace("h", "H")   # creates a new string "Hello"


# -----------------------------------------------------------------------------
# 4. CONCATENATION & REPETITION
# -----------------------------------------------------------------------------

greeting = "Hello" + ", " + "World!"   # concatenation with +
repeated = "ha" * 3                     # 'hahaha'

# Efficient multi-part joining (preferred over many + operations):
words = ["Python", "is", "fun"]
sentence = " ".join(words)              # 'Python is fun'


# -----------------------------------------------------------------------------
# 5. F-STRINGS (Formatted String Literals) — Python 3.6+
# -----------------------------------------------------------------------------

name  = "Alice"
score = 95.678

print(f"Name: {name}")                  # Name: Alice
print(f"Score: {score:.2f}")           # Score: 95.68  (2 decimal places)
print(f"Upper: {name.upper()}")        # Upper: ALICE  (expressions allowed)
print(f"{'centered':^20}")             # aligned within 20 chars


# -----------------------------------------------------------------------------
# 6. COMMON STRING METHODS
# -----------------------------------------------------------------------------

s = "  Hello, Python World!  "

# --- Case ---
print(s.upper())          # "  HELLO, PYTHON WORLD!  "
print(s.lower())          # "  hello, python world!  "
print(s.title())          # "  Hello, Python World!  "
print(s.swapcase())       # "  hELLO, pYTHON wORLD!  "
print(s.capitalize())     # "  hello, python world!  " (only 1st char up)

# --- Whitespace ---
print(s.strip())          # "Hello, Python World!"   (both ends)
print(s.lstrip())         # "Hello, Python World!  " (left only)
print(s.rstrip())         # "  Hello, Python World!" (right only)

# --- Search & Replace ---
t = "Hello, Python World!"
print(t.find("Python"))       # 7    (index of first match, -1 if not found)
print(t.index("Python"))      # 7    (same, but raises ValueError if missing)
print(t.count("l"))           # 3
print(t.replace("Python", "Wonderful"))   # "Hello, Wonderful World!"
print(t.startswith("Hello"))  # True
print(t.endswith("!"))        # True

# --- Split & Join ---
csv = "apple,banana,cherry"
fruits = csv.split(",")            # ['apple', 'banana', 'cherry']
rejoined = " | ".join(fruits)      # 'apple | banana | cherry'

multiline = "line1\nline2\nline3"
lines = multiline.splitlines()     # ['line1', 'line2', 'line3']

# --- Padding & Alignment ---
print("42".zfill(5))          # '00042'  (zero-pad)
print("hi".ljust(10, "-"))    # 'hi--------'
print("hi".rjust(10, "-"))    # '--------hi'
print("hi".center(10, "-"))   # '----hi----'

# --- Check / Validate ---
print("abc123".isalnum())     # True  (all alphanumeric)
print("abc".isalpha())        # True  (all alphabetic)
print("123".isdigit())        # True  (all digits)
print("   ".isspace())        # True  (all whitespace)
print("Hello".istitle())      # True  (title-cased)
print("HELLO".isupper())      # True
print("hello".islower())      # True


# -----------------------------------------------------------------------------
# 7. ESCAPE SEQUENCES
# -----------------------------------------------------------------------------

print("Line 1\nLine 2")       # newline
print("Col1\tCol2")           # tab
print("She said \"Hi\"")      # escaped double quote
print('It\'s fine')           # escaped single quote
print("Back\\slash")          # literal backslash
print("\u2764")               # Unicode character: ❤


# -----------------------------------------------------------------------------
# 8. STRING FORMATTING STYLES
# -----------------------------------------------------------------------------

name, age = "Bob", 30

# f-string (modern, preferred)
print(f"{name} is {age} years old.")

# str.format() (older, still common)
print("{} is {} years old.".format(name, age))
print("{name} is {age} years old.".format(name=name, age=age))

# %-formatting (legacy, avoid in new code)
print("%s is %d years old." % (name, age))


# -----------------------------------------------------------------------------
# 9. USEFUL BUILT-IN FUNCTIONS ON STRINGS
# -----------------------------------------------------------------------------

s = "Python"

print(len(s))           # 6   — number of characters
print(ord("A"))         # 65  — Unicode code point of a character
print(chr(65))          # 'A' — character from code point
print(str(3.14))        # '3.14' — convert any object to string
print(list(s))          # ['P','y','t','h','o','n'] — iterate characters
print(sorted(s))        # ['P','h','n','o','t','y'] — sorted characters
print("py" in s.lower()) # True — membership test (case-insensitive here)


# -----------------------------------------------------------------------------
# 10. MULTILINE STRINGS & DOCSTRINGS
# -----------------------------------------------------------------------------

address = """
123 Main Street
Springfield, IL 62701
USA
"""

def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


# -----------------------------------------------------------------------------
# 11. STRING UNPACKING & ITERATION
# -----------------------------------------------------------------------------

for ch in "abc":
    print(ch)           # 'a', then 'b', then 'c'

first, *middle, last = "Python"
print(first)   # 'P'
print(middle)  # ['y', 't', 'h', 'o']
print(last)    # 'n'


# -----------------------------------------------------------------------------
# 12. KEY TAKEAWAYS
# -----------------------------------------------------------------------------
#
#  • Strings are IMMUTABLE — every method returns a NEW string.
#  • Use f-strings for readable, expressive string formatting.
#  • Prefer .join() over + when building strings from many pieces.
#  • Slicing syntax [start:stop:step] is powerful and widely used.
#  • str.split() / str.strip() / str.replace() cover most parsing needs.
#  • Raw strings (r"...") are essential for regex patterns and file paths.
