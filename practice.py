s = 'hello'
d = s[:]
print(s is d)  # True  — slicing a string returns the same object
print(s == d)  # True   — contents are the same
print(hash(s) == hash(d))  # True   — same contents → same hash
print(id(s), id(d))  # same memory addresses
print(id(s) == id(d))  # True  — same object in memory
