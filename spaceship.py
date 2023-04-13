from turtle import Turtle

Y_START = -260
X_MIN = -300
X_MAX = 300

BLAST_SPEED = 5


class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("img/spaceship_xs.gif")
        self.resizemode("user")
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.showturtle()
        # look "up"
        self.setheading(90)
        self.pu()
        self.goto(0, Y_START)
        self.radius = 10

        self.move_x = 15

    def move_left(self):
        if self.xcor() > X_MIN:
            new_x = self.xcor() - self.move_x
            self.hideturtle()
            self.goto(new_x, Y_START)
            self.showturtle()

    def move_right(self):
        if self.xcor() < X_MAX:
            new_x = self.xcor() + self.move_x
            self.hideturtle()
            self.goto(new_x, Y_START)
            self.showturtle()

    def destroy(self):
        self.hideturtle()




class Blast(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.pu()
        self.shapesize(stretch_wid=0.15, stretch_len=0.15)
        self.goto(pos)
        if self.ycor() <= Y_START + 5 :
            self.setheading(90)
        else:
            self.setheading(270)
        self.move_val = BLAST_SPEED
        self.radius = 2

    def move(self):
        self.forward(self.move_val)

    def destroy(self):
        self.hideturtle()
        self.goto(-500, -500)
