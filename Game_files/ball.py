"""
ball.py

This module defines the Ball class, which represents a movable ball object using Python's turtle graphics.

Classes:
    Ball -- Inherits from turtle.Turtle and initializes a circular ball with custom size, color, and movement attributes.

Usage:
    Import the Ball class and create an instance by specifying a color.
    Example:
        from ball import Ball
        ball = Ball("red")

Features:
    - Custom shape and size
    - Pen-up mode to prevent drawing
    - Movement attributes for x and y directions
"""


# Import the Turtle class from the turtle graphics module
from turtle import Turtle

# Define a Ball class that inherits from Turtle
class Ball(Turtle):

    def __init__(self, color):

        """
        Initializes a Ball object with specific visual properties and movement settings.

        Parameters:
        color (str): The color of the ball.
        """
        # Call the constructor of the parent Turtle class
        super().__init__()

        # Set the shape of the turtle to a circle to represent a ball
        self.shape("circle")

        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=0.8, stretch_len= 0.8)

        # Set the vertical movement increment
        self.move_ycor = 10

        # Set the horizontal movement increment
        self.move_xcor = 10