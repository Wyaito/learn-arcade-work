class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    print('this is main yo')
    room_list = []
    room = Room("You're in a dark room, you can see the light of a doorway to the east", None, None, 1, None)
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
        
        #printing room description and instructions 
        print('')
        print(room_list[current_room].description)
        print('')
        print("You can go North, South, East, or West")
        print(current_room)
        #getting user input and setting it to all caps
        userChoice = input("What direction do you want to go? ")
        userChoice = userChoice.upper()
        
        #If statements to check user input
        
        
        #check if north
        if userChoice == "N" or userChoice == "NORTH":
            nextRoom = room_list[current_room].north
            if nextRoom == None:
                print("You can't go that way")
            else: 
                current_room = nextRoom
        
       
        #check if south
        elif userChoice == "S" or userChoice == "SOUTH":
            nextRoom = room_list[current_room].south
            if nextRoom == None:
                print("You can't go that way")
            else: 
                current_room = nextRoom
        
        
        #check if east
        elif userChoice == "E" or userChoice == "EAST":
            nextRoom = room_list[current_room].east
            if nextRoom == None:
                print("You can't go that way")
            else: 
                current_room = nextRoom
        
       
        #check if west
        elif userChoice == "W" or userChoice == "WEST":
            nextRoom = room_list[current_room].west
            if nextRoom == None:
                print("You can't go that way")
            else: 
                current_room = nextRoom
        else:
            print("That is not a valid direction")

main()
