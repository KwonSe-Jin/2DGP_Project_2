from pico2d import*
import collision
import os
import play_state

class Squirtle:
    def __init__(self):
        self.x = 650
        self.y = 70
        self.frame = 0
        self.frame2 = 5
        self.image = load_image('Squirtle.png')
        self.dirx = 0
        self.diry = 0
        self.jump = 0
        self.locate = 0
        self.win = False
        self.lose = False
        self.c = 0

    def update(self):
        self.frame = (self.frame + 1) % self.frame2
        if self.lose == False and self.win == False:
            self.x += self.dirx * 5
            if self.jump == 1:
                self.y += 15
                if self.y >= 400:
                    self.jump = -1
            elif self.jump == -1:
                self.y -= 15
                if self.y <= 70:
                    self.jump = 0
            else:
                self.y = 70
            if (collision.collide(play_state.squirtle, play_state.net)):
                play_state.squirtle.x = 450
        if (play_state.point.Lpoint == 2):
            self.lose = True
            self.locate = 5
            self.frame2 = 5
            self.time = 0
        elif (play_state.point.Rpoint == 2):
            self.win = True
            self.locate = 4
            self.frame2 = 3
            self.time = 0

    def draw(self):
        if self.lose == False and self.win == False:
            if self.locate:
                self.image.clip_draw(self.frame * 64, self.locate * 64, 64, 64, self.x, self.y, 120, 120)
            else:
                self.image.clip_draw(0, 0, 64, 64, self.x, self.y, 120, 120)
        elif self.win == True:
            self.image.clip_draw(self.frame * 64, self.locate * 64, 64, 64, self.x, self.y, 120, 120)
            delay(0.05)
        elif self.lose == True:
            self.image.clip_draw(256, self.locate * 64, 64, 64, self.x, self.y, 120, 120)
            delay(0.05)

    def get_bb(self):
        return self.x - 40, self.y - 30, self.x + 10, self.y + 40