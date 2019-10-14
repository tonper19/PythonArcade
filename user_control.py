
# copied from: 
# https://arcade-book.readthedocs.io/en/latest/chapters/15_window_class/window_class.html

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
    
    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        print(f'Ball. x = {self.position_x}, y = {self.position_y}, change_x = {self.change_x}, change_y = {self.change_y}')
        if self.position_x < self.radius:
            self.change_x *= -1
        
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1
        
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

    def increment_radius(self):
        self.radius += 1

    def decrement_radius(self):
        self.radius -= 1

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        
        self.ball_list = []

        ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)

        ball = Ball(100, 150, 2, 3, 15, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        self.ball_list.append(ball)
        
        ball = Ball(150, 250, -3, -1, 15, arcade.color.FOREST_GREEN)
        self.ball_list.append(ball)
        
        print('MyGame constructor called')
    
    def on_draw(self):
        arcade.start_render()
        
        for ball in self.ball_list:
            ball.draw()

        # print('MyGame on_draw called')
    
    # def update(self, delta_time):
    #     for ball in self.ball_list:
    #         ball.update()
    #     # print(f'MyGame update called. delta_time = {delta_time}')

    def on_mouse_motion(self, x, y, dx, dy):
        for idx in range(len(self.ball_list)):
            i = idx - 1
            if idx == 1:
                self.ball_list[i].position_x = x
                self.ball_list[i].position_y = y
            elif idx == 2:
                self.ball_list[i].position_x = x - 50
                self.ball_list[i].position_y = y + 50
            else:
                self.ball_list[i].position_x = x + 50
                self.ball_list[i].position_y = y - 50

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for ball in self.ball_list:
                ball.decrement_radius()
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            for ball in self.ball_list:
                ball.increment_radius()

def main():
    window = MyGame(640, 480, 'Bouncing Ball')
    arcade.run()

if __name__ == '__main__':
    main()
    
