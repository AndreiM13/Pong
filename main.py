from turtle import Screen
from paddle import Paddle
from ball import Ball
from  scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
scoreboard = Scoreboard()
paddle1.new_position(350, 0)
paddle2.new_position(-350, 0)


screen.listen()
screen.onkey(paddle1.go_Up, "Up")
screen.onkey(paddle1.go_Down, "Down")
screen.onkey(paddle2.go_Up, "w")
screen.onkey(paddle2.go_Down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
     #need to bounce
        ball.bounce_y()
    #Detect collision with  paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect when left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
