command = ""

while True:
    command = input("> ").lower()

    if command == "help":
        print(
            """
start - to start the car
stop - to stop the car
quit - to exit
          """
        )
    elif command == "start":
        print("Car Started!")
    elif command == "stop":
        print("Car Stopped!")
    elif command == "quit":
        break
    else:
        print("I dont understand!")
