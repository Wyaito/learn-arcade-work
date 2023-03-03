class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0


def main():
    print('this is main yo')
    room_list = []
    room = Room("You are in a dark room, you can see the light of a doorway to the east", None, None, 1, None)
    room_list.append(room)
    room = Room("this room is boring", 3, None, 2, 0)
    room_list.append(room)
    room = Room("this room is gay af", None, None, None, 1)
    room_list.append(room)
    room = Room("this room is straight witerally", 5, 1, None, None)
    room_list.append(room)
    room = Room("this room swings both ways", None, 3, 6, 4)
    room_list.append(room)
    room = Room("this room wont do anyone", None, None, 5, None)
    room_list.append(room)
    room = Room("heeheeheehaw", None, None, None, 5)
    room_list.append(room)
    current_room = 0
    done = False
    while done == False:
        print('')
        print(room_list[current_room].description)
        input("What direction do you want to go? type N, S, E, or W")

main()
