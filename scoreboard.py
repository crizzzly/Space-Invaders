from turtle import Turtle

P1SCORE_POSX = -250
P2SCORE_POSX = 250
HISCORE_POSX = 0
SCORE_POSY = - 300
TEXT_POSY = 320
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, pl):
        super().__init__()
        self.game_over = False
        self.color("white")
        self.penup()
        self.hideturtle()

        self.score = 0
        self.highscore = 0
        self.lives = 3
        self.level = 1
        self.player = pl
        self.hits = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        if self.player == 0:
            x = P1SCORE_POSX
            y = SCORE_POSY

            self.clear()
            self.goto(P1SCORE_POSX, TEXT_POSY)
            self.write(f"SCORE<1>", align="left", font=FONT)
            self.goto(HISCORE_POSX, TEXT_POSY)
            self.write("HI-SCORE", align="center", font=FONT)
            self.goto(P2SCORE_POSX, TEXT_POSY)
            self.write("SCORE<2>", align="right", font=FONT)

    def reset_scoreboard(self):
        pass

    def point(self, val):
        self.score += val
        self.update_scoreboard()

    def point_less(self):
        self.score -= 1
        self.update_scoreboard()

    def reduce_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        if self.level > 2:
            self.game_over = True
            self.reset_scoreboard()
            if self.score > self.highscore:
                self.highscore = self.score
