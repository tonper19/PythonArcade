# https://arcade-book.readthedocs.io/en/latest/chapters/18_sprites_and_collisions/sprites.html

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_GOLD_COUNT = 10
COIN_SILVER_COUNT = 10
COIN_BRONZE_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists.
        self.player_list = None
        self.coin_gold_list = None
        self.coin_silver_list = None
        self.coin_bronze_list = None

        # Number of gold, silver and bronze coins respectevely
        self.coin_count_dict = {'./images/coinGold.png':8
                               ,'./images/coinSilver.png':12
                               ,'./images/coinBronze.png':30}

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_gold_list = arcade.SpriteList()
        self.coin_silver_list = arcade.SpriteList()
        self.coin_bronze_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("./images/character_malePerson_walk0.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for coin_type, number_of_coins in self.coin_count_dict.items():
            for i in range(number_of_coins):

                # Create the coin instance
                # Coin image from kenney.nl
                coin = arcade.Sprite(coin_type, SPRITE_SCALING_COIN)

                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # Add the coin to each of the lists

                self.coin_gold_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        # Draw the sprite lists here. Typically sprites are divided into
        # different groups. Other game engines might call these "sprite layers"
        # or "sprite groups." Sprites that don't move should be drawn in their
        # own group for the best performance, as Arcade can tell the graphics
        # card to just redraw them at the same spot.
        # Try to avoid drawing sprites on their own, use a SpriteList
        # because there are many performance improvements in that code.
        self.coin_gold_list.draw()
        self.player_list.draw()

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()