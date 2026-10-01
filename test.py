import random

print("Welcome to shop, what is your name?")
while True:
    command = input(">")
    characters = len(command)

    if characters >= 6:
        username = command
        print(f"Hello, {username}")
        break

    else:
        print("Username must be longer than 6 characters")

product_print = [
    "Sword = 5$, Shield = 10$, Armor = 20$, Health Potion = 2$ "]

print(f"Here are the wears for today: {product_print}")
while True:
    product_price = {"sword": 5, "shield": 10, "armor": 20, "health potion": 2}

    print("Do you want to buy? Y/N ")
    command = input(">")

    if command.lower() == "y":
        answer = input("What do you want to buy? ")

        if answer.lower() in product_price:
            while True:
                try:
                    amount = float(input("How many do you want? "))

                except ValueError:
                    print("Please type a valid number")

                else:
                    product = product_price[answer.lower()]
                    total_amount = amount * product
                    print(f"Total Amount is {total_amount}")
                    break

        else:
            print("We don't have that here")

    elif command.lower() == "n":
        print("Goodbye, Thanks for Shopping")
        break

    else:
        print("Please type Y/N")

animal_types = {"monkey": "mammal", "lizard": "reptile",
                "ostrich": "bird", "frog": "amphibian"}
animal_question = ["monkey", "lizard", "ostrich", "frog"]


def player_answer(expected_answer, expected_question):
    question = expected_question[random.randint(0, 3)]
    answer = expected_answer[question]

    print("Halt!, To get past this area you must answer this question.")
    print(f"What category does {question} belong to? ")
    while True:
        command = input(">")

        if command.lower() == answer:
            print("You are correct!, You shall pass")
            break

        else:
            print("You are incorrect! You shall not pass!")


player_answer(animal_types, animal_question)

print("Congratulations, You passed the quest")

for character in username[0:3]:
    print(character)
