from pico2d import*
import gfw
import gobj
from bullet import*

MAX_LIFE = 5 


def init():
    global pos, radius,image,state,delta,fidx,time,FPS,life,life_1,life_2
    pos = 100,get_canvas_height()//4+80
    image = gfw.image.load('res/rockman.png')
    delta =0,25
    state='running'
    fidx = 0
    time=0
    FPS = 8
    radius = 50
    
    life = MAX_LIFE

    life_1 = gfw.image.load('res/Life1.png')
    life_2 = gfw.image.load('res/Life2.png')

    reset()

def state():
    global state
    return state
def state(states):
    global state
    state = states
def fire():
    global pos
    x,y = pos
    Bullet = bullet(x+30,y,600)
    gfw.world.add(gfw.layer.bullet,Bullet)

def reset():
    global pos,state,life,delta
    pos = 100,get_canvas_height()//4+80
    state='running'
    life = MAX_LIFE
    delta =0,25

def decrease_life():
    global life
    life-=1
    return life<=0

def increas_life():
    global life
    if life >=MAX_LIFE:
        return True
    life += 1
    return False
      
def draw():
    global pos, state,fidx, life_1, life_2
    if state =='running':
        if fidx==0:
            image.clip_draw(188,40,25,35,*pos,100,100)
        elif fidx == 1:
            image.clip_draw(214,40,25,35,*pos,100,100)
        elif fidx ==2:
            image.clip_draw(239,40,25,35,*pos,100,100)
        elif fidx==3:
           image.clip_draw(214,40,25,35,*pos,100,100)

    elif state == 'jump':
        image.clip_draw(265,40,30,40,*pos,100,100)
        pass

    elif state=='jumpfire':
        fire()
        image.clip_draw(145,10,30,35,*pos,100,100)
        pass
    elif state=='gunfire':
        fire()
        x,y = pos
        if fidx==0:
            image.clip_draw(48,10,31,33,x,y+20,100,100)
        elif fidx == 1:
            image.clip_draw(83,10,30,33,x,y+20,100,100)
        elif fidx ==2:
            image.clip_draw(110,10,33,33,x,y+20,100,100)
        elif fidx==3:
           image.clip_draw(83,10,30,32,x,y+20,100,100)

    x,y = get_canvas_width()-30, get_canvas_height()-30
    for i in range(MAX_LIFE):
        Life = life_1 if i<life else life_2
        Life.draw(x,y)
        x-=Life.w

                
                

def update():
    global time, FPS, fidx, state, pos, delta
    time += gfw.delta_time
    frame = time * FPS
    fidx = int(frame) % 4

    if state=='jump':
        x,y= pos
        dx,dy= delta
        
        y+=dy
        dy-=1
            
        pos=x,y
        delta = dx,dy
        if y<get_canvas_height()//4:
             pos = 100,get_canvas_height()//4+80
             delta =0,25
             state='running'
                 
    elif state=='jumpfire':
        x,y=pos
        dx,dy=delta

        y+=dy
        dy-=1
        
        pos=x,y
        delta = dx,dy
        if y<get_canvas_height()//4:
             pos = 100,get_canvas_height()//4+80
             delta =0,25
             state='running'
        
        pass

def handle_event(e):
    global fire_wav,jump_wav, state, fidx
    fire_wav = load_wav(gobj.res('PL00_U_00023.wav'))
    jump_wav = load_wav(gobj.res('STB_1_1_00007.wav'))
       
    fire_wav.set_volume(30)
    jump_wav.set_volume(30)

    if e.type == SDL_KEYDOWN:
        if state=='jump':
            if e.key ==SDLK_RETURN:
                fire_wav.play()
                state='jumpfire'
        elif state=='running':
            if e.key == SDLK_SPACE:
                jump_wav.play()
                state = 'jump'
            elif e.key == SDLK_RETURN:
                fire_wav.play()
                state = 'gunfire'

    elif e.type ==SDL_KEYUP:
        if state=='jumpfire':
            if e.key == SDLK_RETURN:
                state='jump'
        elif state=='gunfire':
            if e.key == SDLK_RETURN:
                fidx=0
                state='running'

def get_bb():
    global pos
    x,y=pos
    hw = image.w//2
    hh = image.h//2
    return x-hx, y-hh,x+hw,y+hh

        
                
        
