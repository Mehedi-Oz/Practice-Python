def recursion_function(n):
    if n == 5:
        print(n)
        return

    print(n)
    recursion_function(n + 1)


recursion_function(1)
