"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting room for the simplified prototype.

current_room = "Great Hall"  # Player begins in the Great Hall

print("Welcome to the simplified Dragon Text Game!")
print("Type north, south, east, west, or exit to quit.\n")

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

while current_room != "exit":
    # Step 1: Display the current room
    print(f"You are currently in the {current_room}.")

    # Step 2: Prompt for a command
    command = input("Enter your command: ").lower().strip()

    # Step 3: Handle exit command
    if command == "exit":
        current_room = "exit"
        print("Exiting the game...")

    # Step 4: Handle movement commands
    elif command in ["north", "south", "east", "west"]:
        if command in rooms[current_room]:
            new_room = rooms[current_room][command]
            print(f"You move {command} and enter the {new_room}.\n")
            current_room = new_room
        else:
            print("You cannot go that way.\n")

    # Step 5: Handle invalid input
    else:
        print("Invalid command. Try north, south, east, west, or exit.\n")

# TODO: Run and debug all milestone cases in prototype/README.md.

print("Thanks for playing the game. Hope you enjoyed it!")
