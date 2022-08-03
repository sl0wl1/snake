from snake_class import Snake
from time import sleep
from turtle import Screen
from snake_food import Food
from snake_score import Scoreboard
from snake_area import Area

screen = Screen()
screen.tracer(0)
snake = Snake()
food = Food()

scoreboard = Scoreboard()
area = Area()


screen.title("Snake-Mania")
screen.bgcolor("yellow")
screen.setup (width=600, height=600)


screen.listen()

def game():

    screen.onkeypress(snake.go_up, "Up")
    screen.onkeypress(snake.go_down, "Down")
    screen.onkeypress(snake.go_left, "Left")
    screen.onkeypress(snake.go_right, "Right")
    not_over = True
    
    while not_over:
        area.draw_area()
        screen.update()
        if scoreboard.score < 5:
            sleep(0.1)
        elif scoreboard.score < 10:
            sleep(0.05)

        snake.move()
        if snake.head.distance(food) < 15:
            food.new_food()
            snake.extend()
            scoreboard.increase_score()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            not_over = False
            scoreboard.game_over()
        for seg in snake.snake_seg[1:]:
            if snake.head.distance(seg) < 10:
                not_over = False
                scoreboard.game_over()

screen.onkeypress(game, "s")
screen.exitonclick()