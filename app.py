import random
agents = ["Omen", "Yoru", "Clove", "Chamber", "Sage", "Phoenix"]


while True:
    command = input("Do you want to pick an agent? Y/N  ")

    if command.lower() == "y":
        print(f"Your Agent is {agents[random.randint(0, 5)]}")
        command = input("Do you want to randomize again? Y/N ")
        if command.lower() == "n":
            print("Turning Off")
            break
        elif command.lower() == "y":
            print("Restarting")

    elif command.lower() == "n":
        print("Turning Off")
        break
    else:
        print("Invalid command, Please try again")
