from turtle import Turtle


class Ball(Turtle):

    def __init__(self, color):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=0.8, stretch_len= 0.8)
        self.move_ycor = 10
        self.move_xcor = 10