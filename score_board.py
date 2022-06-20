from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setposition(0, 280)
        self.score_board()

    def score_board(self):
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
