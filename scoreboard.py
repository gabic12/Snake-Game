from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        """Scoreboard class inherits the Turtle class"""
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=-10, y=270)
        with open("high_score.txt") as file: #High score is located in the high_score.txt file
            self.high_score = int(file.read())
        self.display_score(0)

    def display_score(self, score):
        """The score of the player will be displayed at the top of the screen"""
        self.clear()
        self.write(arg=f"Score: {score} High score: {self.high_score}", align="center", font=("Courier", 15, "bold"))

    def game_over(self, new_high_score):
        """Game over message will be displayed at the center of the screen and the new high score will pe updated in the file"""
        self.goto(x=0, y=0)
        self.write(arg="Game over", align="center", font=("Courier", 15, "bold"))
        if new_high_score > self.high_score: #Check the high score and update it in file, if necessary
            with open("high_score.txt", mode="w") as file:
                file.write(str(new_high_score))