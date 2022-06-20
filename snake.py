from turtle import Turtle
from random import choice
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
COLORS = ['red', 'green', 'yellow', 'purple']
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.head = self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        return self.snake_segments[0]

    def move(self):
        for snake in range(len(self.snake_segments) - 1, 0, -1):
            segment = self.snake_segments[snake]
            segment.setposition(self.snake_segments[snake - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_square = Turtle('circle')
        new_square.penup()
        new_square.color(choice(COLORS))
        new_square.setposition(position)
        self.snake_segments.append(new_square)

    def extend(self):
        last_segment_position = self.snake_segments[len(self.snake_segments) - 1].position()
        self.add_segment(last_segment_position)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
