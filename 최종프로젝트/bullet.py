from pico2d import*
import gfw
from gobj import *

class bullet:
    size = 15
    def __init__(self,x,y,speed):
        global pos,radius
        self,pos=x,y
        pos = self.pos
        self.dx= speed
        self.image = gfw.image.load(RES_DIR+'/bullet.png')
        self.power =100
        self.fidx = 0
        self.radius = 15
        radius = self.radius
       

    def draw(self):
        self.image.clip_draw(self.fidx,0,10,10,self.x,self.y,bullet.size,bullet.size)
        
    def update(self):
        self.x +=self.dx * gfw.delta_time
        self.fidx=(self.fidx+1)%3
        if self.x>get_canvas_width()+bullet.size:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w//2
        hh = self.image.h//2
        return self.x-hx, self.y-hh,self.x+hw,self.y+hh
