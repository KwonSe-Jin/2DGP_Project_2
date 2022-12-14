from pico2d import *
import game_framework
import title_state
import Ball
class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.bgm = load_music('bgm.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400, 300)


    def update(self):
        pass
class Net:
    def __init__(self):
        self.net = load_image('NetBottom.png')
        self.x = 400
        self.y = 120
    def draw(self):
        self.net.draw(self.x, self.y)
    def update(self):
        pass
    def get_bb(self):
        return self.x - 5, self.y - 110, self.x + 5, self.y + 110

class NetTop:
    def __init__(self):
        self.net = load_image('NetTop.png')
        self.x = 400
        self.y = 250
    def draw(self):
        self.net.draw(self.x, self.y)
    def update(self):
        pass
    def get_bb(self):
        return self.x - 18, self.y - 15, self.x + 18, self.y + 15