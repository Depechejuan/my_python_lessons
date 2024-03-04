car = input("> ")

while car != "quit":
    if car == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
        car = input("> ")
    elif car == "start":
        print("Car has started! ..,")
        car = input("> ")
    elif car == "stop":
        print("Car has stopped!")
        car = input("> ")
    elif car == "quit":
        break
    else:
        print("I don't understand that...")
        car = input("> ")

print("Program finished")

