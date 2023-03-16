import arcade


#main function
def main():
    colorSelectPrompt()
    arcade.open_window(600, 600, "Fish Under The Sun")
    skyBack()
    # getting ready to draw
    arcade.start_render()
    #drawing
    drawSun(300, 350)
    drawWater(400, 175)
    drawFish(240, 75)
    drawFish(300, 260)
    # finish drawing
    arcade.finish_render()
    # keeping the window open
    arcade.run()

# function that lets you choose what color the sky is
def colorSelectPrompt():
    print("What color would you like the sky to be?")
    print("1. orange")
    print("2. red")
    print("3. black")
    print("4. blue")

    skyColor = input("Type the number of the color you want : ")
    global endColor
    if skyColor == "1":
        endColor = arcade.csscolor.DARK_ORANGE
    if skyColor == "2":
        endColor = arcade.csscolor.RED
    if skyColor == "3":
        endColor = arcade.color.BLACK
    if skyColor == "4":
        endColor = arcade.color.SKY_BLUE
    return endColor

#function to draw the sky or background color
def skyBack():
    #setting background color
    arcade.set_background_color((endColor))

#function to draw the sun
def drawSun(x,y):
    #drawing the sun

    #suns beautiful rays
    arcade.draw_line(x, y - 110, x, y + 150, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(x, y - 110, x - 80, y + 130, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(x, y - 110, x + 80, y + 130, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(x, y - 110, x + 140, y + 100, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(x, y - 110, x - 140, y + 100, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(x, y - 50, x + 190, y + 50, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(x, y - 50, x - 190, y + 50, arcade.csscolor.YELLOW, 8)

    #sun base
    arcade.draw_ellipse_filled(x, y, 350, 240, arcade.csscolor.YELLOW)

    #center of sun is (300,350)

# function to draw water
def drawWater(x,y):
    #drawing the water
    arcade.draw_lrtb_rectangle_filled(x - 400, x + 400 , y + 175, y - 175, arcade.color.CORNFLOWER_BLUE)
    #middle of water rectangle is (400, 175)


#function to draw a fish
def drawFish(x,y):
    # drawing the fish

    # tail fin
    arcade.draw_triangle_filled(x - 220, y + 70, x - 135, y, x - 220, y - 70, arcade.csscolor.DARK_SALMON)
    # body
    arcade.draw_ellipse_filled(x, y, 300, 150, arcade.csscolor.DARK_SALMON)

    # body fin
    arcade.draw_line(x - 30, y + 15, x - 70, y + 25, arcade.csscolor.BLACK, 2)
    arcade.draw_line(x - 70, y + 25, x - 70, y - 25, arcade.csscolor.BLACK, 2)
    arcade.draw_line(x - 70, y - 25, x - 30, y - 10, arcade.csscolor.BLACK, 2)

    # eye and mouth
    arcade.draw_circle_filled(x + 100, y + 30, 10, arcade.csscolor.BLACK)
    arcade.draw_arc_filled(x + 120, y - 15, 25, -20, arcade.csscolor.BLACK, 0, 180)

    # center of the fish is (300, 160)


main()
