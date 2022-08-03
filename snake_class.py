from turtle import Turtle
from random import random

START_POS = ((0, 0), (0, -20), (0, -40))
DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake():   

    def __init__(self):
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]
    
    def create_snake(self):
        for POS in START_POS:
            self.add_seg(POS)

    
    def add_seg(self, POS):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color(random(), random(), random())
        snake.goto(POS)
        self.snake_seg.append(snake)
    
    def move(self):
        for seg in range(len(self.snake_seg) - 1, 0, -1):
            position_x = self.snake_seg[seg-1].xcor()
            position_y = self.snake_seg[seg-1].ycor()
            self.snake_seg[seg].goto(position_x, position_y)
        self.head.fd(DISTANCE)
    
    def extend(self):
        self.add_seg(self.snake_seg[-1].pos())

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
        
    def go_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)




