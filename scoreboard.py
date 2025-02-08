from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        """Scoreboard class inherits the Turtle class"""
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=-10, y=270)
        self.display_score(0)

    def display_score(self, score):
        """The score of the player will be displayed at the top of the screen"""
        self.clear()
        self.write(arg=f"Score: {score}", align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        """Game over message will be displayed at the center of the screen"""
        self.goto(x=0, y=0)
        self.write(arg="Game over", align="center", font=("Courier", 15, "bold"))