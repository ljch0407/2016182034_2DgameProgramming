from pico2d import *
import gfw
import random

MOVE_FPS=120

class Enemy:
    def __init__(self,pos,delta):
        self.init(pos,delta,'res/enemy.png')
        mag = random.uniform(0.2,0.5)
        self.radius = mag * self.image.h//2
        self.time = get_time()
        self.FPS = random.uniform(5.0,10.0)

    def init(self, pos,delta, imageName):
        self.pos =pos
        self.delta =delta
        self.image = gfw.image.load(imageName)
        self.radius = self.image.h//2
        self.fcount = self.image.w//self.image.h//2

    def update(self):
        x,y =self.pos
        dx = self.delta
        x -= dx * MOVE_FPS * gfw.delta_time()

        self.pos = x,y
        if not self.in_boundary():
            gfw.world.remove(self)

    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.FPS) % self.fcount
        src_size = self.image.h//2
        dst_size = self.radius *2*2
        self.image.clipdraw(src_size * fidx,0,src_size,src_size*2,*self.pos,dst_size,dst_size)

    def in_boundary(self):
        x,y =self.pos
        if x < -self.radius : return False
        if y < -self.radius : return False
        if x > get_canvas_width() + self.radius : return False
        if y > get_canvas_height() + self.radius : return False

        return True
        
