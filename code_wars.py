def sorter(text: list[str]) -> list[str]:
    return sorted(text, key=lambda x: x.lower())


# Example usage:
input_text = ["Banana", "apple", "Cherry", "date"]
sorted_text = sorter(input_text)
print(sorted_text)  # Output: ['apple', 'Banana', 'Cherry', 'date']


def remove_every_other(my_list: list) -> list:
    # return my_list[::2]
    # return [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
    return [item for index, item in enumerate(my_list) if index % 2 == 0]


# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
result = remove_every_other(input_list)
print(result)  # Output: [1, 3, 5]


def count_positives_sum_negatives(lst: list[int]) -> list[int]:
    if not lst:
        return []
    positive_count = sum(1 for number in lst if number > 0)
    negative_sum = sum(number for number in lst if number < 0)
    return [positive_count, negative_sum]


# Example usage:
numbers = [1, -2, 3, -4, 5]
result = count_positives_sum_negatives(numbers)
print(result)  # Output: [3, -9]


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


# Example usage:
strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(result)  # Output: "fl"


def monkey_count(n: int) -> list[int]:
    return list(range(1, n + 1))


# Example usage:
n = 5
result = monkey_count(n)
print(result)  # Output: [1, 2, 3, 4, 5]


def two_highest(arg1: list[int]) -> list[int]:
    unique_numbers = set(arg1)
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[:2]


# Example usage:
numbers = [1, 2, 3, 4, 5, 5]
result = two_highest(numbers)
print(result)  # Output: [5, 4]


def square_sum(numbers: list[int]) -> int:
    return sum(x**2 for x in numbers)


# Example usage:
numbers = [1, 2, 3, 4, 5]
result = square_sum(numbers)
print(result)  # Output: 55


def alternative_square_sum(arr: list[int]) -> int:
    if not arr:
        return 0
    # even_positions_sum = sum(item for index, item in enumerate(arr) if index % 2 == 0)
    # odd_positions_sum = sum(item**2 for index, item in enumerate(arr) if index % 2 != 0)
    # return even_positions_sum + odd_positions_sum

    # even_positions_sum = sum(arr[i] for i in range(0, len(arr), 2))
    # odd_positions_sum = sum(arr[i] ** 2 for i in range(1, len(arr), 2))
    # return even_positions_sum + odd_positions_sum

    return sum(
        item**2 if index % 2 == 1 else item for index, item in enumerate(arr)
    )


# Example usage:
numbers = [1, 2, 3, 4, 5]
result = alternative_square_sum(numbers)
print(result)  # Output: 55
