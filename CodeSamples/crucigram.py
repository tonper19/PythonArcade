import arcade

arcade.open_window(1040, 500, "Grid")
# Set the background color
arcade.set_background_color(arcade.color.AMAZON)

# Get ready to draw
arcade.start_render()

# Draw a line
# Start point of (75, 590)
# End point of (95, 570)

for coordinate in range(10, 491, 40):
    arcade.draw_line(coordinate, 10, coordinate, 490, arcade.color.BLACK, 2)
    arcade.draw_line(10, coordinate, 490, coordinate, arcade.color.BLACK, 2)

# for y in range(10, 491, 40):
    
#     arcade.draw_line(10, y, 490, y, arcade.color.BLACK, 2)


for x in range(510, 991, 40):
    arcade.draw_line(x, 10, x, 490, arcade.color.BLUEBERRY, 2)

for y in range(10, 491, 40):
    arcade.draw_line(510, y, 990, y, arcade.color.BLUEBERRY, 2)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
