from turtle import Turtle

COLORS = ["#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", "#845EC2"]


class Bricks:
    def __init__(self):
        self.all_bricks = []
        self.create_bricks()
    
    def create_bricks(self):
        brick_width = 50
        brick_height = 20
        horizontal_spacing = 10
        vertical_spacing = 2
        
        x_start = -400 + (brick_width / 2)
        y_start = 200
        cols = 13  # Reduced to fit with spacing
        rows = len(COLORS) * 2
        
        for row in range(rows):
            y = y_start - row * (brick_height + vertical_spacing)
            color = COLORS[row % len(COLORS)]  # Use modulus to cycle through colors
            for col in range(cols):
                x = x_start + col * (brick_width + horizontal_spacing)
                brick = Turtle("square")
                brick.color(color)
                brick.shapesize(stretch_wid=1, stretch_len=2.5)
                brick.penup()
                brick.goto(x, y)
                self.all_bricks.append(brick)
