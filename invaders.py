from turtle import Turtle


class Invader(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.setheading(270)
        self.pu()
        self.goto(pos)

        self.radius = 10
        self.move_val_x = 1
        self.move_val_y = 1
        self.move_speed = 0.1

        self.x_min = pos[0] - 30
        self.x_max = pos[0] + 30

    def move(self):
        x = self.xcor() + self.move_val_x * self.move_speed
        if x < self.x_min or x > self.x_max:
            self.move_val_x *= -1
        y = self.ycor() - self.move_val_y * self.move_speed
        self.goto(x, y)

    def destroy(self):
        self.hideturtle()
        self.goto(-500, -500)


class AlienSmall(Invader):
    def __init__(self, pos):
        super().__init__(pos)
        self.shape("img/invader_small_glow.gif")
        # self.setheading(270)
        # self.pu()
        # self.goto(pos)

        self.x_min = pos[0] - 30
        self.x_max = pos[0] + 30
        # self.radius = 10
        # self.move_val_x = 1
        # self.move_val_y = 1
        self.move_speed = 0.1


class AlienMiddle(Invader):
    def __init__(self, pos):
        super().__init__(pos)
        self.shape("img/Alien_xs.gif")

        self.radius = 20
        # self.x_min = pos[0] - 30
        # self.x_max = pos[0] + 30



class AlienGreen(Invader):
    def __init__(self, pos):
        super().__init__(pos)
        self.shape("img/Alien_xs.gif")

        self.radius = 20
        # self.x_min = pos[0] - 30
        # self.x_max = pos[0] + 30


