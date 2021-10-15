"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""

# [3, 4, 2, 1], 6 
def two_sum(nums, target):
    dictionary = {}

    for i in range(len(nums)):
        secondNum = target-nums[i]
        if secondNum in dictionary.keys():
            secondIdx = nums.index(secondNum)
            if i != secondIdx:
                return sorted([i, secondIdx])
        dictionary.update({nums[i]: i})




print(two_sum([2,5,9,13], 7))
print(two_sum([4,3,5], 8))
print(two_sum([3, 1, 2, 4], 6 ))