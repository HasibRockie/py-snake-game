from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,200)
        self.initial()

    def Update_score(self):
        self.score +=1

        self.write(f"Your score:{self.score}", align='center', font=('Arial', 15))

    def initial(self):
        self.write(f"Your score:{self.score}", align='center', font=('Arial', 15))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game over!!", align='center', font=('Arial', 15))
