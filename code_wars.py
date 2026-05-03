def sorter(text: list[str]) -> list[str]:
    return sorted(text, key=lambda x: x.lower())


# Example usage:
input_text = ["Banana", "apple", "Cherry", "date"]
sorted_text = sorter(input_text)
print(sorted_text)  # Output: ['apple', 'Banana', 'Cherry', 'date']


def remove_every_other(my_list: list) -> list:
    return my_list[::2]


# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
result = remove_every_other(input_list)
print(result)  # Output: [1, 3, 5]
