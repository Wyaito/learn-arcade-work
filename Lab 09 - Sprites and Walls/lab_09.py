"""
Sprite Move With Walls

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_walls
"""

import arcade
import random
SPRITE_SCALING = 0.12
WALL_SCALING = 0.3
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DORITO_SCALING = 0.2
DORITO_COUNT = 40
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 5
eat = arcade.load_sound('bite-of-chip-48270.mp3')

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.dorito_list = None
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.score = None
    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.dorito_list = arcade.SpriteList()
        # Set up the player
        self.player_sprite = arcade.Sprite("GBF.png",
                                           SPRITE_SCALING)
        self.score = 0
        self.player_sprite.center_x = 40
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)
        # dorito sprite setup
        # self.dorito_sprite = arcade.Sprite('dorito.png', DORITO_SCALING)
        for i in range(DORITO_COUNT):

            dorito = arcade.Sprite("bean.jpg", DORITO_SCALING)

            dorito_placed_successfully = False

            # Keep trying until success
            while not dorito_placed_successfully:
                # Position the dorito
                dorito.center_x = random.randrange(SCREEN_WIDTH)
                dorito.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the dorito is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(dorito, self.wall_list)

                # See if the dorito is hitting another coin
                dorito_hit_list = arcade.check_for_collision_with_list(dorito, self.dorito_list)

                if len(wall_hit_list) == 0 and len(dorito_hit_list) == 0:
                    # It is!
                    dorito_placed_successfully = True

            # Add the dorito to the lists
            self.dorito_list.append(dorito)

        # -- Set up the walls
        # Create a row of boxes
        for x in range(15, 650, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = x
            wall.center_y = 150
            self.wall_list.append(wall)
        for y in range(218, 370, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = 400
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(320, 480, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = 550
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(480, 490, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = 250
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(460, 470, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = 747.5
            wall.center_y = y
            self.wall_list.append(wall)
        for x in range(15, 250, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = x
            wall.center_y = 320
            self.wall_list.append(wall)


        # creating map border
        for y in range(0, 600, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = -15
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(0, 600, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = 815
            wall.center_y = y
            self.wall_list.append(wall)
        for x in range(0, 800, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = x
            wall.center_y = 615
            self.wall_list.append(wall)
        for x in range(15, 785, 64):
            wall = arcade.Sprite("brick.png",
                                 WALL_SCALING)
            wall.center_x = x
            wall.center_y = -15
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 20, 20, arcade.color.RED, 18)
        # Draw all the sprites.
        self.dorito_list.draw()
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):


        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):


        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        dorito_eaten_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.dorito_list)

        for dorito in dorito_eaten_list:
            dorito.remove_from_sprite_lists()
            arcade.play_sound(eat)
            self.score += 1

        self.physics_engine.update()


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()