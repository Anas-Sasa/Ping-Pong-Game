"""
score.py

Defines the Score class for displaying and updating a player's score using turtle graphics.

Classes:
    Score -- A lightweight Turtle subclass that tracks left and right scores,
             displays them at a given position, and provides methods to increment
             and refresh the displayed score.

Usage:
    from score import Score
    score_display = Score(color="white", position=(0, 200))
    score_display.increase_player_point()
    score_display.increase_computer_point()
"""


from turtle import Turtle

class Score(Turtle):

    """
    A Turtle-based score display.

    Keeps two integer counters (left and right), draws the current score on the
    screen at the provided position, and provides methods to increment each
    counter and refresh the displayed value.

    Parameters
    ----------
    color : str
        The color used to write the score on the screen.
    position : tuple
        (x, y) coordinates where the score will be displayed.
    """
    
    def __init__(self, color, position):

        # Initialize the parent Turtle class
        super().__init__()

        # Score counters for left and right players (start at zero)
        self.l_score = 0
        self.r_score = 0

        self.hideturtle()
        self.penup()
        self.color(color)
        self.goto(position)


        # Draw the initial scores (right and left). Each call clears and writes,
        # so calling twice will result in the last written value visible.
        # We keep to the same API as update_score to ensure consistent rendering
        self.update_score(score= self.r_score)
        self.update_score(score= self.l_score)



    def increase_player_point(self):
        """
        Increment the right player's score by one and update the display.
        """

        # Increase right player score
        self.r_score += 1

        # Refresh the shown score
        self.update_score(score= self.r_score)


    def increase_computer_point(self):
        """
        Increment the left player's score by one and update the display.
        """

        # Increase left player score
        self.l_score += 1

        # Refresh the shown score
        self.update_score(score= self.l_score)

    def update_score(self, score):

        """
        Clear any previous text and write the provided score at the current position.

        Parameters
        ----------
        score : int
            The numeric value to display.
        """

        self.clear()

        # Write the score text centered at the turtle's current position
        self.write(f"Score\n [{score}]", font=("courier", 20, 'bold'), align= 'center')
