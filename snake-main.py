from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# hasib = Turtle()
screen = Screen()

screen.setup(width=600, height=450)
screen.bgcolor('black')
screen.title("Snake znz")
#
# hasib.color('white')
# hasib.shape('square')
# hasib.width()

screen.tracer(0)

snake = Snake()
food = Food()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



moveon = True
while moveon:

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.Update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -220 or snake.head.ycor() > 220:
        moveon = False
        scoreboard.gameover()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            moveon = False
            scoreboard.gameover()





screen.exitonclick()
