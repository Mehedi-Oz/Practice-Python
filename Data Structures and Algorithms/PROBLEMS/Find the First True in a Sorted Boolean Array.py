def first_true(arr):
    first = 0
    last = len(arr) - 1
    result = -1

    while first <= last:
        mid = (first + last) // 2

        if arr[mid]:
            result = mid
            last = mid - 1
        else:
            first = mid + 1

    return result


arr = [False, False, False, True, True, True]
print(f"Location: {first_true(arr)}")
