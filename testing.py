principal = -1
rate = 0
number_applied = 0
time = 0
command = ""


def solution(variable, minimum, type, wrong_response):
    while True:
        try:
            command = type(input(f"{variable}?: "))
        except ValueError:
            print("Please type a valid number")
        else:
            if command >= minimum:
                return command

            elif command < minimum:
                print(wrong_response)


print("Do you want to calculate your compound interest? Y/N: ")

while True:
    command = input(">")
    while not command.lower() == "n" and command.lower() == "y":
        if command.lower() == "y":
            principal = solution("What is your principal",
                                 0, float, "Principal can't be less than 0")

            rate = solution("What is your rate of interest", 0,
                            float, "Rate can't be less than 0")

            number_applied = solution(
                "how many times is interest applied in a year", 1, int, "Interest per year can't be less than or equal to 0")

            time = solution("how long is the interest plan", 1,
                            int, "Year can't be less than or equal to 0")

            total = principal * pow((1 + rate/100),
                                    (number_applied * time))

            print(f"Your total interest accumulated is: ${total:,.2f}")

            command = input(
                "Do you want to recalculate your compound interest? Y/N: ")
            break

    if command.lower() == "n":
        print("Turning Off...")
        break

    else:
        print("Invalid command, Please Try again")
        if principal == -1:
            print("Do you want to calculate your compound interest? Y/N: ")

        else:
            print("Do you want to recalculate your compound interest? Y/N: ")
