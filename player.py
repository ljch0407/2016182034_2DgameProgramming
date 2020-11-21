from pico2d import*
import gfw

class Player:
    def __init__(self):
        self.pos = 75,get_canvas_height()//4
        self.image = gfw.image.load('res/rockman.png')
        self.delta =0,0
        self.state='running'
        self.fidx = 0
        self.time=0
        self.FPS = 8

    def state(self):
        return self.__state
    def state(self, state):
        self.__state=state

    def draw(self):
        if self.state =='running':
            if self.fidx==0:
                self.image.clip_draw(188,40,25,35,*self.pos,100,100)
            elif self.fidx == 1:
                self.image.clip_draw(214,40,25,35,*self.pos,100,100)
            elif self.fidx ==2:
                self.image.clip_draw(239,40,25,35,*self.pos,100,100)
            elif self.fidx==3:
               self.image.clip_draw(214,40,25,35,*self.pos,100,100)
                
                

    def update(self):
        self.time += gfw.delta_time
        frame = self.time * self.FPS
        self.fidx = int(frame) % 4 
        pass
