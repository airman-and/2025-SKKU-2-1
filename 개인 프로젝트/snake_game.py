from ursina import *
from random import randint

GRID_SIZE = 10

class Snake3D:
    def __init__(self):
        self.segments = [Entity(model='cube', color=color.green, position=(0,0,0))]
        self.direction = Vec3(1,0,0)
        self.add_food()

    def add_food(self):
        self.food = Entity(model='cube', color=color.red,
            position=(randint(-GRID_SIZE, GRID_SIZE), 0, randint(-GRID_SIZE, GRID_SIZE)))

    def move(self):
        head = self.segments[0]
        new_pos = head.position + self.direction
        if new_pos == self.food.position:
            self.food.disable()
            self.segments.append(Entity(model='cube', color=color.green, position=head.position))
            self.add_food()
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].position = self.segments[i-1].position
        head.position = new_pos

def update():
    if held_keys['w']: snake.direction = Vec3(0,0,1)
    if held_keys['s']: snake.direction = Vec3(0,0,-1)
    if held_keys['a']: snake.direction = Vec3(-1,0,0)
    if held_keys['d']: snake.direction = Vec3(1,0,0)
    snake.move()

app = Ursina()
camera.position = (0,20,-20)
camera.look_at((0,0,0))
snake = Snake3D()
app.run()