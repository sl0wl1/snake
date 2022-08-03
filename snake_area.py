from turtle import Turtle

CORNER_TL = (-290, 290)
CORNER_TR = (290, 290)
CORNER_BR = (290, -290)
CORNER_BL = (-290, -290)
CORNER_POS = (CORNER_TL,CORNER_TR, CORNER_BR, CORNER_BL)

class Area(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.penup
        self.goto(CORNER_TL)
        self.pendown()

    def draw_area(self):
        for POS in range(len(CORNER_POS)):
            self.goto(CORNER_POS[POS])
