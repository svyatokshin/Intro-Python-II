from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('shield', "This will protect you")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('lantern', "This will light the way")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('sword', "This will help you fight monsters")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('boots', "This will help you move faster")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('gold', "This will let you buy anything you want")]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("**** WELCOME TO THE BEST ADVENTURE GAME ****")
user_name = input("Name your Player: ")
my_player = Player(user_name, room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
if user_name == "":
    exit()
print(
    f"\n Hello {my_player.name} you are currently at {my_player.current_room}\n\n Item in room: '{my_player.current_room.items[0]}' \n")


while True:
    cmd = input(
        'Which direction would you like to go? [n] [s] [w] [e]. \nIf in a room choose to (take) or (drop) the item in that room. or to quit the game type [q]: ').lower().split(" ")
    if cmd[0] in ["n", "s", "e", "w"]:
        my_player.movement(cmd[0])
    elif cmd[0] == "q":
        print("Thank you for Playing")
        exit()
    elif cmd[0] in ["get", "take"]:
        if cmd[1] != my_player.current_room.items[0].name:
            print("No such item found")
        else:
            item_name = cmd[1]
            my_player.take(item_name)
    elif cmd[0] in ["drop"]:
        item_name = cmd[1]
        my_player.drop(item_name)
    elif cmd[0] in ["i"]:
        my_player.inventory()
    else:
        print("Please try another direction you are gonna fall off this world")
