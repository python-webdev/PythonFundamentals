# ──────────────────────────────────────────────
# Python Strings — A Rigorous, Practical Explanation
# ──────────────────────────────────────────────

from collections import defaultdict
from itertools import zip_longest

# In Python, strings are a data structure with behavior,
# constraints, and performance implications.

# 1. What a Python String Actually Is

# A Python string is:
#   - An ordered, immutable sequence of Unicode characters
#   - A first-class object with a rich method interface

# Key properties:
#   - Ordered    → position matters (s[0] ≠ s[1])
#   - Immutable  → cannot be modified in-place; every operation returns a NEW string
#   - Indexed    → you can access any character directly in O(1)
#   - Iterable   → you can loop through it character by character
#
# If you think "string = text," you're already missing what strings do in real systems.
# Python strings are Unicode sequences backed by an immutable byte buffer.


# 2. Memory Model (This is where most people make mistakes)

# A string does NOT store characters in a way you can mutate.
# Every "modification" creates a brand-new object on the heap.

# ─────────────────────────────────────────────────────────────
#  HOW A STRING IS STORED IN MEMORY
# ─────────────────────────────────────────────────────────────
#
#  s = 'hello'
#
#  Stack (names)        Heap (objects)
#  ┌──────────┐         ┌──────────────────────────────┐
#  │    s    ─┼────────►│  str object  'hello'         │
#  └──────────┘         │  len=5  hash=<cached>        │
#                       │  [h][e][l][l][o]             │
#                       └──────────────────────────────┘
#
#  s[0] = 'H'   ← TypeError — the buffer is read-only.
# ─────────────────────────────────────────────────────────────
#
#  REASSIGNMENT — s = s.upper()
#
#  Before:
#  Stack           Heap
#  ┌───┐           ┌────────────┐
#  │ s ┼──────────►│  'hello'   │
#  └───┘           └────────────┘
#
#  After:
#  Stack           Heap
#  ┌───┐           ┌────────────┐   ← still exists until GC
#  │   │           │  'hello'   │
#  │ s ┼──────────►│  'HELLO'   │   ← NEW object
#  └───┘           └────────────┘
#
#  s now points to the new string; the old one is garbage-collected.
# ─────────────────────────────────────────────────────────────
#
#  STRING INTERNING — Python may reuse identical string objects.
#
#  a = 'hello'
#  b = 'hello'
#  a is b  →  True  (CPython interns short, identifier-like strings)
#
#  Stack           Heap
#  ┌───┐           ┌────────────┐
#  │ a ┼──────────►│  'hello'   │◄──┐
#  ├───┤           └────────────┘   │
#  │ b ┼────────────────────────────┘
#  └───┘
#
#  This is an implementation detail — never rely on it for equality checks.
#  Always use == for value equality, not is.
# ─────────────────────────────────────────────────────────────

s = 'hello'
t = 'hello'
print(s == t)  # True   — same value
print(s is t)  # True   — CPython interns this (don't rely on it)

name = 'Alice'
name = name.upper()
print(name)  # 'ALICE' — a new string; the original 'Alice' is gone


# 3. Creating Strings

single = 'Hello, World!'
double = "Hello, World!"
triple_s = '''This spans
multiple lines'''
triple_d = """This also spans
multiple lines"""

raw = r'C:\Users\name\file.txt'  # raw: backslashes are literal
byte_str = b'bytes, not text'  # bytes literal (type: bytes, not str)
f_string = f'Value: {1 + 1}'  # f-string (evaluated at runtime)

# Embedding quotes:
quote_1 = 'He said "Hello"'
quote_2 = "It's a great day"
escaped = 'She said \'Hi\''
path = 'C:\\Users\\Name'  # \\ produces a single backslash

person = 'ada lovelace'
print(person.title())  # Ada Lovelace
print(person.upper())  # ADA LOVELACE
print(person.lower())  # ada lovelace

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)  # ada lovelace

message = f"Hello, {full_name.title()}!"
print(message)  # Hello, Ada Lovelace!

famous_person = 'albert einstein'
print(
    f"{famous_person.title()} once said, \"A person who never made a mistake never tried anything new.\""
)


# 4. Indexing & Slicing create new strings, but slicing a string returns the same object (if the slice is the whole string).

#
#  String:    H  e  l  l  o
#  Index:     0  1  2  3  4
#  Negative: -5 -4 -3 -2 -1

s = 'Hello'

print(s[0])  # 'H'     — first character
print(s[-1])  # 'o'     — last character
print(s[1:4])  # 'ell'   — slice [start:stop:step] (stop is exclusive)
print(s[:3])  # 'Hel'   — from beginning to index 3
print(s[2:])  # 'llo'   — from index 2 to end
print(s[::2])  # 'Hlo'   — every 2nd character (step)
print(s[::-1])  # 'olleH' — reversed string

language = 'Python'
print(language[0])  # 'P'
print(language[-1])  # 'n'
print(language[0:2])  # 'Py'
print(language[:3])  # 'Pyt'
print(language[3:])  # 'hon'
print(language[::-1])  # 'nohtyP'
print(language[::2])  # 'Pto'

greeting = 'Hello, World!'
print(greeting[7:12])  # 'World'
print(greeting[-6:-1])  # 'World'
print(greeting.index('W'))  # 7

# If you can't slice confidently, you're not in control of string manipulation.


# 5. Immutability

# Strings cannot be changed in-place; every operation returns a NEW string.

s = 'hello'
# s[0] = 'H'  ← TypeError: 'str' object does not support item assignment
s = s.replace('h', 'H')  # creates a new string 'Hello'
print(s)  # 'Hello'

# Every modification creates a new object:
word = 'python'
upper_word = word.upper()
print(word)  # 'python'  — unchanged
print(upper_word)  # 'PYTHON'  — new object

# Naive concatenation inside a loop is inefficient — O(n²):
result = ''
for c in 'hello':
    result += c  # creates a new string object on every iteration

# Prefer join() — allocates once:
result = ''.join(['h', 'e', 'l', 'l', 'o'])
print(result)  # 'hello'

# If you ignore this, your code becomes slow without you realizing it.


# 6. Concatenation & Repetition

greeting = 'Hello' + ', ' + 'World!'  # concatenation with +
repeated = 'ha' * 3  # 'hahaha'
print(greeting)
print(repeated)

# Efficient multi-part joining (preferred over many + operations):
words = ['Python', 'is', 'fun']
sentence = ' '.join(words)  # 'Python is fun'
print(sentence)

parts = ['id', 'name', 'email']
header = ' | '.join(parts)  # 'id | name | email'
print(header)

csv_line = ','.join(['Alice', '30', 'Engineer'])
print(csv_line)  # 'Alice,30,Engineer'


# 7. Whitespace in Strings

# Python uses \n for newlines, \t for tabs.
# strip(), lstrip(), rstrip() remove leading/trailing whitespace.

tabbed = '\tPython'
print(tabbed)  #     Python
newlined = 'Languages:\nPython\nJavaScript\nC++'
print(newlined)

favorite_language = '  Python  '
print(favorite_language.rstrip())  # '  Python'
print(favorite_language.lstrip())  # 'Python  '
print(favorite_language.strip())  # 'Python'

# Stripping is essential when processing user input — they always add spaces.


# 8. F-Strings (Formatted String Literals) — Python 3.6+

name = 'Alice'
score = 95.678

print(f'Name: {name}')  # Name: Alice
print(f'Score: {score:.2f}')  # Score: 95.68   (2 decimal places)
print(f'Upper: {name.upper()}')  # Upper: ALICE   (expressions allowed)
print(f'{"centered":^20}')  # aligned within 20 chars
print(f'2 + 2 = {2 + 2}')  # 2 + 2 = 4

first = 'john'
last = 'doe'
full = f'{first} {last}'
print(f"Hello, {full.title()}!")

# f-strings are faster, cleaner, and easier to debug than % or .format().
# If you're still using %, you're writing legacy code.


# 9. Common String Methods

s = '  Hello, Python World!  '

# --- Case ---
print(s.upper())  # "  HELLO, PYTHON WORLD!  "
print(s.lower())  # "  hello, python world!  "
print(s.title())  # "  Hello, Python World!  "
print(s.swapcase())  # "  hELLO, pYTHON wORLD!  "
print(s.capitalize())  # "  hello, python world!  " (only 1st char up)
print(
    s.casefold()
)  # "  hello, python world!  " (aggressive lower for caseless matching; handles ß → ss etc.)

# --- Whitespace ---
print(s.strip())  # "Hello, Python World!"   (both ends)
print(s.lstrip())  # "Hello, Python World!  " (left only)
print(s.rstrip())  # "  Hello, Python World!" (right only)

# --- Search, Replace & Transform ---
t = 'Hello, Python World!'
print(t.find('Python'))  # 7     (index of first match, -1 if not found)
print(t.rfind('l'))  # 18    (index of LAST match, -1 if not found)
print(
    t.index('Python')
)  # 7     (same as find, but raises ValueError if missing)
print(
    t.rindex('l')
)  # 18    (index of last match, raises ValueError if missing)

# find() vs index(): if you don't know the difference, you will crash programs.
# Use find() when absence is possible; use index() when absence is a bug.
# rfind() / rindex() search from the RIGHT — useful for file extensions, last occurrences.

print(t.count('l'))  # 3
print(t.replace('Python', 'Wonderful'))  # "Hello, Wonderful World!"
print(t.startswith('Hello'))  # True
print(t.endswith('!'))  # True

message = 'I really enjoyed the movie. It was fantastic!'
print(message.find('enjoyed'))  # 9
print(message.count('!'))  # 1
print(message.replace('fantastic', 'brilliant'))

# removeprefix() / removesuffix() — Python 3.9+
# Remove a specific prefix or suffix only if it is present (no-op otherwise).
filename = 'report_2024.pdf'
print(filename.removeprefix('report_'))  # '2024.pdf'
print(filename.removesuffix('.pdf'))  # 'report_2024'
print(filename.removeprefix('missing_'))  # 'report_2024.pdf' — unchanged

# translate() + maketrans() — map or delete individual characters in one pass.
# maketrans(x, y, z): x chars → y chars, z chars deleted.
table = str.maketrans('aeiou', '*****')  # replace vowels with *
print('Hello World'.translate(table))  # 'H*ll* W*rld'

del_table = str.maketrans('', '', 'aeiou')  # delete vowels
print('Hello World'.translate(del_table))  # 'Hll Wrld'

# Real-world use: ROT13-style ciphers, stripping punctuation, normalising text.

# --- Split & Join ---
csv = 'apple,banana,cherry'
fruits = csv.split(',')  # ['apple', 'banana', 'cherry']
rejoined = ' | '.join(fruits)  # 'apple | banana | cherry'
print(fruits)
print(rejoined)

# rsplit() splits from the RIGHT; the maxsplit argument limits how many splits occur.
path = 'home/user/documents/file.txt'
print(path.rsplit('/', 1))  # ['home/user/documents', 'file.txt']
print(path.rsplit('/', 2))  # ['home/user', 'documents', 'file.txt']

# partition() splits at the FIRST occurrence → (before, sep, after) — always a 3-tuple.
url = 'https://example.com/path'
before, sep, after = url.partition('://')
print(before, sep, after)  # 'https' '://' 'example.com/path'
print('no-sep'.partition('/'))  # ('no-sep', '', '')  — sep not found

# rpartition() does the same but at the LAST occurrence.
filepath = '/home/user/docs/report.pdf'
dir_part, _, filename = filepath.rpartition('/')
print(dir_part)  # '/home/user/docs'
print(filename)  # 'report.pdf'

multiline = 'line1\nline2\nline3'
lines = multiline.splitlines()  # ['line1', 'line2', 'line3']
print(lines)

sentence = 'The quick brown fox jumps over the lazy dog'
word_list = sentence.split()  # splits on any whitespace
print(len(word_list))  # 9
print(word_list[0])  # 'The'
print(word_list[-1])  # 'dog'

# This is fundamental for data processing, APIs, and parsing.

# --- Padding & Alignment ---
print('42'.zfill(5))  # '00042'   (zero-pad for numbers)
print('hi'.ljust(10, '-'))  # 'hi--------'
print('hi'.rjust(10, '-'))  # '--------hi'
print('hi'.center(10, '-'))  # '----hi----'

# expandtabs() replaces \t with spaces; default tabsize is 8.
print('col1\tcol2\tcol3'.expandtabs(10))  # 'col1      col2      col3'

label = 'Python'
print(f"{'Name':<10} {'Score':>10}")
print(f"{label:<10} {95.6:>10.2f}")

# --- Check / Validate ---
print('abc123'.isalnum())  # True  (all alphanumeric)
print('abc'.isalpha())  # True  (all alphabetic)
print('123'.isdigit())  # True  (all digits)
print(
    '123'.isnumeric()
)  # True  (digits + numeric chars like ² ③ — wider than isdigit)
print(
    '123'.isdecimal()
)  # True  (only 0-9 decimal digits — narrowest of the three)
print('   '.isspace())  # True  (all whitespace)
print('Hello World'.istitle())  # True  (title-cased)
print('HELLO'.isupper())  # True
print('hello'.islower())  # True
print('my_var_1'.isidentifier())  # True  (valid Python identifier)
print('hello\tworld'.isprintable())  # False (tab is not printable)
print('hello'.isprintable())  # True
print('hello'.isascii())  # True  (all chars within ASCII range 0-127)
print('café'.isascii())  # False (é is outside ASCII)

# isdecimal ⊂ isdigit ⊂ isnumeric — choose the narrowest check you need.

username = 'user_42'
print(username.isalpha())  # False — underscore is not alpha
print(username.replace('_', '').isalnum())  # True — after removing underscore


# 10. Escape Sequences

print('Line 1\nLine 2')  # newline
print('Col1\tCol2')  # tab
print('She said "Hi"')  # embedded double quote
print("It's fine")  # embedded single quote
print('Back\\slash')  # literal backslash
print('❤')  # Unicode character: ❤
print('A')  # Unicode: A  (code point 65)

# Raw strings — backslashes are literal, no escape processing:
windows_path = r'C:\Users\Name\Documents'
regex_pattern = r'\d{3}-\d{4}'
print(windows_path)
print(regex_pattern)

# If you forget r"", your Windows paths and regex patterns will silently break.


# 11. String Formatting Styles

name, age = 'Bob', 30

# f-string (modern, preferred):
print(f'{name} is {age} years old.')

# str.format() (older, still common):
print('{} is {} years old.'.format(name, age))
print('{name} is {age} years old.'.format(name=name, age=age))

# format_map() — like format(**mapping) but accepts any mapping object
# (useful with defaultdict or custom __missing__ to silently skip missing keys).
d = defaultdict(lambda: '<unknown>', name='Alice')
print(
    '{name} is {age} years old.'.format_map(d)
)  # 'Alice is <unknown> years old.'

# %-formatting (legacy, avoid in new code):
print('%s is %d years old.' % (name, age))

# Number formatting:
price = 1234567.89
print(f'{price:,.2f}')  # 1,234,567.89   (thousands separator)
print(f'{price:.0f}')  # 1234568         (rounded, no decimal)
print(f'{0.1234:.1%}')  # 12.3%           (percentage)
print(f'{255:#010x}')  # 0x000000ff      (hex, zero-padded)


# 12. Useful Built-in Functions on Strings

s = 'Python'

print(len(s))  # 6     — number of characters
print(ord('A'))  # 65    — Unicode code point of a character
print(chr(65))  # 'A'   — character from code point
print(str(3.14))  # '3.14' — convert any object to string
print(list(s))  # ['P','y','t','h','o','n'] — iterate characters
print(sorted(s))  # ['P','h','n','o','t','y'] — sorted characters
print('py' in s.lower())  # True — membership test (case-insensitive)
print('Py' in 'Python')  # True
print('Java' not in 'Python')  # True

book_title = 'the hitchhiker\'s guide to the galaxy'
print(len(book_title))
print(book_title.title())
print(book_title.upper())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(len(alphabet))  # 26
print(alphabet[0])  # 'a'
print(alphabet[-1])  # 'z'
print(alphabet[12])  # 'm'


# 13. Multiline Strings & Docstrings

address = """
123 Main Street
Springfield, IL 62701
USA
"""
print(address)


def greet(name):
    """Return a greeting string for the given name."""
    return f'Hello, {name}!'


poem = '''
Roses are red,
Violets are blue,
Python is great,
And so are you.
'''
print(poem)

# Multiline f-strings:
person_name = 'John'
person_age = 30
profile = f"""
Name:  {person_name}
Age:   {person_age}
Upper: {person_name.upper()}
"""
print(profile)


# 14. Iteration & Unpacking

# Strings behave like sequences — you can iterate character by character.

for ch in 'hello':
    print(ch, end=' ')  # h e l l o
print()

word = 'Python'
for i, ch in enumerate(word):
    print(f'[{i}] = {ch}')

# Unpacking works just like with lists:
first, *middle, last = 'Python'
print(first)  # 'P'
print(middle)  # 'ytho'
print(last)  # 'n'

# Building from iteration:
vowels = [ch for ch in 'Hello World' if ch.lower() in 'aeiou']
print(vowels)  # ['e', 'o', 'o']

consonants = [ch for ch in 'Python' if ch.lower() not in 'aeiou']
print(consonants)  # ['P', 't', 'h', 'n']


# 15. String Comparison

# Comparison is lexicographical (dictionary order), NOT by length.
# Case affects ordering: uppercase letters have lower code points than lowercase.

print('apple' == 'apple')  # True
print('apple' < 'banana')  # True  — 'a' comes before 'b'
print('b' > 'a')  # True
print('Z' < 'a')  # True  — ord('Z')=90, ord('a')=97
print('apple' == 'Apple')  # False — case-sensitive

# Case-insensitive comparison:
s1 = 'Python'
s2 = 'python'
print(s1.lower() == s2.lower())  # True

languages = ['Java', 'python', 'Go', 'Rust', 'c']
print(sorted(languages))  # ['Go', 'Java', 'Rust', 'c', 'python']
print(sorted(languages, key=str.lower))  # case-insensitive sort

# This matters in sorting, validation, and lookup logic.


# 16. Unicode Awareness

# Python strings are Unicode by default — but encoding can surprise you.

print(len('é'))  # 1  — single character in NFC form
print(ord('é'))  # 233

# The same visible character can have multiple byte representations (NFC vs NFD).
# In NFD, "é" is two code points: 'e' + combining accent → len() returns 2.
# If you're building real systems (APIs, DBs), ignoring Unicode = bugs.

emoji = '🐍'
print(len(emoji))  # 1  — Python 3 handles multi-byte Unicode correctly
print(ord(emoji))  # 128013

# Encoding to bytes and decoding back:
text = 'café'
encoded = text.encode('utf-8')  # b'caf\xc3\xa9'
decoded = encoded.decode('utf-8')  # 'café'
print(encoded)
print(decoded)

# Raw strings prevent escape processing — essential for file paths and regex:
pattern = r'C:\Users\Name'  # backslashes are literal
print(pattern)


# 17. Performance

# Because strings are immutable, += in a loop allocates a new string each time.

# Inefficient — O(n²) allocations:
s = ''
for i in range(1000):
    s += str(i)  # new string object on every iteration

# Correct — collect parts, join once:
parts = []
for i in range(1000):
    parts.append(str(i))
s = ''.join(parts)

# Same pattern with a generator expression (even more idiomatic):
s = ''.join(str(i) for i in range(1000))

# If you ignore this, your backend code will choke under load.
# 10,000 concatenations with += is the difference between 1ms and 100ms.


# 18. Subtle Pitfalls (You should recognise these instantly)

# Using is instead of == for string equality:
a = 'hello world'
b = 'hello world'
print(a == b)  # True  — always correct
print(a is b)  # implementation-dependent — do NOT use for equality checks

# Forgetting that split() without arguments splits on ANY whitespace:
line = '  hello   world  '
print(line.split())  # ['hello', 'world']  — strips edges, splits on runs
print(
    line.split(' ')
)  # ['', '', 'hello', '', '', 'world', '', '']  — no stripping

# Chaining methods returns a new string each time:
result = '  Hello, World!  '.strip().lower().replace(',', '').replace('!', '')
print(result)  # 'hello world'

# str.format() with missing keys raises KeyError:
template = '{name} is {age} years old.'
try:
    print(template.format(name='Alice'))  # KeyError: 'age'
except KeyError as e:
    print(f'Missing key: {e}')


# 19. Strings in Real-World Code

# Parsing input:
csv_row = 'Alice,30,Engineer'
name, age, role = csv_row.split(',')
print(f'{name} is a {role} aged {age}')

# Cleaning data:
raw_input = '   user@example.com   '
email = raw_input.strip().lower()
print(email)

# Validating:
pin = '1234'
print(pin.isdigit() and len(pin) == 4)  # True

# Validating email:
email = 'user@example'
print('@' in email and email.index('@') < email.index('.'))  # True

# Validating password:
password = 'abc123'
print(password.isalnum() and len(password) >= 8)  # True

# Validating username:
username = 'alice'
print(username.isalnum() and len(username) >= 3)  # True

# Validating credit card number:
card_number = '1234-5678-9012-3456'
print(
    card_number.replace('-', '').isdigit() and len(card_number) == 19
)  # True

# Validating phone number:
phone = '123-456-7890'
print(phone.replace('-', '').isdigit() and len(phone) == 12)  # True

# Validating post code:
post_code = 'ED1 1AA'
print(post_code.replace(' ', '').isalnum() and len(post_code) == 6)  # True

# Validating URL:
url = 'https://www.example.com'
print(url.startswith('https://') and url.endswith('.com'))  # True

# Validating IP address:
ip_address = '237.84.2.178'
print(ip_address.replace('.', '').isdigit() and len(ip_address) == 15)  # True

# Validating date:
date = '2022-01-01'
print(date.replace('-', '').isdigit() and len(date) == 8)  # True

# Validating time:
time = '12:34:56'
print(time.replace(':', '').isdigit() and len(time) == 8)  # True

# Validating currency:
currency = '$123.45'
print(
    currency.startswith('$') and currency[1:].replace('.', '').isdigit()
)  # True

# Validating social security number:
ssn = '123-45-6789'
print(ssn.replace('-', '').isdigit() and len(ssn) == 11)  # True

# Validating bank account number:
account_number = '1234567890'
print(account_number.isdigit() and len(account_number) == 10)  # True

# Validating ISBN:
isbn = '978-3-16-148410-0'
print(isbn.replace('-', '').isdigit() and len(isbn) == 13)  # True

# Validating credit card CVV:
cvv = '123'
print(cvv.isdigit() and len(cvv) == 3)  # True

# Validating driver's license:
license_number = 'D1234567'
print(
    license_number.startswith('D')
    and license_number[1:].isdigit()
    and len(license_number) == 8
)  # True

# If you ignore this, your backend code will choke under load.

# Strings in Real Backend Work

# You're not learning strings for toy examples.

# You'll use them for:
#   Parsing JSON
#   Building API responses
#   Handling user input
#   Logging
#   SQL queries (careful—SQL injection risk)

# SQL injection — the classic string danger:
user_input = "admin' OR 1=1 --"
# Never: query = "SELECT * FROM users WHERE name = '" + user_input + "'"
# Always use parameterized queries instead.

# If you blindly inject this into SQL, you've just broken your system.

# Building structured output:
fields = ['id', 'name', 'email']
header = ' | '.join(f'{f:<15}' for f in fields)
print(header)


# 20. Packing, Unpacking, and zip / unzip with Strings

# ── Does packing/unpacking belong to strings? ────────────────────────────
# Yes — strings are sequences too. Unpacking treats every character as one
# element, which is useful for short strings but can surprise you on longer ones.

# Basic unpack — character by character:
a, b, c = 'RGB'
print(f'Red channel code: {a}, Green: {b}, Blue: {c}\n')

# Extended unpack — same * mechanic as with lists:
# The starred variable always collects into a list of characters.
first, *middle, last = 'Python'
print(f'First: {first}')  # 'P'
print(f'Middle: {middle}')  # ['y', 't', 'h', 'o']
print(f'Last: {last}\n')  # 'n'

# Real world: parsing a fixed-width status code like "A12B".
status, *digits, flag = 'A12B'
print(f'Status flag: {status}, Digits: {digits}, End flag: {flag}\n')


# Packing — * spreads a string's characters into individual positional args:
def show_initials(first, middle, last):
    print(f'Initials: {first}.{middle}.{last}.')


show_initials(*'JFK')  # unpacks 'J', 'F', 'K' as three arguments
print()

# ── zip() with strings ────────────────────────────────────────────────────
# zip() treats a string as an iterable of characters — useful for pairing,
# aligning, or diffing two strings of equal length.

# Pairing characters from two strings:
plain = 'hello'
cipher = 'khoor'
for p, c in zip(plain, cipher):
    print(f'{p} → {c}', end='  ')
print()

# Real world: building a mapping dict from two equal-length strings.
keys = 'abcde'
values = '12345'
charmap = dict(zip(keys, values))
print(f'Char map: {charmap}\n')

# zip stops at the SHORTER string — watch out when strings differ in length:
short = 'hi'
long_ = 'hello'
pairs = list(zip(short, long_))
print(f'zip of unequal strings: {pairs}\n')  # only 2 pairs

# zip() with enumerate() for indexed character pairing:
word_a = 'spam'
word_b = 'eggs'
for i, (ca, cb) in enumerate(zip(word_a, word_b)):
    print(f'[{i}] {ca} vs {cb}')
print()

# ── unzip with strings ────────────────────────────────────────────────────
# zip(*iterable) reverses a zip — same idiom as with lists.

pairs = [('a', '1'), ('b', '2'), ('c', '3')]
letters, numbers = zip(*pairs)
print(f'Letters: {letters}')  # ('a', 'b', 'c')
print(f'Numbers: {numbers}\n')  # ('1', '2', '3')

# Reassemble into strings using join:
letters_str = ''.join(letters)
numbers_str = ''.join(numbers)
print(f'Letters string: {letters_str}')  # 'abc'
print(f'Numbers string: {numbers_str}\n')  # '123'

# ── zip_longest with strings ──────────────────────────────────────────────
# Use when strings have different lengths and you need to keep all characters.

word1 = 'cat'
word2 = 'elephant'
for c1, c2 in zip_longest(word1, word2, fillvalue='_'):
    print(f'{c1} | {c2}')
print()


# 21. Mental Model (If you remember nothing else)

# A Python string is:
#   An immutable sequence of Unicode characters with O(1) indexing,
#   a rich method interface, and a hidden allocation cost for mutations.
#
#   • Every "change" creates a new object — strings do not mutate.
#   • Use join() to build strings from many pieces, not +=.
#   • f-strings are the modern default for formatting.
#   • Slicing is powerful and safe — it always returns a new string.
#   • Raw strings are essential for regex patterns and file paths.
#
# If your mental model is weaker than this, you're guessing — not engineering.

# ──────────────────────────────────────────────
# Final Challenge (Don't skip this)
# ──────────────────────────────────────────────
# Answer this without running code:

s = 'Python'
result = s.replace('P', 'J').upper()[:3]
print(result)

# And this:
parts = ['hello', 'world']
out = ' '.join(parts).title()
print(out)

# If you had to think hard, you don't understand strings yet.

# ──────────────────────────────────────────────
# Summary
# ──────────────────────────────────────────────
#  • Strings are IMMUTABLE — every method returns a NEW string.
#  • Use f-strings for readable, expressive string formatting.
#  • Prefer .join() over + when building strings from many pieces.
#  • Slicing syntax [start:stop:step] is powerful and widely used.
#  • str.split() / str.strip() / str.replace() cover most parsing needs.
#  • Raw strings (r"...") are essential for regex patterns and file paths.
#  • find() returns -1 on miss; index() raises ValueError — choose deliberately.
#  • Comparison is lexicographical; Unicode encoding can change length/order.
#  • In loops, += on strings is O(n²); collect into a list and join() once.
#  • Never concatenate user input directly into SQL or shell commands.
#
# Reality check — if you truly understand strings, answer these without guessing:
#   - Why is string concatenation expensive in a loop?
#   - When should you use join()?
#   - What happens if Unicode is mishandled across encodings?
#   - Why does immutability matter for concurrency and safety?
