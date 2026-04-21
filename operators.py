# ─────────────────────────────────────────────
# 1. ARITHMETIC OPERATORS
# ─────────────────────────────────────────────
a, b = 10, 3

print(a + b)   # 13  — addition
print(a - b)   # 7   — subtraction
print(a * b)   # 30  — multiplication
print(a / b)   # 3.333... — true division (always float)
print(a // b)  # 3   — floor division (drops the decimal)
print(a % b)   # 1   — modulus (remainder)
print(a ** b)  # 1000 — exponentiation (10³)


# ─────────────────────────────────────────────
# 2. COMPARISON OPERATORS  →  always return bool
# ─────────────────────────────────────────────
x, y = 5, 8

print(x == y)  # False — equal
print(x != y)  # True  — not equal
print(x >  y)  # False — greater than
print(x <  y)  # True  — less than
print(x >= y)  # False — greater than or equal
print(x <= y)  # True  — less than or equal


# ─────────────────────────────────────────────
# 3. LOGICAL OPERATORS  →  combine conditions
# ─────────────────────────────────────────────
t, f = True, False

print(t and f)  # False — both must be True
print(t or  f)  # True  — at least one must be True
print(not t)    # False — flips the boolean

# practical example
age = 20
has_id = True
print(age >= 18 and has_id)  # True


# ─────────────────────────────────────────────
# 4. MEMBERSHIP OPERATORS  →  check containment
# ─────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]

print("apple"  in     fruits)  # True
print("grape"  in     fruits)  # False
print("grape"  not in fruits)  # True

# works on strings too
print("py" in "python")  # True


# ─────────────────────────────────────────────
# 5. IDENTITY OPERATORS  →  check same object in memory
# ─────────────────────────────────────────────
p = [1, 2, 3]
q = p          # q points to the SAME list
r = [1, 2, 3]  # r is an EQUAL but DIFFERENT list

print(p is  q)      # True  — same object
print(p is  r)      # False — different objects, even though equal
print(p is not r)   # True

# tip: use == to compare values, use is only for None / singletons
value = None
print(value is None)  # True  ✓ (preferred over value == None)
