# dict = {"name": "hasan", "age": 20, "is_varified": True}

# print(dict["name"])

# dict["name"] = "Hasan"
# print(dict.get("Name", "Hasan"))
# print(dict)


# Q
# phone = input("Phone: ")

# dict_phone = {"1": "One", "2": "two", "3": "three"}
# output = ""

# for i in phone:
#     output += dict_phone.get(i, "!") + " "

# print(output)

# Q
message = input("> ")
messages = message.split(" ")

emoji = {":)": "XD", ":(": "-_-"}
output = ""

for item in messages:
    output += emoji.get(item, item) + " "

print(output)
