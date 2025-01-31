def peak_index(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start


arr = [0,2,1,0]
print(f"Outout: {peak_index(arr)}")
