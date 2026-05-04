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
