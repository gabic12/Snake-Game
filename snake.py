from turtle import Turtle
DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        """The snake will be composed of square segments measuring 20 pixels in length"""
        #The snake position is determined by the items in STARTING_POSITION list
        self.snake_segments_list = []

        for position in STARTING_POSITION:
            self.add_snake_segment(position)

        self.snake_head = self.snake_segments_list[0]

    def add_snake_segment(self, position):
        """Adds a new segment to the snake"""
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_segments_list.append(snake_segment)

    def increase_snake_size(self):
        """Adds a new segment at the end of the snake"""
        self.add_snake_segment(self.snake_segments_list[-1].position())

    def move(self):
        """The snake will start moving in a straight line"""
        for index in range(len(self.snake_segments_list) - 1, 0, -1):
            new_x = self.snake_segments_list[index - 1].xcor()
            new_y = self.snake_segments_list[index - 1].ycor()
            self.snake_segments_list[index].goto(new_x, new_y)
        self.snake_head.forward(DISTANCE)

    #          N = 90°
    #            |
    # W = 180° -- -- E = 0°
    #            |
    #          S = 270°

    def move_up(self):
        """The head of the snake will be facing north"""
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def move_down(self):
        """The head of the snake will be facing south"""
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def move_right(self):
        """The head of the snake will be facing east"""
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def move_left(self):
        """The head of the snake will be facing west"""
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)