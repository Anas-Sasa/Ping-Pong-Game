
"""
main.py

Simple Ping-Pong game using turtle graphics.

This module configures the game screen, initializes game objects (paddles,
ball, and score displays), and runs the main game loop. It also contains small
utility functions for sleeping and clearing the terminal, and handles the
window close event gracefully.

Usage:
    python main.py

Dependencies:
    - python turtle module (standard library)
    - paddle.py (Paddle class)
    - ball.py (Ball class)
    - boardscore.py (Score class)

Author: Anas
"""


# Import Screen from turtle to create and manage the game window
from turtle import Screen

# Import custom game objects implemented in separate modules
from paddle import Paddle
from ball import Ball
from boardscore import Score

# Import standard utilities: random for style/behavior variation,
# time for simple sleep wrapper, os for clearing the terminal if needed
import random, time, os

# Small wrapper around time.sleep to keep naming consistent in this module
def sleep(second ):
    time.sleep(second)

# Clear the terminal in a cross-platform way
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

clear_terminal()

# Predefined color palettes to pick a visual style for the game
colors = [

    ["Green", "Black"],["Dark Blue", "Light Cyan"], 

    ["Red", "White"],["Purple", "Gold"],   

    ["dim gray", "Orange"],["Teal", "Yellow"]  ]

# Game state control flag and default loop timing (seconds per frame)
game_running = True
default_time = 0.03

# Distances used by the simple AI paddle(computer) to follow the ball (shuffled during play)
loss_distance = [  40, 40, 40, 40, 40, 40, 65, 65, 40, 40, 40, 40,40,40]

# Choose a random color scheme for this session
style_color = random.choice(colors)

# Initialize the screen (game window)
screen = Screen()
screen.title("Ping Pong‼️ 🥅 🥅 😎")
screen.setup(width= 990, height= 800)

# Optionally set a background image instead of a plain color
screen.bgcolor(style_color[0])

# Turn off automatic screen updates; updates are done manually each frame
screen.tracer(0)

# Create paddles and ball using chosen color scheme and starting positions
r_paddle = Paddle(color= style_color[1], position= (470, 0), width= 6)

l_paddle = Paddle(color= style_color[1], position= (-475, 0), width= 5)

ball = Ball(style_color[1])


# Create score displays for player and computer at the top of the screen using chosen color scheme
player_score = Score(color= style_color[1], position= ( 200, 330 ))

computer_score = Score(color= style_color[1], position= ( -200, 330 ))


# Get the underlying Tkinter window intercept the window close event
tk_window = screen.getcanvas().winfo_toplevel()

# Graceful close handler: stop the main loop and show a message on the canvas
# Handle window close button
def on_close():

    global game_running

    game_running = False

    # Hide the ball and display an exit prompt
    ball.hideturtle()
    ball.color("white")
    ball.goto(0, 220)
    ball.write("Click On Screen To Exit...", font= ("courier", 25, "normal"), align= "center")

# Register the close handler to run when the window's close button is pressed
tk_window.protocol("WM_DELETE_WINDOW", on_close)


# Main game loop
while game_running:

    # Manually refresh the screen
    screen.update()
    
    # Control the frame rate
    sleep(default_time)

    # Move the ball according to its velocity attributes
    ball.goto(x= ball.xcor() + ball.move_xcor, y= ball.ycor() + ball.move_ycor)

    # Bounce off the top and bottom edges
    if ball.ycor() >= 385 or ball.ycor() <= -385:

        ball.move_ycor *= -1

    # Ball collides with a paddle region: reverse horizontal direction and speed up slightly
    if ball.xcor() > 450 and ball.xcor() < 470 and ball.distance(r_paddle) <= 65 or ball.xcor() <= -455 and ball.xcor() >= -480 and ball.distance(l_paddle) < 55:

        ball.move_xcor *= -1

        # Make the game slightly faster after a successful paddle hit
        default_time *= 0.9

        # Shuffle AI distances to vary computer reaction
        random.shuffle(loss_distance)
        
    # Ball passes the right edge: point for computer
    if ball.xcor() > 500:
        
        ball.home()
        
        # Reverse directions so the ball restarts toward the scoring side
        ball.move_xcor *= -1

        ball.move_ycor *= -1

        default_time = 0.03

        computer_score.increase_computer_point()

        random.shuffle(loss_distance)

    # Ball passes the left edge: point for player
    if ball.xcor() < -500:
        
        ball.home()

        # Reverse directions so the ball restarts toward the scoring side
        ball.move_xcor *= -1

        ball.move_ycor *= -1

        default_time = 0.03

        player_score.increase_player_point()

        random.shuffle(loss_distance)


    # Keyboard event bindings: set and clear paddle movement flags
    screen.listen()

    screen.onkeypress(r_paddle.press_up, "Up")
    screen.onkeyrelease(r_paddle.release_up, "Up")

    screen.onkeypress(r_paddle.press_down, "Down")
    screen.onkeyrelease(r_paddle.release_down, "Down")

    # Update right paddle position if input flags are set
    r_paddle.move_paddle()

    # Simple AI: move left paddle to follow the ball with an offset from loss_distance
    if ball.xcor() < 0:

        l_paddle.goto(x= l_paddle.xcor(), y= ball.ycor() - loss_distance[0])

    else: 
        # Return to center when ball is on the right side
        l_paddle.goto(l_paddle.xcor(), 0)
   
    # Keep left paddle within screen bounds
    if l_paddle.ycor() < -350:
        l_paddle.goto(l_paddle.xcor(), -350)
  
# Wait for a final click before closing the window
screen.exitonclick()