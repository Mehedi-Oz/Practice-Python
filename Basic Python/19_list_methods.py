numbers = [3, 2, 4, 7, 8, 1, 1, 1]
numbers.append(100)
numbers.insert(0, 99)
# numbers.remove(1)
# numbers.clear()
# numbers.pop()

# print(numbers.index(1))
# print(3 in numbers)
# print(numbers)
# print(numbers.count(1))

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)

# numbers2 = numbers.copy()
# print(numbers2)


# Q

numList = [1, 4, 6, 2, 1, 6, 87, 6, 4, 4, 2, 7]
print(numList)
uniqueList = []

for item in numList:
  if item not in uniqueList:
    uniqueList.append(item)

print(uniqueList)