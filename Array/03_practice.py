# Find the second largest number in a list.

# Input:  [3, 7, 1, 9, 4]
# Output: 7

def second_largest(nums):
    first = nums[0]
    second = None

    for num in nums:
        if num > first:
            second = first
            first = num
        
        elif second is None or num > second:
            if num !=first:
                second = num

    return second

print(second_largest([3, 7, 1, 9, 4]))