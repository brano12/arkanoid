import random
import time
from turtle import Screen, Turtle, mainloop
from scoreboard import Scoreboard
from game import Game
from paddle import Paddle
from ball import Ball, sig_num
from level import Level

# pohyby, cierna vec asi napis v strede,vyhru

screen = Screen()
game = Game()

screen.setup(width=1100, height=950)
screen.bgcolor("black")
screen.title("Arkanoid")

screen.tracer(0)

############### Paddle

paddle = Paddle((0,-400))

############## Ball

ball = Ball()

############## Scoreboard

scoreboard = Scoreboard()

############## Level setting (Bricks and etc)

level1 = Level()

############## key bindings
def space_fun():
    game.pause = False
    game.new_game = True

def esc_fun():
    game.pause = False
    game.game_is_on = False

screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkey(space_fun, "space")
screen.onkey(esc_fun, "Escape")

screen.listen()

############# Start of a game

while game.game_is_on:

    time.sleep(ball.timer)
    screen.update()
    ball.move()
    for item in level1.level_sur_list:
        item.move()

    #detection collision with a ceiling

    if ball.ycor() > 378:
        ball.allow_bounce = True
        ball.bounce_y()

    # detection collision with a wall
    if ball.xcor() < -530 or ball.xcor() > 520:
        ball.allow_bounce = True
        ball.bounce_x()

    #detection collision with a paddle
    if ball.distance(paddle) < 40 and ball.ycor() > -415 and ball.allow_bounce == True:
        ball.timer_int +=1
        #print(ball.timer_int)
        ball.allow_bounce = False
        ball.bounce_y()

        if ball.timer_int == 10:
            ball.x_move = sig_num(ball.x_move) * 13
            ball.y_move = sig_num(ball.y_move) * 13

        elif ball.timer_int == 3:
            ball.x_move = sig_num(ball.x_move) * 9
            ball.y_move = sig_num(ball.y_move) * 9

    # detection collision of BONUS SURPRISE with a paddle
    for item in level1.level_sur_list:
        if item.distance(paddle) < 60 and item.ycor() > -415:

            if item.name == "life":
                game.add_life()
                scoreboard.update_scoreboard(game.life)
                item.goto(475, -545)
                item.hideturtle()

            if item.name == "slower_ball":
                ball.slow_ball()
                item.goto(475, -545)
                item.hideturtle()

            if item.name == "faster_ball":
                ball.fast_ball()
                item.goto(475, -545)
                item.hideturtle()

            if item.name == "long_paddle":
                paddle.longer_shape()
                item.goto(475, -545)
                item.hideturtle()

            if item.name == "short_paddle":
                paddle.shorter_shape()
                item.goto(475, -545)
                item.hideturtle()

        if item.ycor() < -430:
            item.goto(475, -545)
            item.hideturtle()

    #bouncing bricks
    for item in level1.wall:
        if ball.distance(item) < 45 and item.hit != True:
            ball.allow_bounce = True
            ball.bounce_y()

       #  checking whether surprise bonus  is in brick, if there is, surprise object will be created, added to the
        #  list of objects and start to fall down
            if item.surprise != "_empty_":
                 level1.add_surprise(item.pos(), item.surprise)

            item.hideturtle()
            item.hit = True
            level1.hit_brick_counter +=1
            scoreboard.point(game.life)


    #detect when paddle misses
    if ball.ycor() < -440:

        ball.reset_position()
        paddle.reset_shape()
        game.life -= 1
        scoreboard.update_scoreboard(game.life)

        for item in level1.level_sur_list:
            item.goto(475, -545)
            item.hideturtle()

    # winning of game
    if level1.hit_brick_counter == len(level1.wall):
        game.pause = True
        game.new_game = False
        ball.hideturtle()

        for item in level1.level_sur_list:
            item.hideturtle()

        game_over = Turtle()

        while game.pause:
            # we will use game_over turtle for statements, when win
            game_over.penup()
            game_over.hideturtle()
            game_over.goto(0, -100)
            game_over.color("yellow")
            game_over.write("Press SPACE if you want to play again or ESC to exit", align="center",
                            font=("Courier", 15, "bold"))
            game_over.goto(0, -100)
            game_over.color("red")
            game_over.write("YOU WON", align="center", font=("Courier", 100, "bold"))
            time.sleep(0.1)
            game_over.goto(0, -100)
            game_over.color("orange")
            game_over.write("YOU WON", align="center", font=("Courier", 100, "bold"))
            time.sleep(0.1)
            game_over.goto(0, -100)
            game_over.color("blue")
            game_over.write("YOU WON", align="center", font=("Courier", 100, "bold"))
            paddle.hideturtle()
            screen.update()

            if game.new_game:
                ball.showturtle()
                ball.reset_position()

                game.life = 3

                scoreboard.score = 0
                scoreboard.update_scoreboard(3)

                paddle.showturtle()
                paddle.goto((0, -400))
                game_over.reset()
                game_over.penup()
                game_over.goto(-550, -475)

                level1.reset_wall()
                level1 = Level()

                screen.update()

    if game.life == 0:

        game.pause = True
        game.new_game = False
        ball.hideturtle()

        for item in level1.level_sur_list:
            item.hideturtle()

        game_over = Turtle()

        while game.pause:

            game_over.penup()
            game_over.hideturtle()
            game_over.goto(0, -100)
            game_over.color("yellow")
            game_over.write("Press SPACE if you want to continue or ESC to exit", align="center", font=("Courier", 15, "bold"))
            game_over.goto(0,-100)
            game_over.color("red")
            game_over.write("GAME OVER", align="center", font=("Courier", 100, "bold"))
            time.sleep(0.1)
            game_over.goto(0, -100)
            game_over.color("orange")
            game_over.write("GAME OVER", align="center", font=("Courier", 100, "bold"))
            time.sleep(0.1)
            game_over.goto(0, -100)
            game_over.color("blue")
            game_over.write("GAME OVER", align="center", font=("Courier", 100, "bold"))
            paddle.hideturtle()
            screen.update()

            if game.new_game:
                ball.showturtle()
                ball.reset_position()

                game.life = 3

                scoreboard.score = 0
                scoreboard.update_scoreboard(3)

                paddle.showturtle()
                paddle.goto((0,-400))
                game_over.reset()
                game_over.penup()
                game_over.goto(-550, -475)

                level1.reset_wall()
                level1 = Level()

                screen.update()

screen.exitonclick()
mainloop()
