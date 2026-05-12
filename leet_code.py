# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from typing import List, TypeVar

T = TypeVar("T", int, float)


class Solution:
    def twoSum(self, nums: List[T], target: T) -> List[int]:

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


def duck_duck_goose(players: List[Player], position: int) -> str:
    index = (position - 1) % len(players)
    return players[index].name


# Example usage:
position = 4
goose = duck_duck_goose(players, position)
print(goose)  # Output: 'a'


class MergeSolution:
    def merge(self, nums1: List[T], m: int, nums2: List[T], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        print(nums1)


# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge_solution = MergeSolution()
merge_solution.merge(nums1, m, nums2, n)  # Output: [1, 2, 2, 3, 5, 6]


class RemoveElementSolution:
    def removeElement(self, nums: List[T], val: T) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Example usage:
nums = [3, 2, 2, 3]
val = 3
remove_element_solution = RemoveElementSolution()
new_length = remove_element_solution.removeElement(nums, val)
print(new_length)  # Output: 2
print(nums[:new_length])  # Output: [2, 2]


class RemoveDuplicatesSolution:
    def removeDuplicates(self, nums: List[T]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Example usage:
nums = [1, 1, 2]
remove_duplicates_solution = RemoveDuplicatesSolution()
new_length = remove_duplicates_solution.removeDuplicates(nums)
print(new_length)  # Output: 2
print(nums[:new_length])  # Output: [1, 2]
