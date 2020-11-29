from pico2d import *
import gfw
import random

MOVE_FPS=2

class Enemy:
    def __init__(self,pos,delta):
        self.init(pos,delta,'res/enemy.png')
        mag = random.uniform(0.2,0.5)
        self.radius = mag * self.image.h//2
        self.time = get_time()
        self.FPS = random.uniform(5.0,10.0)
        pos = self.pos
        self.hp = 700

    def init(self, pos,delta, imageName):
        self.pos =pos
        self.delta =delta
        self.image = gfw.image.load(imageName)
        self.radius = self.image.h//2
        self.fcount = self.image.w//self.image.h//2

    def update(self):
        x,y =self.pos
        dx,dy = self.delta
        x -= dx * MOVE_FPS 
        
        self.pos = x,y
        if not self.in_boundary():
            gfw.world.remove(self)

    def draw(self):
        self.image.draw(*self.pos)

    def remove(self):
        gfw.world.remove(self)
    
    def decrease_hp(self, amount):
        self.hp -= amount
        return self.hp <= 0
        
    def in_boundary(self):
        x,y =self.pos
        if x < -self.radius : return False
        if y < -self.radius : return False
        if x > get_canvas_width() + self.radius : return False
        if y > get_canvas_height() + self.radius : return False

        return True
    
    def get_bb(self):
        x,y=self.pos
        hw = self.image.w//2
        hh = self.image.h//2
        return x-hw,y-hh,x+hw,y+hh

class E_can(Enemy):
    def __init__(self,pos,delta):
        self.init(pos,delta,'res/item.png')
