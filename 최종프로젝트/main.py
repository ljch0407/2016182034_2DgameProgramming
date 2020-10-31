from pico2d import *


def handle_events():
    global running
    global rockman
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running = False
        elif event.type==SDL_KEYDOWN and event.key==SDLK_LCTRL:
            rockman.state='gunfire'
        elif event.type==SDL_KEYUP and event.key==SDLK_LCTRL:
            rockman.state='run'
        

class Rockman:
    def __init__(self):
        self.frame = 0 
        self.state ='run'
        self.image = load_image('res/megaman_move_'+self.state+'.png')
    def draw(self):
        self.image = load_image('res/megaman_move_'+self.state+'.png')
        if self.state=='run':
            self.image.clip_draw(self.frame*100,0,100,100,180,200,90,90)
        elif self.state=='gunfire':
            self.image.clip_draw(self.frame*100,0,100,100,180,200,100,100)
    def update(self):
        self.frame = (self.frame+1) % 3


open_canvas()

rockman = Rockman()
back_ground = load_image('res/back_ground.png')
running = True
hide_cursor()

while(running):
    handle_events()
    
    rockman.update()
    
    clear_canvas()
    back_ground.draw(0,0,1600,1200)
    
    rockman.draw()

    update_canvas()
    delay(0.1)

close_canvas()
