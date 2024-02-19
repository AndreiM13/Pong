from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(4, 1)
        self.penup()
        self.new_position(0,0 )



    def new_position(self,new_x,new_y):
        self.setposition(new_x, new_y)

    def go_Up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

