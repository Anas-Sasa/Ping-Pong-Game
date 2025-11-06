
"""
paddle.py

Defines the Paddle class for a simple paddle object using the turtle graphics library.

Classes:
    Paddle -- Subclasses turtle.Turtle to create a rectangular paddle with
              adjustable height, movement flags, and methods to move in response
              to key press/release events.

Usage:
    from paddle import Paddle
    left_paddle = Paddle(color="white", position=(-350, 0), width=5)
    right_paddle = Paddle(color="white", position=(350, 0), width=5)
"""



from turtle import Turtle

class Paddle(Turtle):

    """
    A Turtle-based paddle for a pong-like game.

    Parameters
    ----------
    color : str
        The color used to color the paddle.
    position : tuple
        (x, y) coordinates to place the paddle initially.
    width : float
        Vertical stretch factor for the paddle height (shapesize stretch_wid).
    """
        

    def __init__(self, color, position, width):

        # Initialize the parent Turtle class
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid= width, stretch_len= 0.5)
        self.penup()
        self.color(color)
        self.goto(position)

        # Movement speed in pixels per move
        self.r_speed_paddle = 30

        # Flags used to track continuous movement from key press/release events
        self.move_up = False
        self.move_down = False

    # Input handlers: set movement flags when keys are pressed or released
    def press_up(self):
        """
        Set the flag to start moving the paddle upward."""
        self.move_up = True

    def release_up(self):
        """
        Clear the upward movement flag to stop upward movement."""
        self.move_up = False

    def press_down(self):
        """
        Set the flag to start moving the paddle downward."""
        self.move_down = True

    def release_down(self):
        """
        Clear the downward movement flag to stop downward movement."""
        self.move_down = False


    def move_paddle(self):

        """
        Move the paddle based on current movement flags.

        Moves up if move_up is True and the paddle is below the upper boundary.
        Moves down if move_down is True and the paddle is above the lower boundary.
        Boundaries prevent the paddle from leaving the visible play area.
        """

        # Move up: check flag and top boundary (y < 325)
        if self.move_up and self.ycor() < 325:
            self.goto(x= self.xcor(), y= self.ycor() + self.r_speed_paddle)

        # Move down: check flag and bottom boundary (y > -325)
        if self.move_down and self.ycor() > - 325:
            self.goto(x= self.xcor(), y= self.ycor() - self.r_speed_paddle)
