from pico2d import *
import gfw
import gobj
from player import Player
from bullet import bullet
from background import HorzScrollBackground

def enter():
    gfw.world.init(['bg','enemy','bullet','player'])
    global player
    player = Player()
    gfw.world.add(gfw.layer.player,player)
    bg = HorzScrollBackground("bg.png")
    bg.speed=50
    gfw.world.add(gfw.layer.bg,bg)

    global bg_music,run_wav
    bg_music = load_music(gobj.res('bg.mp3'))
    bg_music.set_volume(60)
    bg_music.repeat_play()

    run_wav = load_wav(gobj.res('STB_1_1_00003.wav'))
    run_wav.repeat_play()
    run_wav.set_volume(10)
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
