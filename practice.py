from dataclasses import dataclass


def invert(lst: list[int]) -> list[int]:
    return [-x for x in lst]


# Example usage:
numbers = [1, -2, 3, -4, 5]
inverted_numbers = invert(numbers)
print(inverted_numbers)  # Output: [-1, 2, -3, 4, -5]


# LeetCode problem: Two Sum
class Solution:  # pylint: disable=too-few-public-methods
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], index]

            num_to_index[num] = index

        return []  # This line is never reached since the problem guarantees a solution exists


# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]

# Example usage:
nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(result)  # Output: [1, 2]


@dataclass
class Player:
    name: str


players = [Player(name='a'), Player(name='b'), Player(name='c')]


def duck_duck_goose(players: list[Player], position: int) -> str:
    index = (position - 1) % len(players)
    return players[index].name
