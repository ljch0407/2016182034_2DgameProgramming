from pico2d import *
from helper import *

open_canvas()

def handle_events():
    global running
    global x
    global y
    global END
    global Speed
    global Pos_list
    global INDEX
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False
        elif event.type==SDL_MOUSEBUTTONDOWN:
            if event.button==SDL_BUTTON_LEFT:
                x = event.x
                y = get_canvas_height()-event.y
                Pos_list.append((x,y))
                
                if END==True:
                    INDEX=INDEX+1
                    END=False
            elif event.button==SDL_BUTTON_RIGHT:    
                if END==False:
                    Speed=Speed+1
                    

                
class Boy:
    def __init__(self):
        self.image = load_image('../res/run_animation.png')
        self.done=END
        self.frame = 0
        self.x=10
        self.y=90
        self.pos = (self.x,self.y)
        self.speed = Speed
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.pos[0],self.pos[1])

    def update(self):
        global Speed
        global END
        global INDEX
        global Pos_list
        self.frame = (self.frame+1)% 8
        if self.done == END:
            self.pos,self.done = move_toward(self.pos,delta(self.pos,Pos_list[INDEX],self.speed),Pos_list[INDEX])
            self.speed=Speed
            Pos_list
            if self.done==True:
                INDEX = INDEX+1
                if(len(Pos_list)==INDEX):
                    INDEX=INDEX-1
                    END=True
                Speed=1
                self.done=False
                
        #self.x,self.y=x,y
        pass

class grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
    def draw(self):
        self.image.draw(400,30)

Pos_list=[(10,90)]
INDEX=0
Speed=1
END = True    
x=10
y=90
targetpos=(x,y)
boy=Boy()
grass=grass()


running = True
while running:
    handle_events()

    clear_canvas()
    boy.draw()
    grass.draw()
    update_canvas()
    boy.update()

    delay(0.01)

close_canvas()
