""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_GOOD = 0.2
SPRITE_SCALING_BAD = 0.05
doritoCount = 10
bombCount = 20
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

eat  = arcade.load_sound("bite-of-chip-48270.mp3")
explosion = arcade.load_sound('mixkit-arcade-game-explosion-2759.wav')
class Dorito(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class Bomb(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_x -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.left < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")


        # Variables that will hold sprite lists.
        self.player_list = None
        self.good_list = None
        self.bad_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.amount = 0
        self.damage = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)


    def on_draw(self):
        arcade.start_render()
        if self.amount < 10 and self.damage < 3:
            self.good_list.draw()
            self.bad_list.draw()
            self.player_list.draw()
            # Put the text on the screen.

            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.RED, 14)
            ondamage = f"Damage: {self.damage}"
            arcade.draw_text(ondamage, 300, 20, arcade.color.RED, 14)
        elif self.damage > 2:
            arcade.draw_text('YOU DIED!', 300, 400, arcade.color.RED, 100)
            ondamage = f"Damage: {self.damage}"
            arcade.draw_text(ondamage, 300, 20, arcade.color.RED, 14)
        elif self.amount == 10:
            arcade.draw_text('YOU WON!',300,400, arcade.color.RED, 100)

    def on_mouse_motion(self, x, y, dx, dy):


        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.good_list.update()
        self.bad_list.update()
        # Generate a list of all sprites that collided with the player.
        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.good_list)

        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_list)
        # Loop through each colliding sprite, remove it, and add to the score.

        for dorito in good_hit_list:
            dorito.remove_from_sprite_lists()
            arcade.play_sound(eat)
            dorito.reset_pos()
            self.score += 1
            self.amount += 1

        for bomb in bad_hit_list:
            bomb.remove_from_sprite_lists()
            bomb.reset_pos()
            arcade.play_sound(explosion)
            self.score -= 1
            self.damage += 1



    def setup(self):
        # Sprite lists


        self.player_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()
        self.score  = 0
        self.player_sprite = arcade.Sprite('obama.png', SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for x in range(doritoCount):
            self.good_sprite = Dorito('dorito.png', SPRITE_SCALING_GOOD)
            self.good_sprite.center_x = random.randint(0,1200)
            self.good_sprite.center_y = random.randint(300,800)
            self.good_list.append(self.good_sprite)
        for x in range(bombCount):
            self.bad_sprite = Bomb('bomb.png', SPRITE_SCALING_BAD)
            self.bad_sprite.center_x = random.randint(700,1200)
            self.bad_sprite.center_y = random.randint(0,800)
            self.bad_list.append(self.bad_sprite)

" Movement and game logic """
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()