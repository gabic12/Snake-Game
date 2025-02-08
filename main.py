from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Setting the game variables
game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0

#Scrren will react to our key inputs
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collecting food
    if snake.snake_head.distance(food) < 15:
        food.spawn_food()
        snake.increase_snake_size()
        score += 1
        scoreboard.display_score(score)

    #Hitting the wall
    if snake.snake_head.xcor() > 280 or  snake.snake_head.xcor() < -280 or  snake.snake_head.ycor() > 280 or  snake.snake_head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #Hitting the tail
    for segment in snake.snake_segments_list[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()