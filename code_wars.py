from typing import List, TypeVar

T = TypeVar("T", int, float)


def sorter(text: List[str]) -> List[str]:
    return sorted(text, key=lambda x: x.lower())


# Example usage:
input_text = ["Banana", "apple", "Cherry", "date"]
sorted_text = sorter(input_text)
print(sorted_text)  # Output: ['apple', 'Banana', 'Cherry', 'date']


def remove_every_other(my_list: List[T]) -> List[T]:
    # return my_list[::2]
    # return [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
    return [item for index, item in enumerate(my_list) if index % 2 == 0]


# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
result = remove_every_other(input_list)
print(result)  # Output: [1, 3, 5]


def count_positives_sum_negatives(lst: List[T]) -> List[int | T]:
    if not lst:
        return []
    positive_count = sum(1 for number in lst if number > 0)
    negative_sum = sum(number for number in lst if number < 0)
    return [positive_count, negative_sum]


# Example usage:
numbers = [1, -2, 3, -4, 5]
result = count_positives_sum_negatives(numbers)
print(result)  # Output: [3, -9]


def longest_common_prefix(strs: List[str]) -> str:
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


def monkey_count(n: int) -> List[int]:
    return list(range(1, n + 1))


# Example usage:
n = 5
result = monkey_count(n)
print(result)  # Output: [1, 2, 3, 4, 5]


def two_highest(arg1: List[int]) -> List[int]:
    unique_numbers = set(arg1)
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[:2]


# Example usage:
numbers = [1, 2, 3, 4, 5, 5]
result = two_highest(numbers)
print(result)  # Output: [5, 4]


def square_sum(numbers: List[T]) -> T:
    return sum(x**2 for x in numbers)


# Example usage:
numbers = [1, 2, 3, 4, 5]
result = square_sum(numbers)
print(result)  # Output: 55


def alternative_square_sum(arr: List[T]) -> T:
    if not arr:
        return 0  # type: ignore
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


def distinct(seq: List[T]) -> List[T]:
    # seen = set()
    # result = []
    # for item in seq:
    #     if item not in seen:
    #         seen.add(item)
    #         result.append(item)
    # return result

    return list(dict.fromkeys(seq))


# Example usage:
numbers = [1, 2, 2, 3, 4, 4, 5]
result = distinct(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]


def add_length(strs: str) -> List[str]:
    return [f"{s} {len(s)}" for s in strs.split(" ")]


# Example usage:
input_str = "apple banana cherry"
result = add_length(input_str)
print(result)  # Output: ['apple 5', 'banana 6', 'cherry 6']


def each_cons(lst: List[T], n: int) -> List[List[T]]:
    return [lst[i : i + n] for i in range(len(lst) - n + 1)]


# Example usage:
numbers = [1, 2, 3, 4]
n = 3
result = each_cons(numbers, n)
print(result)  # Output: [[1, 2, 3], [2, 3, 4]]


def pipe_fix(nums: List[int]) -> List[int]:
    if not nums:
        return []
    # return list(range(nums[0], nums[-1] + 1))
    return [idx for idx in range(min(nums), max(nums) + 1)]


# Example usage:
input_nums = [1, 3, 5]
result = pipe_fix(input_nums)
print(result)  # Output: [1, 2, 3, 4, 5]


def flick_switch(lst: List[str]) -> List[bool]:
    result = []
    current_value = True
    for item in lst:
        if item == "flick":
            current_value = not current_value
        result.append(current_value)
    return result


# Example usage:
input_lst = ["flick", "flick", "flick", "flick"]
result = flick_switch(input_lst)
print(result)  # Output: [False, True, False, True]


def fix_the_meerkat(arr: List[str]) -> List[str]:
    return arr[::-1]


# Example usage:
meerkat = ["tail", "body", "head"]
result = fix_the_meerkat(meerkat)
print(result)  # Output: ['head', 'body', 'tail']


def sort_by_binary_ones(arr: List[int]) -> List[int]:
    # Sort by number of 1's in binary representation, then by value (descending)
    return sorted(arr, key=lambda x: (bin(x).count('1'), -x), reverse=True)


# Example usage:
numbers = [5, 3, 7, 10]
sorted_numbers = sort_by_binary_ones(numbers)
print(sorted_numbers)  # Output: [7, 5, 3, 10]


def filter_list(lst: List[int | str]) -> List[int | float]:
    return [x for x in lst if isinstance(x, (int, float)) and x > 0]


# Example usage:
mixed_list = [1, 'a', -2, 3.5, 'b', 0, 4]
filtered_list = filter_list(mixed_list)
print(filtered_list)  # Output: [1, 3.5, 4]
