# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """ Holds information about the player """
    def __init__(self, name, starting_room, items = []):
        self.name = name
        self.current_room = starting_room
        self.items = items
    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
#        current_room = self.current_room
#        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(f"You are in the {self.current_room}")
        else:
            print("You cannot move in that direction")
