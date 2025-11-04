from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, color, position, width):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid= width, stretch_len= 0.5)
        self.penup()
        self.color(color)
        self.goto(position)
        self.r_speed_paddle = 30
        self.move_up = False
        self.move_down = False


    def press_up(self):
        self.move_up = True

    def release_up(self):
        self.move_up = False

    def press_down(self):
        self.move_down = True

    def release_down(self):
        self.move_down = False

    def move_paddle(self):

        if self.move_up and self.ycor() < 325:
            self.goto(x= self.xcor(), y= self.ycor() + self.r_speed_paddle)


        if self.move_down and self.ycor() > - 325:
            self.goto(x= self.xcor(), y= self.ycor() - self.r_speed_paddle)
