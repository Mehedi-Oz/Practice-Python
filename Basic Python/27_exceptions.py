try:
    age = int(input("Age: "))
    salary = 10000
    risk = salary / age
    print(age)
except ValueError:
    print("Invalid Value!")
except ZeroDivisionError:
    print("Age Cannot be 0!")
