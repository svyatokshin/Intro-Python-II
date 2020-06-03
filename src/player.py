# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, direction=None):
        self.name = name
        self.room = room
        self.direction = direction
        self.inventory = []

    def movement(self, direction):
        move = getattr(self.room, f"{direction}_to")
        if move != None:
            self.room = move
            print(self.room)
        else:
            print("you cannot go this direction, please choose another")

    # def __str__(self):
    #     return f"Your name is {self.name} and the location you are in is {self.room}."
