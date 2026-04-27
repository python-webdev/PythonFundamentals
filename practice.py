# miscellaneous = [
#     "fruit",
#     True,
#     42,
#     3.14,
#     [1, 2, 3],
#     {"key": "value"},
#     (4, 5),
#     {1, 2, 3},
#     None,
# ]

# print(miscellaneous[0].upper())
# print(miscellaneous[1].bit_length())
# print(miscellaneous[2].bit_length())
# print(miscellaneous[3].is_integer())
# miscellaneous[4].append(4)
# print(miscellaneous[4])
# print(miscellaneous[5]["key"])
# print(miscellaneous[6].count(4))
# miscellaneous[7].add(4)
# print(miscellaneous[7])
# print(miscellaneous[8] is None)


a = [1, 2, 3]
b = a
print(a is b)  # True, because a and b reference the same list object in memory
b.append(4)
print(
    a
)  # [1, 2, 3, 4], because a and b reference the same list object in memory
c = a.copy()
print(
    a is c
)  # False, because a and c reference different list objects in memory
c.append(5)
print(
    a
)  # [1, 2, 3, 4] because a and c reference different list objects in memory

d = a[:]
print(
    a is d
)  # False, because a and d reference different list objects in memory
d.append(6)
print(
    a
)  # [1, 2, 3, 4] because a and d reference different list objects in memory

pairs = [(1, "one"), (2, "two"), (3, "three")]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]

cars = ["Toyota", "Honda", "Ford", "BMW", "Audi"]
print(
    f"Original list: {cars}"
)  # Original list: ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi']
print(
    f"Temporary sorted list: {sorted(cars)}"
)  # Temporary sorted list: ['Audi', 'BMW', 'Ford', 'Honda', 'Toyota']
print(
    f"Original list: {cars}"
)  # Original list: ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi']
