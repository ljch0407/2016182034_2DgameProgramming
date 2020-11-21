from pico2d import *
import gfw
from player import Player

def enter():
    gfw.world.init(['bg','enemy','player'])
    global player
    player = Player()
    gfw.world.add(gfw.layer.player,player)
    
    pass

def update():
    gfw.world.update()
    pass

def draw():
    gfw.world.draw()

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return

    player.handle_event(e)


def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
