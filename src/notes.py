# Runtime analysis
# Algorithm: A step-by-step progress to solve a program. Algorithms exist
# everywhere, even in your routine.
# input => steps = efficiency

# def print_number(n):
#     print(n)

# print(10)
# print(10000000)

# does the number of steps change? No. It's one step. Constant => It's O(1)

def print_many_items(n):
    for i in range(n):
        print(i)

print(print_many_items(5))
