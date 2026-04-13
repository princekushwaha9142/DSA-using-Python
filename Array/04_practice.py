# Sum of Array

# Problem:
# Given an array of integers, find the sum of all elements.

# Input:

# n = 5
# arr = [1, 2, 3, 4, 5]

# Output:

# 15

def array_sum(arr):
    total = 0
    
    for num in arr:
        total += num
    
    return total

arr = [1, 2, 3, 4, 5]

print(array_sum(arr))  # 15