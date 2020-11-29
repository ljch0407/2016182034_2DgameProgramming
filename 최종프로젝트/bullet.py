from pico2d import*
import gfw
from gobj import *


class bullet:
    size = 15
    def __init__(self,x,y,speed):
        global pos
        self.pos=x,y
        pos = self.pos
        self.dx= speed
        self.image = gfw.image.load(RES_DIR+'/bullet.png')
        self.power =100
        self.fidx = 0
        self.radius = 15
        radius = self.radius
       

    def draw(self):
        self.image.clip_draw(self.fidx,0,10,10,*self.pos,bullet.size,bullet.size)
        
    def update(self):
        x,y = self.pos
        x +=self.dx * gfw.delta_time
        self.fidx=(self.fidx+1)%3
        if x>get_canvas_width()+bullet.size:
            self.remove()
        self.pos = x,y
        

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        x,y=self.pos
        hw = self.image.w//2
        hh = self.image.h//2
        return x-hw,y-hh,x+hw,y+hh
