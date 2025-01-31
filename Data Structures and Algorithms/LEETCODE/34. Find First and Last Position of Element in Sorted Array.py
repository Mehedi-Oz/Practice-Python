def binary_search(first, last, condition):
    while first <= last:
        mid = (first + last) // 2
        result = condition(mid)

        if result == "found":
            return mid
        elif result == "left":
            last = mid - 1
        elif result == "right":
            first = mid + 1
    return -1


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"
            return "found"
        elif nums[mid] > target:
            return "left"
        elif nums[mid] < target:
            return "right"

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return "right"
            return "found"
        elif nums[mid] > target:
            return "left"
        elif nums[mid] < target:
            return "right"

    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


nums = [5, 7, 7, 8, 8, 10]
target = 7
print(f"target Location: {first_and_last_position(nums, target)}")
