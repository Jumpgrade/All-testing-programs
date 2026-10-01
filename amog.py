player_movement = {
    "Tavern": {
        "north": "Tavern Room",
        "east": "Tavern Bar",
        "west": "Blacksmith",
        "south": "Woods",
    },

    "Tavern Room": {
        "south": "Tavern"
    },

    "Blacksmith": {
        "east": "Tavern"
    },

    "Tavern Bar": {
        "west": "Tavern"
    },

    "Woods": {
        "north": "Tavern"
        "south"
    },
}

player_action = {
    "Tavern": {
        "talk": {1: "You talk to Felix the innkeeper of the Tavern",
                 2: "Felix: Feel Free to look around the cabin.",
                 5: "amogus"
                 },
    },

    "Blacksmith": {
        "talk": {1: "You talk to Dray the Blacksmith"}
    },

    "Tavern Bar": {
        "talk": {1: "You talk to Bob the Bartender"}
    },

    "Woods": {
        "talk": {2: "Eca: What do you want? Don't waste my time.",
                 1: "You talk to Eca the Swordsmaster",
                 3: "Banana"}
    },
}

dialogue_interaction = {
    "Tavern": 1,
    "Blacksmith": 1,
    "Tavern Bar": 1,
    "Woods": 1,

}
current_location = "Tavern"
current_status = "idle_mode"
npc_state = 1



def player_choice(current_location, current_status):
    movement = player_movement.get(current_location, {})
    action = player_action.get(current_location, {})
    npc_state = dialogue_interaction.get(current_location, {})
    while True:
        choice = input(">")

        if choice.lower() in movement and current_status == "idle_mode":
            destination = movement[choice.lower()]
            print(f"You went to the {destination}")
            npc_state = dialogue_interaction.get(destination, {})
            return destination, "idle_mode", npc_state

        elif choice.lower() in action and current_status == "idle_mode":
            try:
                npc_dialogue = action[choice.lower()]
                print(npc_dialogue[npc_state])
                npc_check = max(npc_dialogue.keys())
                if npc_state in npc_dialogue and npc_state < npc_check:
                    npc_state += 1
                    return current_location, "idle_mode", npc_state
                else:
                    return current_location, "idle_mode", npc_state
            except KeyError:
                safety_net = [
                    option for option in npc_dialogue if option < npc_state]
                if safety_net:
                    safe_number = max(safety_net)
                    safe = npc_dialogue[safe_number]
                    print(safe)

                    return current_location, "idle_mode", npc_state
                else:
                    safe = None
                    return current_location, "idle_mode", npc_state
        else:
            print("You can't do that")


while True:
    current_location, current_status, npc_state = player_choice(
        current_location, current_status)

    dialogue_interaction[current_location] = npc_state
