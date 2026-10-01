import random
shapes = ["Triangle", "Circle", "Diamond", "Rectangle", "Banana"]


while True:
    print(f"Can you guess where the {shapes[random.randint(0, 4)]} goes?")
    command = input(">")

    if "hole" in command.lower():
        print("That's right it goes in the square hole.\n")

    else:
        print("Please include 'hole' in your answer")
