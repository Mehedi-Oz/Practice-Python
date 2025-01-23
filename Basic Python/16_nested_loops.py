# for x in range(5):
#     for y in range(5):
#         print(f"X: {x}, Y: {y}")


numbers = [5, 2, 5, 2, 2]

for i in numbers:
    output = ""
    for j in range(i):
        output += "x"
    print(output)
