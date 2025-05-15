from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        if self.xcor() > -330:
            self.setx(self.xcor() - 30)

    def move_right(self):
        if self.xcor() < 330:
            self.setx(self.xcor() + 30)
