name = input("Enter Your Name: ")
name_size = len(name)

if name_size < 3:
    print("Name must be at least 3 characters long!")
elif name_size > 50:
    print("Name can be at maximum of 50 characters!")
else:
    print("Name Looks Good!")
