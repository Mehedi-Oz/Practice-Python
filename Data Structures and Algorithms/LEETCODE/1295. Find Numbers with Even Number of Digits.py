
# 1295. Find Numbers with Even Number of Digits
# (https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)


def finding_even_numbers(nums):
    total_even_numbers = 0

    for number in nums:
        if len(str(abs(number))) % 2 == 0:
            total_even_numbers += 1

    return total_even_numbers


nums = [0]
print(f"Total Even Numbers: {finding_even_numbers(nums)}")
print("Time Complexity is O(N) - Optimized Solution")


# 1295. Find Numbers with Even Number of Digits
# (https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)


def total_even_numbers(count):

    if count % 2 == 0:
        return 1

    return 0


def counting_digits(number):
    count = 0

    if number < 0:
        number = number * -1

    if number == 0:
        return 0
    else:
        while number > 0:
            count += 1
            number = number // 10

    return total_even_numbers(count)


def finding_even_numbers(nums):
    total_even_numbers = 0

    if len(nums) == 0:
        return 0
    else:
        for number in nums:
            total_even_numbers += counting_digits(number)

    return total_even_numbers


nums = [0]
print(f"Total Even Numbers: {finding_even_numbers(nums)}")
print("Time Complexity is O(N*M) / O(N * log₁₀(N)) - Unoptimized Solution")