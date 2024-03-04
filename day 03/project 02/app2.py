command = ""
status = "stopped"
while True:
    command = input("> ").lower()
    if command == "start":
        if status == "running":
            print("Car is already running...")
        else: 
            print("Car started...")
            status = "running"
    elif command == "stop":
        if status == "stopped":
            print("Car is already stopped")
        else:
            print("Car stopped.")
            status = "stopped"
    elif command == "help":
        print("""start - to start the car 
stop - to stop the car
quit - to exit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")

# YT uses a bool for "status", and on stop use condition "if not started"