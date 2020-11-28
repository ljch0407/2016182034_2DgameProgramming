from pico2d import*
import gfw
import gobj
from bullet import*

MAX_LIFE = 5 

class Player:
    def __init__(self):
        global pos, radius
        self.pos = 100,get_canvas_height()//4+80
        pos = self.pos
        self.image = gfw.image.load('res/rockman.png')
        self.delta =0,25
        self.state='running'
        self.fidx = 0
        self.time=0
        self.FPS = 8
        self.radius = 50
        radius = self.radius
        self.life = MAX_LIFE

        self.life_1 = gfw.image.load('res/Life1.png')
        self.life_2 = gfw.image.load('res/Life2.png')

        self.reset()

    def state(self):
        return self.__state
    def state(self, state):
        self.__state=state
    def fire(self):
        x,y = self.pos
        Bullet = bullet(x+30,y,600)
        gfw.world.add(gfw.layer.bullet,Bullet)

    def reset(self):
        self.pos = 100,get_canvas_height()//4+80
        self.state='running'
        self.life = MAX_LIFE
        self.delta =0,25

    def decrease_life(self):
        self.life-=1
        return self.life<=0

    def increas_life(self):
        if self.life >=MAX_LIFE:
            return True

        self.life += 1
        return False
      
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
            self.fire()
            self.image.clip_draw(145,10,30,35,*self.pos,100,100)
            pass
        
        elif self.state=='gunfire':
            self.fire()
            x,y = self.pos
            if self.fidx==0:
                self.image.clip_draw(48,10,31,33,x,y+20,100,100)
            elif self.fidx == 1:
                self.image.clip_draw(83,10,30,33,x,y+20,100,100)
            elif self.fidx ==2:
                self.image.clip_draw(110,10,33,33,x,y+20,100,100)
            elif self.fidx==3:
               self.image.clip_draw(83,10,30,32,x,y+20,100,100)

        x,y = get_canvas_width()-30, get_canvas_height()-30
        for i in range(MAX_LIFE):
            Life = self.life_1 if i<self.life else self.life_2
            Life.draw(x,y)
            x-=Life.w

                
                

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
                 self.pos = 100,get_canvas_height()//4+80
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
                 self.pos = 100,get_canvas_height()//4+80
                 self.delta =0,25
                 self.state='running'
        
        pass

    def handle_event(self,e):
        global fire_wav,jump_wav
        fire_wav = load_wav(gobj.res('PL00_U_00023.wav'))
        jump_wav = load_wav(gobj.res('STB_1_1_00007.wav'))
       
        fire_wav.set_volume(30)
        jump_wav.set_volume(30)

        if e.type == SDL_KEYDOWN:
            if self.state=='jump':
                if e.key ==SDLK_RETURN:
                    fire_wav.play()
                    self.state='jumpfire'
            elif self.state=='running':
                if e.key == SDLK_SPACE:
                    jump_wav.play()
                    self.state = 'jump'
                elif e.key == SDLK_RETURN:
                    fire_wav.play()
                    self.state = 'gunfire'

        elif e.type ==SDL_KEYUP:
            if self.state=='jumpfire':
                if e.key == SDLK_RETURN:
                    self.state='jump'
            elif self.state=='gunfire':
                if e.key == SDLK_RETURN:
                    self.fidx=0
                    self.state='running'

    def get_bb(self):
        hw = self.image.w//2
        hh = self.image.h//2
        return self.x-hx, self.y-hh,self.x+hw,self.y+hh
                
                    
                
        
