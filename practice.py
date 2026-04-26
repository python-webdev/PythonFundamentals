miscellaneous = [
    "fruit",
    True,
    42,
    3.14,
    [1, 2, 3],
    {"key": "value"},
    (4, 5),
    {1, 2, 3},
    None,
]

print(miscellaneous[0].upper())
print(miscellaneous[1].bit_length())
print(miscellaneous[2].bit_length())
print(miscellaneous[3].is_integer())
miscellaneous[4].append(4)
print(miscellaneous[4])
print(miscellaneous[5]["key"])
print(miscellaneous[6].count(4))
miscellaneous[7].add(4)
print(miscellaneous[7])
print(miscellaneous[8] is None)
