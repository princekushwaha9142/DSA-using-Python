# find the smallest number without using min()

# Input:  [3, 7, 1, 9, 4]
# Output: 1

def find_smallest(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    return smallest

print(find_smallest([3, 7, 1, 9, 4]))
