from turtle import Turtle

ALIGN = "center"
FONT_SCORE = ("Courier", 25, "italic")
FONT_GAME_OVER = ("Courier", 50, "italic")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Red")
        self.ht()
        self.penup()        
        self.goto(0, 250)
        self.make_scoreboard()
    
    def make_scoreboard(self):
        self.write("Score: " + str(self.score), move = False, align = ALIGN, font = FONT_SCORE)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("YOU ARE STUPID", move = False, align = ALIGN, font = FONT_GAME_OVER)

    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.make_scoreboard()