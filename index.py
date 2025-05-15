import time
import pygame
from turtle import Screen
from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard


class BreakoutGame:
    def __init__(self):
        pygame.mixer.init()
        self.screen = Screen()
        self.setup_screen()
        
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = Bricks()
        self.scoreboard = Scoreboard()
        self.scoreboard.load_high_score()
        
        self.game_is_on = False
        self.setup_controls()
    
    def setup_screen(self):
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Breakout Pro")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.cv._rootwindow.resizable(False, False)
    
    def setup_controls(self):
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.onkeyrelease(self.paddle.stop, "Left")
        self.screen.onkeyrelease(self.paddle.stop, "Right")
        self.screen.onkeypress(self.start_game, "space")
        self.screen.onkeypress(self.reset_game, "Return")
    
    def start_game(self):
        if not self.game_is_on:
            self.game_is_on = True
            self.game_loop()
    
    def reset_game(self):
        if not self.game_is_on:
            self.ball.reset_position()
            self.paddle.goto(0, -250)
            self.bricks.clear()
            self.bricks.create_all_lanes()
            self.scoreboard.reset()
            self.screen.update()
    
    def check_paddle_collision(self):
        paddle_left, paddle_right, paddle_top, _ = self.paddle.get_bounding_box()
        ball_left, ball_right, ball_top, ball_bottom = self.ball.get_bounding_box()
        
        if (ball_bottom <= paddle_top and
                ball_right > paddle_left and
                ball_left < paddle_right):
            hit_position = (self.ball.xcor() - self.paddle.xcor()) / (self.paddle.width / 2)
            self.ball.x_move = hit_position * 12
            self.ball.y_move = abs(self.ball.y_move)
            self.ball.bounce_y()
            return True
        return False
    
    def check_wall_collision(self):
        ball_left, ball_right, ball_top, ball_bottom = self.ball.get_bounding_box()
        
        if ball_left < -390 or ball_right > 390:
            self.ball.bounce_x()
        
        if ball_top > 290:
            self.ball.bounce_y()
        
        if ball_bottom < -290:
            if self.scoreboard.lose_life():
                self.scoreboard.save_high_score()
                self.scoreboard.game_over()
                self.game_is_on = False
            else:
                self.ball.reset_position()
                time.sleep(1)
    
    def play_sound(self, file):
        try:
            pygame.mixer.Sound(file).play()
        except:
            pass
    
    def game_loop(self):
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            
            self.paddle.move()
            self.ball.move()
            
            self.check_wall_collision()
            self.check_paddle_collision()
            
            bounce_direction, points = self.bricks.check_collision(self.ball)
            if points > 0:
                self.scoreboard.increase_score(points)
                self.play_sound("brick_hit.wav")
            
            if bounce_direction == "x":
                self.ball.bounce_x()
                self.ball.increase_speed()
            elif bounce_direction == "y":
                self.ball.bounce_y()
                self.ball.increase_speed()
            
            if len(self.bricks.bricks) == 0:
                self.scoreboard.level_complete()
                self.game_is_on = False
        
        self.screen.update()
    
    def run(self):
        self.screen.update()
        self.screen.mainloop()


if __name__ == "__main__":
    game = BreakoutGame()
    game.run()
