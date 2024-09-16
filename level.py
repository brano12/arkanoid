import time
import random
from turtle import Turtle, Screen


sc = Screen()
life_gif = ("zivot.gif")
sc.register_shape(life_gif)

slowball_gif = ("pomala_lopta.gif")
sc.register_shape(slowball_gif)

fastball_gif = ("rych_lopta_surp.gif")
sc.register_shape(fastball_gif)

long_paddle_sur_gif = ("padlo_surp.gif")
sc.register_shape(long_paddle_sur_gif)

short_paddle_sur_gif = ("kr_padlo_surp.gif")
sc.register_shape(short_paddle_sur_gif)

class Level():

    bricks_surprise_list = []


    def __init__(self):
        self.wall = self.build_wall()
        self.level_sur_list = []
        self.hit_brick_counter = 0

    def build_wall(self):
        wall = []
        Level.bricks_surprise_list = ["short_paddle", "long_paddle", "_empty_", "_empty_", "_empty_", "_empty_","_empty_" ,
                                      "_empty_", "_empty_", "_empty_", "_empty_","_empty_", "_empty_", "life", "_empty_",
                                      "_empty_", "_empty_", "_empty_", "_empty_", "_empty_", "_empty_", "faster_ball",
                                      "_empty_", "_empty_", "_empty_", "_empty_", "slower_ball", "_empty_", "_empty_", "_empty_"]


        color_list = []
        for i in range(0,8):
            color = random.choice(["red", "blue", "white", "yellow", "green", "orange", "purple", "brown"])
            if i == 1:
                color_list.append(color_list[0])
            elif i == 2:
                while color == color_list[1]:
                    color = random.choice(["red", "blue", "white", "yellow", "green", "orange", "purple", "brown"])
                color_list.append(color)
            elif i == 3 or i == 4:
                color_list.append(color_list[2])
            elif i == 5:
                while color == color_list[4] or color == color_list[0]:
                    color = random.choice(["red", "blue", "white", "yellow", "green", "orange", "purple", "brown"])
                color_list.append(color)
            elif  i == 6 or i == 7:
                color_list.append(color_list[5])
            else:
                color_list.append(color)

        for digit in range(0, 8):
            for num in range(-10, 990, 90):
                wall.append(Brick((-490 + num, 50 + digit * 40), color_list[digit]))

        return wall

    def reset_wall(self):
        for item in self.wall:
            item.reset()

    def add_surprise(self, brick_position, brick):

        if brick != "_empty_":
            if brick == "life":
                shape = life_gif
            elif brick == "slower_ball":
                shape = slowball_gif
            elif brick == "faster_ball":
                shape = fastball_gif
            elif brick == "long_paddle":
                shape = long_paddle_sur_gif
            elif brick == "short_paddle":
                shape = short_paddle_sur_gif
            self.level_sur_list.append(Surprise(shape, brick_position,brick))

        # for item in self.level_sur_list:
        #     print(item.name)


    def up_life(self, life):
            life += 1

class Brick(Turtle):


    def __init__(self, starting_pos, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.shapesize(stretch_len=4, stretch_wid=1.5)
        self.goto(starting_pos)
        self.surprise = None
        self.hit = False
        self.choose_sur()

    def choose_sur(self):
        sur_tuple = tuple(Level.bricks_surprise_list)
        surprise = random.choice(sur_tuple)

        if surprise != "_empty_":
            Level.bricks_surprise_list.remove(surprise)

        self.surprise = surprise


class Surprise(Turtle):

    def __init__(self, shape, starting_pos, name):
        super().__init__()
        self.shape(shape)
        self.right(90)
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.goto(starting_pos)
        self.y_move = -7
        self.name = name
       # self.hideturtle()

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
