from pico2d import *
import gfw
import gobj
from background import HorzScrollBackground
import main_state


def start():
    gfw.push(main_state)

def build_world():
    gfw.world.init(['bg'])
    bg = HorzScrollBackground("menu.png")
    bg.speed=0
    gfw.world.add(gfw.layer.bg,bg)

    global bg_music
    bg_music = load_music(gobj.res('menu_bg.mp3'))
    bg_music.set_volume(60)
    bg_music.repeat_play()

def enter():
    build_world()
    
   
def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    
def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
        elif e.key==SDLK_RETURN:
            global bg_music
            bg_music.stop()
            start()

    
def exit():
    print("menu_state exits")
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
