from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard(3)
        pad_life = Turtle()
        pad_life.shape("square")
        pad_life.penup()
        pad_life.color("white")
        pad_life.shapesize(stretch_len=3, stretch_wid=0.5)
        pad_life.goto(380,410)
        upper_border = Turtle()
        upper_border.shape("square")
        upper_border.penup()
        upper_border.color("silver")
        upper_border.shapesize(stretch_len=120, stretch_wid=0.05)
        upper_border.goto(-545, 393)
        upper_border2 = Turtle()
        upper_border2.shape("square")
        upper_border2.penup()
        upper_border2.color("grey")
        upper_border2.shapesize(stretch_len=120, stretch_wid=0.05)
        upper_border2.goto(-545, 394)
        upper_border3 = Turtle()
        upper_border3.shape("square")
        upper_border3.penup()
        upper_border3.color("grey")
        upper_border3.shapesize(stretch_len=120, stretch_wid=0.05)
        upper_border3.goto(-545, 395)



    def update_scoreboard(self, life):
        self.clear()
        self.goto(0, 400)
        self.color("red")
        self.write("ARKANOID", align="center", font=("Courier", 30, "bold"))
        self.color("white")
        self.goto(-420, 410)
        self.write("Your score is:", align="center", font=("Courier", 16, "bold"))
        self.color("yellow")
        self.goto(-310, 405)
        self.write(self.score, align="center", font=("Courier", 20, "bold"))
        self.goto(440, 400)
        self.write(f"x {life}", align="center", font=("Courier", 16, "bold"))



    def point(self, life):
        self.score += 1
        self.update_scoreboard(life)
