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
    #ROOM 0
    room = Room("You're in a dark room, you can see the light of a doorway to the east", None, None, 1, None)
    room_list.append(room)
    #ROOM 1
    room = Room("This room is a kitchen, smells like something good is cooking!\nThere are doors North, East, or back the way you came.", 3, None, 2, 0)
    room_list.append(room)
    #ROOM 2
    room = Room("This room is a bedroom with something playing on the TV\nThe only door is the one you came in from.", None, None, None, 1)
    room_list.append(room)
    #ROOM 3
    room = Room("This looks like it's the living room\nThere is a door to the North, or back the way you came.", 4, 1, None, None)
    room_list.append(room)
    #ROOM 4
    room = Room("Woah! this room is a bowling alley.\nYou can go East, West, or back from where you entered.", None, 3, 6, 5)
    room_list.append(room)
    #ROOM 5
    room = Room("This is just a boring laundry room\nYou can only leave the way you came in.", None, None, 4, None)
    room_list.append(room)
    #ROOM 6
    room = Room("this is a movie theatre room.\nYou can only leave the way you came in.", None, None, None, 4)
    room_list.append(room)
    done = False
    current_room = 0
    while done == False:

        #printing room description and instructions 

        print('')
        print(room_list[current_room].description)
        print('')
        print("You can go North, South, East, or West\nOr you can exit the game.")
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

        #check if exit
        elif userChoice == "X" or userChoice == "EXIT":
            done = True


        else:
            print("That is not a valid direction")

main()
