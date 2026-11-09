from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None
    large_image = None

    def __init__(self, x, y, velocity, large=False):
        if large:
            if Ball.large_image is None:
                Ball.large_image = load_image('ball41x41.png')
            self.image = Ball.large_image
        else:
            if Ball.image is None:
                Ball.image = load_image('ball21x21.png')
            self.image = Ball.image
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
