from dataclasses import dataclass


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


@dataclass
class Player:
    name: str


players = [Player(name='a'), Player(name='b'), Player(name='c')]


def duck_duck_goose(players: list[Player], position: int) -> str:
    index = (position - 1) % len(players)
    return players[index].name


# Example usage:
position = 4
goose = duck_duck_goose(players, position)
print(goose)  # Output: 'a'
