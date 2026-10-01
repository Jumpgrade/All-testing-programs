import random
import time
moves = ("rock", "paper", "scissors")
type_chart = {
    "rock": "paper",
    "scissors": "rock",
    "paper": "scissors"
}

countdown = {
    "ROCK!": 3,
    "PAPER!": 2,
    "SCISSORS!": 1,
    "": "SHOOT!"
}

for move, count in countdown.items():
    print(f"{count}, {move}")
    time.sleep(1)


def game(move):
    while True:
        if move.lower() in moves:
            computer_move = moves[random.randint(0, 2)]
            print(f"Computer plays {computer_move}. ")
            weakness = type_chart[move.lower()]
            if computer_move == weakness:
                print("You Lose!")

            elif computer_move == move.lower():
                print("You Tied.")

            else:
                print("You Win!")

        else:
            print("It's rock, paper, scissors.")


# print(random.choice(moves))
