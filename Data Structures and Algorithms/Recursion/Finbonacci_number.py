# Not Efficient
import math


# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(6))


def fibo_formula(n):
    return int((1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** n))


print(fibo_formula(50))
