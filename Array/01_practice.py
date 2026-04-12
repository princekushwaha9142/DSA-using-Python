# Given a list of numbers, find the largest number WITHOUT using the max() function.

# Input: [3, 7, 1, 9, 4]
# Output: 9

def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    
    return largest

print(find_largest([3, 7, 1, 9, 4]))