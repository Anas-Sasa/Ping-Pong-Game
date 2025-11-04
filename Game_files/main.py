from turtle import Screen
from paddle import Paddle
from ball import Ball
from boardscore import Score
import random, time, os

def sleep(second ):
    time.sleep(second)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

clear_terminal()


colors = [

    ["Green", "Black"],["Dark Blue", "Light Cyan"], 

    ["Red", "White"],["Purple", "Gold"],   

    ["dim gray", "Orange"],["Teal", "Yellow"]  ]

game_running = True
default_time = 0.03

loss_distance = [  40, 40, 40, 40, 40, 40, 65, 65, 40, 40, 40, 40,40,40]

style_color = random.choice(colors)

screen = Screen()
screen.title("Ping Pong‼️ 🥅 🥅 😎")
screen.setup(width= 990, height= 800)
# screen.bgpic("pingpong.gif")
screen.bgcolor(style_color[0])
screen.tracer(0)

r_paddle = Paddle(color= style_color[1], position= (470, 0), width= 6)

l_paddle = Paddle(color= style_color[1], position= (-475, 0), width= 5)

ball = Ball(style_color[1])

player_score = Score(color= style_color[1], position= ( 200, 330 ))

computer_score = Score(color= style_color[1], position= ( -200, 330 ))


# Get the underlying Tkinter window
tk_window = screen.getcanvas().winfo_toplevel()

# Handle window close button
def on_close():

    global game_running

    game_running = False
    ball.hideturtle()
    ball.color("white")
    ball.goto(0, 220)
    ball.write("Click On Screen To Exit...", font= ("courier", 25, "normal"), align= "center")

    # tk_window.destroy()

tk_window.protocol("WM_DELETE_WINDOW", on_close)



while game_running:

    screen.update()
    
    sleep(default_time)

    ball.goto(x= ball.xcor() + ball.move_xcor, y= ball.ycor() + ball.move_ycor)

    if ball.ycor() >= 385 or ball.ycor() <= -385:

        ball.move_ycor *= -1

    if ball.xcor() > 450 and ball.xcor() < 470 and ball.distance(r_paddle) <= 65 or ball.xcor() <= -455 and ball.xcor() >= -480 and ball.distance(l_paddle) < 55:

        ball.move_xcor *= -1

        default_time *= 0.9

        random.shuffle(loss_distance)
        

    if ball.xcor() > 500:
        
        ball.home()
        
        ball.move_xcor *= -1

        ball.move_ycor *= -1

        default_time = 0.03

        computer_score.increase_computer_point()

        random.shuffle(loss_distance)


    if ball.xcor() < -500:
        
        ball.home()

        ball.move_xcor *= -1

        ball.move_ycor *= -1

        default_time = 0.03

        player_score.increase_player_point()

        random.shuffle(loss_distance)



    screen.listen()

    screen.onkeypress(r_paddle.press_up, "Up")
    screen.onkeyrelease(r_paddle.release_up, "Up")

    screen.onkeypress(r_paddle.press_down, "Down")
    screen.onkeyrelease(r_paddle.release_down, "Down")

    r_paddle.move_paddle()

    if ball.xcor() < 0:
        l_paddle.goto(x= l_paddle.xcor(), y= ball.ycor() - loss_distance[0])
    else:
        l_paddle.goto(l_paddle.xcor(), 0)
   

    if l_paddle.ycor() < -350:
        l_paddle.goto(l_paddle.xcor(), -350)
  
screen.exitonclick()