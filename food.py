from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        """Food class inherits the Turtle class"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("white")
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        """Spawn the food at a random location on the screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)