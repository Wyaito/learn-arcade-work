import random


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
    distanceFromNatives = 20
    drinksInCanteen = 3

    #main game loop
    while done==False:


        # if thirst > 6:
        #     print('YOU DIED OF THIRST!')
        #     done = True
        #     break
        # elif thirst > 4:
        #     print('You are thirsty!')
        # if camelTiredness > 8:
        #     print('Your camel is dead')
        #     done = True
        # elif camelTiredness > 5:
        #     print('Your camel is getting tired')
        #



        # calculating distance from the natives
        if distanceNativesTraveled < 0:
            distanceFromNatives = abs(distanceNativesTraveled) + milesTraveled
        else:
            distanceFromNatives = (milesTraveled - distanceNativesTraveled)

        #check to see if natives are close
        # if distanceFromNatives < 15:
        #     print('The natives are getting close!')
        # elif distanceFromNatives < 1:
        #     print('The natives caught you!')
        #     print('GAME OVER')


        # #check to see if you won
        # if milesTraveled > 199:
        #     print('YOU ESCAPED AND WON THE GAME!')
        #     done = True

        #instructions
        print('A. Drink from your canteen.')
        print('B. Ahead moderate speed.')
        print('C. Ahead full speed.')
        print('D. Stop for the night.')
        print('E. Status check.')
        print('Q. Quit.')

        #user selection prompt
        userChoice = input("What is your choice? ")
        userChoice = userChoice.upper()

        #selection checks
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
            distanceNativesTraveled = distanceNativesTraveled + random.randint(7,16)


        #travel selections
        elif userChoice == 'C':
            fullSpeedTravelDistance = random.randint(10,20)
            milesTraveled = milesTraveled + fullSpeedTravelDistance
            print('You traveled',fullSpeedTravelDistance, 'miles')
            thirst += 1
            camelTiredness += random.randint(1,3)
            distanceNativesTraveled = distanceNativesTraveled + random.randint(7,15)

        elif userChoice == 'B':
            moderateSpeedTravelDistance = random.randint(5,12)
            milesTraveled = milesTraveled + moderateSpeedTravelDistance
            print('You traveled',moderateSpeedTravelDistance,'miles')
            thirst += 1
            camelTiredness += 1
            distanceNativesTraveled = distanceNativesTraveled + random.randint(7, 14)
        if userChoice == 'B' or userChoice == 'C':
            oasis = random.randint(1,20)
            if oasis == 5 and thirst > 4:
                print('You found an oasis!')
                drinksInCanteen = 3
                thirst = 0
                camelTiredness = 0



        elif userChoice == 'A':
            if drinksInCanteen > 0:
                drinksInCanteen -= 1
                thirst = 0
            else:
                print('You don\'t have any drinks left in your canteen!')

            if thirst > 6:
                print('YOU DIED OF THIRST!')
                done = True
                break
            elif thirst > 4:
                print('You are thirsty!')



            # check to see if natives are close
        if distanceFromNatives < 15 and distanceFromNatives > 0:
            print('The natives are getting close!')
        elif distanceFromNatives < 1:
            print('The natives caught you!')
            print('GAME OVER')
            done = True
            break

        #check to see if you won
        if milesTraveled > 199:
            print('YOU ESCAPED AND WON THE GAME!')
            done = True
            break


        #vital checks
        if thirst > 6:
            print('YOU DIED OF THIRST!')
            done = True
            break
        elif thirst > 4:
            print('You are thirsty!')
        if camelTiredness > 8:
            print('Your camel is dead')
            print('GAME OVER')
            done = True
        elif camelTiredness > 5:
            print('Your camel is getting tired')








main()