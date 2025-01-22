# i = 1

# while i <= 5:
#     print("*" * i)
#     i += 1

# print("DONE")

winning_guess = 3
count = 0

while count < 3:
    guess = input("Guess: ")
    count += 1
    if int(guess) == winning_guess:
        print("You Win!")
        break
else:
    print("You've failed!")
