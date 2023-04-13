class Item:
    def __init__(self, roomNumber, description, name):
        self.roomNumber = roomNumber
        self.description = description
        self.name = name

def main():
    item_list = []
    #sword
    item = Item(2, 'this is a sharp broadsword, be careful where you swing it', 'Sword')
    item_list.append(item)
    #compass
    item = Item(1, "this compass can tell you what direction you're going", 'compass')
    item_list.append(item)
    #
