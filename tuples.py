# ──────────────────────────────────────────────
# Python Tuples — A Rigorous, Practical Explanation
# ──────────────────────────────────────────────


# 1. What a Python Tuple Actually Is

# A Python tuple is:
#   - Ordered sequence → position matters (t[0] ≠ t[1])
#   - Immutable     → cannot change after creation
#   - Heterogeneous → can hold different types

t = (1, "hello", 3.14)

# A tuple is not about "storage." It's about guarantees.
# When you use a tuple, you're saying:
# "This structure must never change — not by me, not by any function, not by accident."
# That's a design decision, not just a syntax choice.


# 2. Tuple Creation — Where People Get Sloppy

# Basic syntax
t = (1, 2, 3)

# The trap: single-element tuples
t = 1  # WRONG → this is just int
t = (1,)  # CORRECT → tuple

# Parentheses are not what define a tuple — commas are.
# Without parentheses (tuple packing):
t = 1, 2, 3

# That matters when reading real-world code.


# 3. Immutability — Stop Oversimplifying It

t = (1, 2, 3)
# t[0] = 10  # ❌ TypeError — the tuple reference is immutable

# But here's where weak understanding fails:
t = ([1, 2], [3, 4])
t[0][0] = 99  # ✅ This works — the list inside is still mutable

# Tuple immutability applies to the REFERENCES, not the contents.
# If you don't internalize this, you'll introduce bugs in state management.


# 4. Accessing and Slicing

t = (10, 20, 30, 40)

t[0]  # 10
t[-1]  # 40
t[1:3]  # (20, 30) — returns a NEW tuple; even slicing respects immutability


# 5. Tuple Packing and Unpacking — This Is Where Power Starts

# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t

# Extended unpacking
a, *rest = (1, 2, 3, 4)
# a = 1, rest = [2, 3, 4]
# Note: rest becomes a list, not a tuple — Python optimizes for flexibility here.


# 6. Why Tuples Exist (And When Lists Are Wrong)

# Use tuples when:

# 1. Data should not change
point = (10, 20)  # coordinates should not randomly mutate

# 2. Fixed structure / meaning by position
user = ("Murod", 67, "Developer")  # each index has a contractual meaning

# 3. As dictionary keys (critical)
d = {(10, 20): "Point A"}
# [10, 20]  # ❌ unhashable — lists cannot be dict keys
# Tuples are hashable (if their contents are). This matters in:
# caching, memoization, graph problems, coordinate systems.


# 4. Returning multiple values from functions
def stats():
    return 10, 20, 30  # implicitly returns a tuple


a, b, c = stats()


# 7. Tuple Methods — Almost None (and that's intentional)

t = (1, 2, 3, 2)

t.count(2)  # 2  — count occurrences
t.index(3)  # 2  — find position

# Compare with lists — dozens of methods.
# Fewer operations = fewer ways to break invariants.


# 8. Performance Reality
# Tuples are:
#   - Faster to create
#   - More memory efficient
#   - Safer to share across code
#
# Why? No need to track mutations; simpler internal structure.
#
# But don't exaggerate: if performance is your only reason to use tuples,
# you're optimizing prematurely. The real reason is DATA INTEGRITY.


# 9. Common Mistakes

# Mistake 1: Using tuples when structure may evolve
user = ("Murod", 67)
# Later you want email → you've boxed yourself in.

# Mistake 2: Using positional tuples for complex data
order = (123, "paid", 99.99)
# What is order[1]? Unreadable.
# Prefer: dataclass, dict, or a domain model.

# Mistake 3: Confusing immutability with safety
t = ([1, 2], [3, 4])
# Still mutable internally — don't rely on tuples blindly for "security."


# 10. When You Should NOT Use Tuples

# - If data evolves         → use list or object
# - If meaning isn't obvious → use a named structure
# - If mutation is required  → tuple is the wrong tool


# 11. Mental Model Upgrade

# Stop thinking:  "Tuple = immutable list"
# Start thinking: "Tuple = fixed contract of values"
#
# That shift separates:
#   beginner code  → data thrown together
#   engineered code → data with guarantees


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


# Final Stress Test

# If you can't answer these instantly, your understanding isn't solid:
#
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
