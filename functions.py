# ============================================================
#  PYTHON FUNCTIONS — COMPREHENSIVE EXPLANATION
# ============================================================
#
# A function is a named, reusable block of code that only runs
# when called. Functions let you write logic once and reuse it
# anywhere — the foundation of clean, maintainable code.
#
# Mental model:
#
#   define →  def greet(name):          ← parameters
#                 return f"Hi {name}"   ← return value
#   call   →  greet("Alice")            ← arguments
#
# ============================================================


# ------------------------------------------------------------
# 1. def KEYWORD
# ------------------------------------------------------------
# Use `def` to define a function.
# Syntax:  def function_name(parameters):
#
# - The colon `:` ends the function signature.
# - The indented block beneath is the function body.
# - Nothing runs until you CALL it by name with ().


def greet():
    print("Hello, World!")


greet()  # Hello, World!


# ------------------------------------------------------------
# 2. ARGUMENTS AND RETURN
# ------------------------------------------------------------
# Arguments pass data INTO a function.
# `return` sends data back OUT to the caller.
#
# Terminology:
#   - parameters → placeholders in the definition  (a, b)
#   - arguments  → actual values at call time       (3, 5)


def add(a, b):
    return a + b


result = add(3, 5)
print(result)  # 8


# A function without `return` implicitly returns None.
def say_hi(name):
    print(f"Hi, {name}!")


value = say_hi("Alice")  # Hi, Alice! pylint: disable=assignment-from-no-return
print(value)  # None


# ------------------------------------------------------------
# 3. DEFAULT ARGUMENTS
# ------------------------------------------------------------
# A parameter can have a fallback value used when the caller
# doesn't provide it.
#
# Rule: defaults must come AFTER non-default parameters.
#   def f(a=1, b): → SyntaxError — b has no default but follows one.


def power(base, exponent=2):
    return base**exponent


print(power(3))  # 9  — exponent defaults to 2
print(power(3, 3))  # 27 — exponent overridden to 3


# ------------------------------------------------------------
# 4. *args AND **kwargs
# ------------------------------------------------------------
# These allow a function to accept ANY NUMBER of arguments.
#
#   *args    — collects extra positional arguments → tuple
#   **kwargs — collects extra keyword arguments    → dict
#
# Combined order rule (always follow this):
#   def f(positional, *args, **kwargs)


def total(*args):
    return sum(args)  # args is a tuple


print(total(1, 2, 3, 4))  # 10


def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


profile(name="Bob", age=30, city="NY")
# name: Bob
# age: 30
# city: NY


# Both combined in one function:
def mixed(first, *args, **kwargs):
    print(first)  # first positional argument
    print(args)  # remaining positional arguments (tuple)
    print(kwargs)  # keyword arguments (dict)


mixed("hello", 1, 2, 3, color="blue", size=10)
# hello
# (1, 2, 3)
# {'color': 'blue', 'size': 10}


# ------------------------------------------------------------
# 5. LAMBDA FUNCTIONS
# ------------------------------------------------------------
# A lambda is a compact, anonymous function limited to a
# single expression.
# Syntax:  lambda parameters: expression
#
# Best used INLINE — as an argument to another function.
#
# Lambda vs def:
#   def      → has a name, multiple statements, explicit return
#   lambda   → anonymous, single expression, implicit return

# Sorting a list of tuples by the second element:
pairs = [(1, "banana"), (2, "apple"), (3, "cherry")]
pairs.sort(key=lambda item: item[1])
print(pairs)  # [(2, 'apple'), (1, 'banana'), (3, 'cherry')]

# Filtering a list with filter():
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

# Transforming a list with map():
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10, 12]
