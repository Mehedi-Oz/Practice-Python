def returnEmoji(message):
    messages = message.split(" ")

    emoji = {":)": "XD", ":(": "-_-"}
    output = ""

    for item in messages:
        output += emoji.get(item, item) + " "

    return output


message = input("> ")
print(returnEmoji(message))
