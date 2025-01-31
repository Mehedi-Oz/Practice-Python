def recursion_function(nums, target, start, end):
    
    if start > end:
        return -1

    mid = (start + end) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return recursion_function(nums, target, start, mid - 1)
    elif nums[mid] < target:
        return recursion_function(nums, target, mid + 1, end)


nums = [1, 2, 3, 40, 54, 82, 90]
target = 82
print(f"Output: {recursion_function(nums, target, 0, len(nums)-1)}")
