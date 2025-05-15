import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Classic")
screen.tracer(0)

# Game objects
paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

# Main game loop
game_on = True
while game_on:
    # Check if the screen is still open
    try:
        time.sleep(ball.move_speed)
        screen.update()
        
        ball.move()
        
        # Wall bounce
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()
        if ball.ycor() > 280:
            ball.bounce_y()
        
        # Paddle bounce
        if ball.ycor() < -230 and paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60:
            ball.bounce_y()
        
        # Brick collision
        for brick in bricks.all_bricks[:]:
            if brick.distance(ball) < 40:
                brick.hideturtle()
                bricks.all_bricks.remove(brick)
                scoreboard.increase_score()
                ball.bounce_y()
                break
        
        # Missed ball
        if ball.ycor() < -290:
            scoreboard.lose_life()
            ball.reset_position()
            if scoreboard.lives == 0:
                scoreboard.game_over()
                game_on = False
        
        # Win
        if not bricks.all_bricks:
            scoreboard.show_win_message()
            game_on = False
    except turtle.Terminator:
        # Exit the game loop if the screen is closed
        game_on = False

screen.exitonclick()
