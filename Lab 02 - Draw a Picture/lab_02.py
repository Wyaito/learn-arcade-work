import arcade
arcade.open_window(600, 600, "Drawing")

#setting background color
arcade.set_background_color((253, 94, 63))

#getting ready to draw
arcade.start_render()

#drawing code goes here

#drawing the sun
arcade.draw_line(300, 240, 300, 500, arcade.csscolor.YELLOW, 8)
arcade.draw_line(300, 240, 220, 480, arcade.csscolor.YELLOW, 8)
arcade.draw_line(300, 240, 380, 480, arcade.csscolor.YELLOW, 8)
arcade.draw_line(300, 240, 440, 450, arcade.csscolor.YELLOW, 8)
arcade.draw_line(300, 240, 160, 450, arcade.csscolor.YELLOW, 8)
arcade.draw_line(300, 300, 490, 400, arcade.csscolor.YELLOW, 8)
arcade.draw_line(300, 300, 110, 400, arcade.csscolor.YELLOW, 8)
arcade.draw_ellipse_filled(300, 350, 350, 240, arcade.csscolor.YELLOW)


#drawing the water
arcade.draw_lrtb_rectangle_filled(0, 800, 350, 0, arcade.color.CORNFLOWER_BLUE)


#drawing the fish
arcade.draw_triangle_filled(80, 230, 165, 160, 80, 90, arcade.csscolor.DARK_SALMON)
arcade.draw_ellipse_filled(300, 160, 300, 150, arcade.csscolor.DARK_SALMON)

arcade.draw_line(270, 175, 230, 185, arcade.csscolor.BLACK, 2)
arcade.draw_line(230, 185, 230, 135, arcade.csscolor.BLACK, 2)
arcade.draw_line(230, 135, 270, 150, arcade.csscolor.BLACK, 2)

arcade.draw_circle_filled(400, 190, 10, arcade.csscolor.BLACK)
arcade.draw_arc_filled(420, 145, 25, -20, arcade.csscolor.BLACK, 0, 180)

#finish drawing
arcade.finish_render()
#keeping the window open
arcade.run()