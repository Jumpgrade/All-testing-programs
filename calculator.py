operations = ""
command = input("Do you want to use the calculator? Y/N ")
while True:
    while not command.lower() == "n" and command.lower() == "y":
        if command.lower() == "y":
            try:
                number_1 = float(input("Please type the first number:"))
                number_2 = float(input("Please type the second number:"))
            except ValueError:
                print("Please Enter a Number")

            else:
                print("\nPlease type an operation")
                print("\nList of Operations")
                print("+, -, /, *")

                while True:
                    try:
                        operations = input(">")
                        if operations == "+":
                            print(number_1 + number_2)
                            command = input(
                                "Do you want to use the calculator again? Y/N ")
                            break

                        elif operations == "-":
                            print(number_1 - number_2)
                            command = input(
                                "Do you want to use the calculator again? Y/N ")
                            break

                        elif operations == "/":
                            print(number_1 / number_2)
                            command = input(
                                "Do you want to use the calculator again? Y/N ")
                            break

                        elif operations == "*":
                            print(number_1 * number_2)
                            command = input(
                                "Do you want to use the calculator again? Y/N ")
                            break

                        else:
                            print("Please type a valid operation")

                    except (ValueError, ZeroDivisionError):
                        print("Cannot divide by 0")

    if command.lower() == "n":
        print("Turning Off...")
        break

    else:
        print("Invalid Command, Please try again")
        if operations == "":
            command = input("Do you want to use the calculator? Y/N ")

        else:
            command = input("Do you want to use the calculator again? Y/N ")
