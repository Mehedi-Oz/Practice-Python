def target_location(nums, target):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid = (first + last) // 2

        if nums[mid] > target:
            last = mid - 1
        elif nums[mid] < target:
            first = mid + 1
        else:
            return mid

    if nums[mid] < target:
        return mid + 1
    else:
        return mid


nums = [1, 3, 5, 6]
target = 7
print(f"Location: {target_location(nums, target)}")
