"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # for n in nums: O(n)
    #     if nums.count(n) == 1: O(n)
    #         return n O(1)
    # O(n) * O(n) => O(n^2)
    my_dict = {}
    for n in nums:
        if n not in my_dict:
            my_dict[n] = 1
        else:
            my_dict[n] += 1
    
    for n in nums:
        if my_dict[n] == 1:
            return n



print(single_number([3,3,2]))
print(single_number([5,2,3,2,3]))
print(single_number([10]))