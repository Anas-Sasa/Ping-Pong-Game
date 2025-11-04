from turtle import Turtle

class Score(Turtle):
    
    def __init__(self, color, position):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color(color)
        self.goto(position)
        self.update_score(score= self.r_score)
        self.update_score(score= self.l_score)



    def increase_player_point(self):
        self.r_score += 1
        self.update_score(score= self.r_score)

    def increase_computer_point(self):
        self.l_score += 1
        self.update_score(score= self.l_score)

    def update_score(self, score):

        self.clear()
        self.write(f"Score\n [{score}]", font=("courier", 20, 'bold'), align= 'center')





        