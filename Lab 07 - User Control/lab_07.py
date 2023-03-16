""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
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
def scene():
    # setting background color
    arcade.set_background_color((253, 94, 63))

    # getting ready to draw
    arcade.start_render()

    # drawing code goes here

    # drawing the sun
    arcade.draw_line(300, 240, 300, 500, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(300, 240, 220, 480, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(300, 240, 380, 480, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(300, 240, 440, 450, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(300, 240, 160, 450, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(300, 300, 490, 400, arcade.csscolor.YELLOW, 8)
    arcade.draw_line(300, 300, 110, 400, arcade.csscolor.YELLOW, 8)
    arcade.draw_ellipse_filled(300, 350, 350, 240, arcade.csscolor.YELLOW)

    # drawing the water
    arcade.draw_lrtb_rectangle_filled(0, 800, 350, 0, arcade.color.CORNFLOWER_BLUE)

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

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)


        # Create our fish
        self.fish = Fish(50, 50, 15, arcade.color.AUBURN)


    def on_draw(self):
        arcade.start_render()
        scene()
        self.fish.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.fish.position_x = x
        self.fish.position_y = y

# class MyGame(arcade.Window):
#     """ Our Custom Window Class"""
#
#     def __init__(self):
#         """ Initializer """
#
#         # Call the parent class initializer
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
#
#     def on_draw(self):
#         #backround using scene function
#         scene()
#
#         class Fish:
#             def __init__(self, position_x, position_y, radius, color):
#                 # Take the parameters of the init function above,
#                 # and create instance variables out of them.
#                 self.position_x = position_x
#                 self.position_y = position_y
#                 self.radius = radius
#                 self.color = color
#
#             def draw(self):
#
#                 drawFish(self.position_x, self.position_y)
#         # finish drawing
#         arcade.finish_render()
#         # keeping the window open


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()