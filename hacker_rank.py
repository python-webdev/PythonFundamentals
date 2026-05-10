from typing import List, TypeVar

T = TypeVar("T", int, float)


def plusMinus(arr: List[T]) -> None:
    n = len(arr)
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)
    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n

    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


# Example usage:
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)

# Output:
# 0.500000
# 0.333333
# 0.166667

# Time complexity: O(n)
# Space complexity: O(1)

# Where n is the length of the input array.

# This code calculates the ratios of positive, negative, and zero elements in the input array. It iterates through the array three times to count the occurrences of each type of element, and then computes the ratios based on the total number of elements. Finally, it prints the ratios formatted to six decimal places.

# The time complexity is O(n), where n is the length of the input array, because we iterate through the array three times. The space complexity is O(1), since no additional data structures are used.


def miniMaxSum(arr: List[T]) -> None:
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)


# Example usage:
arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)

# Output:
# 10 14

# Time complexity: O(n log n) due to sorting
# Space complexity: O(1)
# This code calculates the minimum and maximum sums of four out of five integers in the input array. It first sorts the array, then computes the minimum sum by summing the first four elements and the maximum sum by summing the last four elements. Finally, it prints both sums.

# The time complexity is O(n log n), where n is the length of the input array, because we need to sort the array. The space complexity is O(1), since no additional data structures are used.


def timeConversion_12h_to_24h(s: str) -> str:
    period = s[-2:]
    hour = int(s[:2])
    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = hour if hour == 12 else hour + 12
    return f"{hour:02d}{s[2:-2]}"


# Example usage:
time_12h = "07:05:45PM"
time_24h = timeConversion_12h_to_24h(time_12h)
print(time_24h)  # Output: "19:05:45"

# Time complexity: O(1)
# Space complexity: O(1)
# This code converts a time string from 12-hour format to 24-hour format. It extracts the period (AM/PM) and the hour from the input string, then adjusts the hour based on the period. Finally, it formats the hour and the rest of the time string to return the time in 24-hour format.

# The time complexity is O(1), since we only iterate through the input string once. The space complexity is O(1), since no additional data structures are used.

# Note: The input string is expected to be in the format "hh:mm:ssAM/PM". If the input is not in this format, the function will raise a ValueError.


def breakingRecords(scores: List[T]) -> List[int]:
    if not scores:
        return [0, 0]

    min_score = max_score = scores[0]
    min_breaks = max_breaks = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_breaks += 1
        elif score < min_score:
            min_score = score
            min_breaks += 1

    return [max_breaks, min_breaks]


# Example usage:
scores = [12, 24, 10, 24]
result = breakingRecords(scores)
print(result)  # Output: [1, 1]

# Time complexity: O(n)
# Space complexity: O(1)
# This code counts how many times a player breaks their record for the highest and lowest scores in a game. It initializes the minimum and maximum scores to the first score in the list, then iterates through the scores to update the records and count the breaks. Finally, it returns a list containing the number of times the maximum and minimum records were broken.

# The time complexity is O(n), where n is the length of the input list. The space complexity is O(1), since no additional data structures are used.

# Note: The input list is expected to be non-empty. If the input list is empty, the function will return [0, 0] as a default value.
