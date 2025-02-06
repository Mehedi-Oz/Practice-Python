# 410. Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/description/


def largest_sum(nums, k):
    start = max(nums)
    end = sum(nums)

    while start < end:
        mid = (start + end) // 2

        current_sum = 0
        pieces = 1

        for num in nums:
            if current_sum  + num > mid:
                current_sum  = num
                pieces += 1
            else:
                current_sum  += num

        if pieces > k:
            start = mid + 1
        else:
            end = mid

    return end


nums = [7, 2, 5, 10, 8]
k = 2
print(largest_sum(nums, k))