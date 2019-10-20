import arcade

class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")
        
        # Load the sound when the application starts
        self.laser_sound = arcade.load_sound("./sounds/laser1.ogg")
        # arcade.draw_text("Press space to trigger the laser", 50, 150, arcade.color.BLACK, 24)
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

    def on_key_press(self, key, modifiers):
        # If the user hits  the space bar, play the sound that we loaded
        if key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)
            
def main():
    window = MyApplication(400, 400)
    arcade.run()

if __name__ == "__main__":
    main()