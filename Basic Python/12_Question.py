weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")


if unit.upper() == "L":
    print(f"You are {float(weight) * 0.45} Kg!")
elif unit.upper() == "K":
    print(f"You are {float(weight) * 2.20462} Pounds!")
