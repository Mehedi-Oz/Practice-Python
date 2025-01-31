# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/description/


def customer_wealth(accounts):
    max = 0
    row_value = 0

    for row in accounts:
        row_value = sum(row)
        print(len(row))

        if row_value > max:
            max = row_value

    return max


accounts =  [[]]
print(f"Richest Customer Wealth: {customer_wealth(accounts)}")