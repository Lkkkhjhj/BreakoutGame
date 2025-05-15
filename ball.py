from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.x_move = 5 * random.choice([-1, 1])
        self.y_move = 5
        self.move_speed = 0.03

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, -200)
        self.x_move *= random.choice([-1, 1])
        self.y_move = 5
