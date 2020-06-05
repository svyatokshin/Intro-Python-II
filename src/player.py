# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def movement(self, direction):
        new_room = getattr(self.current_room, f"{direction}_to")
        if new_room != None:
            self.current_room = new_room
            print(self.current_room)
            print("Items in the room: '{}'\n".format(
                ", ".join([item.name for item in self.current_room.items])))
        else:
            print("you cannot go this direction, please choose another")

    def take(self, item_name):
        item = self.current_room.drop(item_name)
        self.items.append(item)
        item.on_take()
        return item

    def drop(self, item_name):
        item = self.find(item_name)
        self.items.remove(item)
        self.current_room.take(item)
        item.on_drop()
        return item

    def find(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

    def inventory(self):
        print("\nInventory:\n")
        for idx, item in enumerate(self.items):
            print(f"  " + str(idx+1) + ") " + item.name + "\n")
