# Runtime analysis
# Algorithm: A step-by-step progress to solve a program. Algorithms exist
# everywhere, even in your routine.
# input => steps = efficiency

# def print_number(n):
#     print(n)

# print(10)
# print(10000000)

# does the number of steps change? No. It's one step. Constant => It's O(1)

# def print_many_items(n):
#     for i in range(n):
#         print(i)

# print(print_many_items(5))
# print(print_many_items(50))

# the amount of steps increase by the amount of input. Linear => O(n)

# def print_many_items_twice(n):
#     for i in range(n):
#         print(i)
#         print(i)

# the amount of steps has doubled despite the input. O(2n). It's still linear time.
# There isn't much of a difference between these last two functions, we only care
# about the class (linear) time.

# another linear function O(n) where n is the length of the array

# def print_all_array_items(arr):
#   for item in arr:
#        print(item)

# def print_pairs(arr): Quadratic Time
#      count = 0
#     for item1 in arr: O(n)
#       for item2 in arr: O(n)
            # count += 1
            # print(item1, item2)
    # print(count)

# there's five inputs, five multiplied twice is 25. It's O(n2) This is the worse linear function you can write.

# print(print_pairs([1, 2, 3, 4, 5]))

# arrays are always O(1)

# def bunch_of_stuff(arr):
    # print(arr[0]) O(1)
#     print("Hello") O(1)
#     print(len(arr)) O(1)

#     for item in arr: O(n) it runs N times
#         print(item) O(1)
            # print("something") O(1)
# O(2) is the total runtime inside the loop
# it's O(2n) for this for loop
    
    # O(n) * O(n) => O(n^2)
#     for item1 in arr: O(n)
#         for item2 in arr: O(n)
#             print(item1, item2) O(1)

# How to get runtime:
# 1. Go line by line in code
# 2. Find out what that line's runtime will be
# 3. Go line by line inside a for loop
# 4. Add all lines up
# 5. multiply lines together to figure out runtime of for loop