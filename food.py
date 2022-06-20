from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.generate_food()

    def generate_food(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.setposition(random_x, random_y)



