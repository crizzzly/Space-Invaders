#!/usr/bin/env python3.11
from turtle import Turtle, Screen
from spaceship import SpaceShip, Blast
from invaders import AlienSmall, AlienMiddle, AlienGreen
from random import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

LEFT_BORDER = -300
RIGHT_BORDER = -300
UPPER_BORDER = 300
LOWER_BORDER = -300

COL_FRAME = "#02f740"

ALIEN = "👾"


def is_collided_with(item_a, item_b):
    return abs(item_a.xcor() - item_b.xcor()) < item_b.radius and abs(item_a.ycor() - item_b.ycor()) < item_b.radius


class SpaceInvaders:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.register_shape("img/spaceship_xs.gif")
        self.screen.register_shape("img/invader_small_glow.gif")
        self.screen.register_shape("img/Alien_xs.gif")
        self.screen.register_shape("img/Alien_green_s.gif")
        # self.screen.register_shape("👾")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Space Invaders - By C.Rost")
        self.screen.tracer(0)

        self.ship = SpaceShip()

        self.screen.onkeypress(self.ship.move_left, "Left")
        self.screen.onkeypress(self.ship.move_right, "Right")
        self.screen.onkeypress(self.exit_game, "x")
        self.screen.onkeypress(self.fire, 'Up')
        self.screen.listen()

        self.game_is_on = True

        self.blasts = []
        self.invaders = []

        self.draw_game()
        self.start_game()



    def draw_game(self):
        # -- FRAME -- #
        frame = Turtle()
        frame.hideturtle()
        frame.color(COL_FRAME)
        frame.pu()
        frame.goto(LEFT_BORDER, LOWER_BORDER)
        frame.setheading(0)

        frame.pd()
        frame.begin_fill()
        for _ in range(2):
            frame.forward(SCREEN_WIDTH)
            frame.left(90)
            frame.forward(2)
            frame.left(90)
        frame.end_fill()
        frame.pu()

        # -- INVADERS -- #
        x_start = LEFT_BORDER + 50
        y_start = UPPER_BORDER - 50
        step = 48
        for el in range(11):
            x = x_start + el * step
            a = AlienSmall([x, y_start])
            self.invaders.append(a)
        for i in range(1, 3):
            for el in range(11):
                x = x_start + el * step
                y = y_start - i * step
                a = AlienMiddle([x, y])
                self.invaders.append(a)
        for i in range(3, 5):
            for el in range(11):
                x = x_start + el * step
                y = y_start - i * step
                a = AlienGreen([x, y])
                self.invaders.append(a)

        self.screen.update()

    @staticmethod
    def exit_game():
        exit(0)


    def fire(self, pos = None):
        print("fire")
        if pos is None:
            x1 = self.ship.xcor() - 15
            x2 = self.ship.xcor() + 12
            y = self.ship.ycor() + 5
        else:
            x1 = pos[0] - 15
            x2 = pos[0] + 12
            y = pos[1] - 5
        b1 = Blast([x1, y])
        b2 = Blast([x2, y])
        self.blasts.append(b1)
        self.blasts.append(b2)
        self.screen.update()


    def start_game(self):
        while self.game_is_on:

            # Move Blasts upwards
            if self.blasts:
                print(f'{len(self.blasts)} blasts')
                for blast in self.blasts:
                    blast.move()

                    # Destroy Blast if out of window
                    if not LOWER_BORDER < blast.ycor() < UPPER_BORDER:
                        print("blast destroy")
                        blast.destroy()
                        self.blasts.remove(blast)


            # Move Aliens downwards
            for alien in self.invaders:
                alien.move()
                # Check collision between blasts and alien
                for b in self.blasts:
                    if is_collided_with(b, alien):
                        alien.destroy()
                        b.destroy()
                        self.invaders.remove(alien)
                        self.blasts.remove(b)
                    if is_collided_with(b, self.ship):
                        print("collision with ship")
                        self.ship.destroy()
                        b.destroy()
                        self.blasts.remove(b)

            self.screen.update()

        self.screen.exitonclick()



if __name__ == "__main__":
    SpaceInvaders()
