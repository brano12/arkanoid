import time
from turtle import Turtle
import random

def sig_num(num):
    if num > 0:
        return 1
    else:
        return -1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        #self.move_coef = 5
        self.x_move = random.choice([-7,7])
        self.y_move = -7
        self.timer = 0.04
        self.timer_int = 0
        self.allow_bounce = True
        self.goto(0,-40)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
  #      self.timer *= 0.75

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,-40)
        self.timer_int = 0
        self.x_move = random.choice([-7,7])
        self.y_move = -7

    def slow_ball(self):
        self.timer_int = 0
        self.x_move = sig_num(self.x_move) * 3.5
        self.y_move = sig_num(self.y_move) * 3.5

    def fast_ball(self):
        self.timer_int = 7
        self.x_move = sig_num(self.x_move) * 17
        self.y_move = sig_num(self.y_move) * 17