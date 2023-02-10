def main():
    #intro and instructions
    print('Welcome to Camel!')
    print('You have stolen a camel to make your way across the great Mobi desert.')
    print('The natives want their camel back and are chasing you down! Survive your')
    print('desert trek and out run the natives')

    #variables
    done = False
    milesTraveled = 0
    thirst = 0
    camelTiredness = 0
    distanceNativesTraveled = -20
    distanceFromNatives = abs(milesTraveled - distanceNativesTraveled)
    drinksInCanteen = 3
    #main game loop
    while done==False:
            print('A. Drink from your canteen.')
            print('B. Ahead moderate speed.')
            print('C. Ahead full speed.')
            print('D. Stop for the night.')
            print('E. Status check.')
            print('Q. Quit.')
            userChoice = input("What is your choice? ")
            userChoice = userChoice.upper()
            if userChoice == 'Q':
                done = True
                print("you have quit the game")
            elif userChoice == 'E':
                print("Miles traveled: " + str(milesTraveled))
                print("Drinks in canteen: " + str(drinksInCanteen))
                print("The natives are " + str(distanceFromNatives) + " miles behind you")
            elif userChoice == 'D':
                camelTiredness = 0
                print('your camel is happy')
                





main()