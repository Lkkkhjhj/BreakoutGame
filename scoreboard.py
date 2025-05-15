from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 5
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_display()

    def update_display(self):
        self.clear()
        self.goto(-350, 260)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 18, "bold"))
        self.goto(350, 260)
        self.write(f"Lives: {self.lives}", align="right", font=("Courier", 18, "bold"))
        self.goto(-350, 270)  # Score
        self.goto(350, 270)  # Lives

    def increase_score(self):
        self.score += 1
        self.update_display()

    def lose_life(self):
        self.lives -= 1
        self.update_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

    def show_win_message(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Courier", 36, "bold"))
