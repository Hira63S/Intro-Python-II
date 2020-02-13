from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player = Player(input("Your name?"), room['outside'])
print(f"Hello, {player.name}") #.\n\n{player.current_room}")

print(player.current_room)
# Write a loop that:
while True:
    cmd = input("-> ".lower())
    if cmd in ["n", "s", "e", "w"]:
        player.travel(cmd)
#        current_room = player.current_room
#        next_room = getattr(current_room, f"{cmd}_to")
#        if next_room != None:
#            player.current_room = next_room
#        else:
#            print(" you cannot move in that direction")
#        print("MOVE" + cmd)
    elif cmd =="q":
        print("Goodbye!")
        exit()
    else:
        print("I did not understand that command.")
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def motion(decision):
    """ Attempt to move in a cardinal direction or return to current room """
    if decision == 'n':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
        else:
            print("You cannot move in that direction")
    if decision == 's':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.s_to
        else:
            print("You cannot move in that direction")
    if decision == 'e':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.e_to
        else:
            print("You cannot move in that direction")
    if decision == 'w':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.w_to
        else:
            print("You cannot move in that direction")
    else:
        return move


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# we can make them move but now let's add item:
room['foyer'] = ['torch']

items = {
    'AR_Heavy': Item("AR_BHeavy", "AR_Blue_Heavy from Fortnite", "drop the one you already have"),
    'Sniper' : Item("Sniper_Heavy", "Heavy_Sniper from FortNite", "drop"),
    'torch' : Item("torch", "to find the way"),
    'map': Item("map", "with linings for passageways"),
    'teaser': Item("teaser", "To tease other hunters"),
    'stick': Item("stick", "to protect against the enemy")
}
