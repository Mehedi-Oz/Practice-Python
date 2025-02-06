def binary_search(first, last, arr, target):
    while first <= last:
        mid = (first + last) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return -1


def pivot_in_rotated_array(nums):
    first, last = 0, len(nums) - 1

    while first <= last:
        mid = (first + last) // 2

        if mid < last and nums[mid] > nums[mid + 1]:
            return mid
        elif mid > first and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[first] >= nums[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return -1


def target_search(nums, target):
    pivot = pivot_in_rotated_array(nums)

    if pivot == -1:
        return binary_search(0, len(nums) - 1, nums, target)
    elif nums[pivot] == target:
        return pivot
    elif target >= nums[0]:
        return binary_search(0, pivot - 1, nums, target)
    elif target < nums[0]:
        return binary_search(pivot + 1, len(nums) - 1, nums, target)


nums = [4,5,6,7,0,1,2]
target = 0
print(f"Index: {target_search(nums, target)}")