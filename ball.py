from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.12

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.setx(0)
        self.sety(0)
        self.move_speed = 0.12
        self.x_move *= -1
        self.y_move *= -1

