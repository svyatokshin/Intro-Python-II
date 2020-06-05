# Implement a class to hold room information. This should have name and
# description attributes.


class Room():

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def take(self, item):
        self.items.append(item)

    def drop(self, item_name):
        item = self.find_item(item_name)
        self.items.remove(item)
        return item

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

    def __str__(self):
        return f"{self.name}.\n\n {self.description}."
