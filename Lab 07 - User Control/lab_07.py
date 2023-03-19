""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
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
def scene():
    # setting background color
    arcade.set_background_color((253, 94, 63))

    # getting ready to draw
    arcade.start_render()

    # drawing code goes here

    # # drawing the sun
    # arcade.draw_line(300, 240, 300, 500, arcade.csscolor.YELLOW, 8)
    # arcade.draw_line(300, 240, 220, 480, arcade.csscolor.YELLOW, 8)
    # arcade.draw_line(300, 240, 380, 480, arcade.csscolor.YELLOW, 8)
    # arcade.draw_line(300, 240, 440, 450, arcade.csscolor.YELLOW, 8)
    # arcade.draw_line(300, 240, 160, 450, arcade.csscolor.YELLOW, 8)
    # arcade.draw_line(300, 300, 490, 400, arcade.csscolor.YELLOW, 8)
    # arcade.draw_line(300, 300, 110, 400, arcade.csscolor.YELLOW, 8)
    # arcade.draw_ellipse_filled(300, 350, 350, 240, arcade.csscolor.YELLOW)

    # drawing the water
    # arcade.draw_lrtb_rectangle_filled(0, 800, 350, 0, arcade.color.CORNFLOWER_BLUE)
class Sun:
    def __init__(self, position_x, position_y, change_x, change_y, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        #self.radius = radius
        self.color = color

    def draw(self):

        drawSun(self.position_x,self.position_y)

    def update(self):
        self.position_y += self.change_y
        if self.position_x < 174 and self.change_x < 0:
            pass
        elif self.position_x > 475 and self.change_x > 0:
            pass
        else:
            self.position_x += self.change_x
class Fish:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        drawFish(self.position_x,self.position_y)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x
class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)


        # Create our fish
        self.fish = Fish(50, 50, 15, arcade.color.AUBURN)
        self.sun = Sun(300,350,0,0,arcade.color.YELLOW)

    def on_draw(self):
        arcade.start_render()
        scene()
        self.sun.draw()
        arcade.draw_lrtb_rectangle_filled(0, 800, 350, 0, arcade.color.CORNFLOWER_BLUE)
        self.fish.draw()
    def on_mouse_motion(self, x, y, dx, dy):
        self.fish.position_x = x
        self.fish.position_y = y

    def update(self, delta_time):
        self.sun.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            if self.sun.position_x < 0:
                self.sun.change_x = 0
            else:
                self.sun.change_x = -MOVEMENT_SPEED
            # else:
            #     pass
        elif key == arcade.key.RIGHT:
            self.sun.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.sun.change_x = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()