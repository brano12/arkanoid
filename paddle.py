from turtle import Turtle, Screen

sc = Screen()
paddle_gif = ("padlo.gif")
sc.register_shape(paddle_gif)

long_paddle_gif = ("dlhe_padlo.gif")
sc.register_shape(long_paddle_gif)

short_paddle_gif = ("krtk_padlo.gif")
sc.register_shape(short_paddle_gif)


class Paddle(Turtle):

    def __init__(self, starting_pos):
        super().__init__()
        self.shape(paddle_gif)
        self.penup()
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.color("white")
        self.speed("slow")
        self.goto(starting_pos)
        self.move_boundary = 460



    def move_left(self):
        new_x = self.xcor() - 40
        if self.xcor() < -self.move_boundary:
            pass
        else:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 40
        if self.xcor() > self.move_boundary:
            pass
        else:
            self.goto(new_x, self.ycor())

    def reset_shape(self):
        self.shape(paddle_gif)
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.move_boundary = 460


    def longer_shape(self):
        self.shape(long_paddle_gif)
        self.shapesize(stretch_len=10, stretch_wid=1)
        self.move_boundary = 420

    def shorter_shape(self):
        self.shape(short_paddle_gif)
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.move_boundary = 480