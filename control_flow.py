# ============================================================
# CONTROL FLOW IN PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. if / elif / else
# ------------------------------------------------------------
# Python evaluates conditions top-to-bottom and runs the first
# block whose condition is True. The else block is a catch-all.

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)  # C


# Conditions can use: ==  !=  <  >  <=  >=  and  or  not  in
temperature = 35
raining = False

if temperature > 30 and not raining:
    print("Great beach day!")
elif temperature > 30 and raining:
    print("Hot but rainy.")
else:
    print("Stay indoors.")


# One-liner (ternary) — only for simple cases
status = "adult" if score >= 18 else "minor"


# ------------------------------------------------------------
# 2. match-case  (Python 3.10+)
# ------------------------------------------------------------
# Like a switch statement, but more powerful.
# Python checks each case pattern in order and runs the first match.

command = "quit"

match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":       # OR patterns with |
        print("Stopping.")
    case "help":
        print("Available commands: start, stop, quit, help")
    case _:                     # _ is the wildcard / default
        print(f"Unknown command: {command}")


# --- Matching on types and structure ---

point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):                # captures y from the tuple
        print(f"On Y-axis at y={y}")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")


# --- Matching dictionaries ---

response = {"status": 200, "body": "OK"}

match response:
    case {"status": 200, "body": body}:
        print(f"Success: {body}")
    case {"status": 404}:
        print("Not found")
    case {"status": status}:
        print(f"Unexpected status: {status}")


# --- Guard clauses (adding extra conditions with `if`) ---

number = 42

match number:
    case n if n < 0:
        print("Negative")
    case n if n % 2 == 0:
        print(f"{n} is even")
    case n:
        print(f"{n} is odd")


# ------------------------------------------------------------
# Key differences at a glance
# ------------------------------------------------------------
# if/elif/else  → general boolean conditions, any Python expression
# match-case    → structural pattern matching on a single value/object
#                 cleaner when branching on shapes, types, or literals
