from pico2d import*
import gfw

class Player:
    def __init__(self):
        self.pos = 75,get_canvas_height()//4
        self.image = gfw.image.load('res/rockman.png')
        self.delta =0,25
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

        elif self.state == 'jump':
            self.image.clip_draw(265,40,30,40,*self.pos,100,100)
            pass

        elif self.state=='jumpfire':
            self.image.clip_draw(145,10,30,35,*self.pos,100,100)
            pass
        
        elif self.state=='gunfire':
            x,y = self.pos
            if self.fidx==0:
                self.image.clip_draw(48,10,31,33,x,y+20,100,100)
            elif self.fidx == 1:
                self.image.clip_draw(83,10,30,33,x,y+20,100,100)
            elif self.fidx ==2:
                self.image.clip_draw(110,10,33,33,x,y+20,100,100)
            elif self.fidx==3:
               self.image.clip_draw(83,10,30,32,x,y+20,100,100)

                
                

    def update(self):
        self.time += gfw.delta_time
        frame = self.time * self.FPS
        self.fidx = int(frame) % 4

        if self.state=='jump':
            x,y=self.pos
            dx,dy=self.delta

            y+=dy
            dy-=1
            
            self.pos=x,y
            self.delta = dx,dy
            if y<get_canvas_height()//4:
                 self.pos = 75,get_canvas_height()//4
                 self.delta =0,25
                 self.state='running'
                 
        elif self.state=='jumpfire':
            x,y=self.pos
            dx,dy=self.delta

            y+=dy
            dy-=1
            
            self.pos=x,y
            self.delta = dx,dy
            if y<get_canvas_height()//4:
                 self.pos = 75,get_canvas_height()//4
                 self.delta =0,25
                 self.state='running'
        
        pass

    def handle_event(self,e):
        if e.type == SDL_KEYDOWN:
            if self.state=='jump':
                if e.key ==SDLK_RETURN:
                    self.state='jumpfire'
            elif self.state=='running':
                if e.key == SDLK_SPACE:
                    self.state = 'jump'
                elif e.key == SDLK_RETURN:
                    self.state = 'gunfire'

        elif e.type ==SDL_KEYUP:
            if self.state=='jumpfire':
                if e.key == SDLK_RETURN:
                    self.state='jump'
            elif self.state=='gunfire':
                if e.key == SDLK_RETURN:
                    self.fidx=0
                    self.state='running'
                
                    
                
        
