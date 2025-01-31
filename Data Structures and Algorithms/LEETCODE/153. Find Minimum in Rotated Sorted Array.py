def find_minimum(nums):
    first, last = 0, len(nums) - 1

    while first < last:
        mid = (first + last) // 2

        if nums[mid] > nums[last]:
            first = mid + 1
        else:
            last = mid

    return nums[last]


nums = [11,13,15,17]
print(f"Outout: {find_minimum(nums)}")
