move = {
    "Tavern":{
        "South": "Tavern_Room",
        "North": "Santa"},

    ""
}

while True:
    command = input(">")
    if command in move:
        print(move.get(command))

    else:
        print("You can't go there")
