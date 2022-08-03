from turtle import Turtle
from random import randint

X_MIN = -280
X_MAX = 280
Y_MIN = -280
Y_MAX = 280

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")        
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("purple")
        self.speed("fastest")
        self.new_food()
        

    def new_food(self):
        self.goto(randint(X_MIN, X_MAX), randint(Y_MIN, Y_MAX))


