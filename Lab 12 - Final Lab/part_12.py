class Room:
    def __init__(self, rNumber, description, north, south, east, west):
        self.rNumber = rNumber
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


class Item:
    def __init__(self, roomNumber, description, name):
        self.roomNumber = roomNumber
        self.description = description
        self.name = name


def main():
    print('this is main yo')
    room_list = []
    item_list = []

    # -- CREATING ITEMS --
    # sword
    item = Item(2, 'this is a sharp sword, be careful where you swing it', 'sword')
    item_list.append(item)
    # compass
    item = Item(1, "this compass can tell you what direction you're going", 'compass')
    item_list.append(item)

    # -- CREATING ROOMS --
    # ROOM 0
    room = Room(0, "You're in a dark room, you can see the light of a doorway to the east", None, None, 1, None)
    room_list.append(room)
    # ROOM 1
    room = Room(1,
                "This room is a kitchen, smells like something good is cooking!\nThere are doors North, East, or back the way you came.",
                3, None, 2, 0)
    room_list.append(room)
    # ROOM 2
    room = Room(2,
                "This room is a bedroom with something playing on the TV\nThe only door is the one you came in from.",
                None, None, None, 1)
    room_list.append(room)
    # ROOM 3
    room = Room(3, "This looks like it's the living room\nThere is a door to the North, or back the way you came.", 4,
                1, None, None)
    room_list.append(room)
    # ROOM 4
    room = Room(4, "Woah! this room is a bowling alley.\nYou can go East, West, or back from where you entered.", None,
                3, 6, 5)
    room_list.append(room)
    # ROOM 5
    room = Room(5, "This is just a boring laundry room\nYou can only leave the way you came in.", None, None, 4, None)
    room_list.append(room)
    # ROOM 6
    room = Room(6, "this is a movie theatre room.\nYou can only leave the way you came in.", None, None, None, 4)
    room_list.append(room)
    done = False
    current_room = 0

    while done == False:

        # printing room description and instructions

        print('')
        print(room_list[current_room].description)
        print('')
        i = 0
        while i < len(item_list):
            if item_list[i].roomNumber != room_list[current_room].rNumber:
                i += 1

            else:
                print(item_list[i].description)
                i += 1

        print("You can go North, South, East, or West\nOr you can exit the game.")
        # getting user input and setting it to all caps
        userCommand = input("What direction do you want to go? ")
        userCommand = userCommand.upper()
        command_words = userCommand.split(" ")
        # If statements to check user input


        # --- PARSING USER COMMANDS ---

##############################################################################################################
        # -- MOVE COMMAND --
        if command_words[0] == 'MOVE':

            # check if north
            if command_words[1] == "N" or command_words[1] == "NORTH":
                nextRoom = room_list[current_room].north
                if nextRoom == None:
                    print("You can't go that way")
                else:
                    current_room = nextRoom


            # check if south
            elif command_words[1] == "S" or command_words[1] == "SOUTH":
                nextRoom = room_list[current_room].south
                if nextRoom == None:
                    print("You can't go that way")
                else:
                    current_room = nextRoom


            # check if east
            elif command_words[1] == "E" or command_words[1] == "EAST":
                nextRoom = room_list[current_room].east
                if nextRoom == None:
                    print("You can't go that way")
                else:
                    current_room = nextRoom


            # check if west
            elif command_words[1] == "W" or command_words[1] == "WEST":
                nextRoom = room_list[current_room].west
                if nextRoom == None:
                    print("You can't go that way")
                else:
                    current_room = nextRoom
#########################################################################################################
        # GET COMMAND

        elif command_words[0] == 'GET':
            targetItem = command_words[1].lower()
            i = 0
            foundItem = False
            while i < len(item_list):
                if item_list[i].name == targetItem and item_list[i].roomNumber == current_room:
                    print(item_list[i].name, 'added to your inventory')
                    item = Item(-1,item_list[i].description,item_list[i].name)
                    item_list.append(item)
                    del item_list[i]
                    foundItem = True
                    i + 1

                else:
                    i += 1
            if foundItem == False:
                print("There isn't a", targetItem,"in this room")
#########################################################################################################
        # INVENTORY COMMAND
        elif command_words[0] == 'INVENTORY':
            i = 0
            print('Items in your inventory:')
            while i < len(item_list):
                if item_list[i].roomNumber == -1:
                    print(item_list[i].name)
                    i += 1
                else:
                    i += 1
###########################################################################################################
        # DROP ITEM COMMAND
        elif command_words[0] == 'DROP':
            i = 0
            hasItem = False
            targetItem = command_words[1].lower()
            while i < len(item_list):
                if item_list[i].roomNumber == -1 and item_list[i].name == targetItem:
                    item = Item(current_room,item_list[i].description,item_list[i].name)
                    item_list.append(item)
                    del item_list[i]
                    i += 1
                    hasItem = True
                    print(targetItem, "dropped")
                else:
                    i += 1
            if hasItem == False:
                print('Item not found in inventory')




        # check if exit
        elif command_words[0] == "X" or command_words[0] == "EXIT":
            done = True


        else:
            print("That is not a valid direction")


main()