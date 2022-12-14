import collision
from pico2d import *
import play_state
import game_world
import select
class Ball:
    def __init__(self):
       self.image = load_image('ball.png')
       self.frame = 0
       self.x = 150
       self.y = 500
       self.to_x = 0
       self.to_y = 6
       self.init_spd_y = 6
       self.touch = load_wav('touch.wav')
       self.spike = load_wav('spike.wav')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def draw(self):
        self.image.clip_draw(self.frame * 40, 0, 40, 40, self.x, self.y, 50, 50)

    def update(self):
        if game_world.objects[1][0].win == True or game_world.objects[1][0].lose == True:
            game_world.remove_object(self)
        self.frame = (self.frame + 1) % 5
        if play_state.pikachu.z == 1:
            if (collision.collide(self, play_state.pikachu)):
                    self.init_spd_y = 20
                    self.to_x = 5
                    self.to_y = self.init_spd_y
                    self.touch.play(1)
                    self.touch.set_volume(40)
                    if(play_state.pikachu.jump == 1):
                        self.init_spd_y = 30
                        self.to_x = 23
                        self.to_y = self.init_spd_y
                        if(play_state.pikachu.locate == 6):
                            self.init_spd_y = 40
                            self.to_x = 40
                            self.to_y = self.init_spd_y
                            self.spike.play(1)
                            self.spike.set_volume(60)
            if (collision.collide(self, play_state.pikachu2)):
                    self.init_spd_y = 20
                    self.to_x = -5
                    self.to_y = self.init_spd_y
                    self.touch.play(1)
                    self.touch.set_volume(40)
                    if(play_state.pikachu2.jump == 1):
                        self.init_spd_y = 30
                        self.to_x = -23
                        self.to_y = self.init_spd_y
                        if (play_state.pikachu2.locate == 6):
                            self.init_spd_y = 40
                            self.to_x = -40
                            self.to_y = self.init_spd_y
                            self.spike.play(1)
                            self.spike.set_volume(60)
        if play_state.squirtle.c == 1:
            if (collision.collide(self, play_state.squirtle)):
                    self.init_spd_y = 20
                    self.to_x = -5
                    self.to_y = self.init_spd_y
                    if(play_state.squirtle.jump == 1):
                        self.init_spd_y = 30
                        self.to_x = -23
                        self.to_y = self.init_spd_y
                        if (play_state.squirtle.locate == 6):
                            self.init_spd_y = 40
                            self.to_x = -40
                            self.to_y = self.init_spd_y

            if (collision.collide(self, play_state.squirtle2)):
                    self.init_spd_y = 20
                    self.to_x = 5
                    self.to_y = self.init_spd_y
                    if (play_state.squirtle2.jump == 1):
                        self.init_spd_y = 30
                        self.to_x = 23
                        self.to_y = self.init_spd_y
                        if (play_state.squirtle2.locate == 6):
                            self.init_spd_y = 40
                            self.to_x = 40
                            self.to_y = self.init_spd_y








        if (collision.collide(self, play_state.netTop)):
            self.to_x = -self.to_x
            self.to_y = 5

        if (collision.collide(self, play_state.net)):
            self.to_x = -self.to_x
            self.to_y = -16

        if self.x <= 50 or self.x >= 750:
            self.to_x = -self.to_x
        if self.y < 40:
            self.to_y = self.init_spd_y
            self.init_spd_y -= 2
        else:
            self.to_y -= 0.5
        if self.y >= 580:
            self.to_y = -self.to_y
        self.x += self.to_x
        self.y += self.to_y

