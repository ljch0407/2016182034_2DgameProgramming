from pico2d import *
import gfw
import gobj
import player
from bullet import bullet
import highscore
from background import HorzScrollBackground
import generator
from collision import *


STATE_IN_GAME,STATE_GAME_OVER = range(2)

def start_game():
    global state
    global player
    if state != STATE_GAME_OVER:
        return

    player.reset()
    gfw.world.clear_at(gfw.layer.enemy)
    gfw.world.remove(highscore)

    state = STATE_IN_GAME

    global score
    score = 0

    global bg_music,run_wav
    bg_music.repeat_play()

def end_game():
    global state
    print('game over')
    state = STATE_GAME_OVER
    bg_music.stop()
    run_wav.play()

    highscore.add(score)
    gfw.world.add(gfw.layer.ui, highscore)

def enter():
    gfw.world.init(['bg','enemy','bullet','item','player','ui'])
    player.init()
    gfw.world.add(gfw.layer.player,player)
    bg = HorzScrollBackground("bg.png")
    bg.speed=50
    gfw.world.add(gfw.layer.bg,bg)

    global game_over_image
    game_over_image = gfw.image.load('res/game_over.png')

    global font
    font = gfw.font.load('res/ConsolaMalgun.ttf', 40)

    global bg_music,run_wav
    bg_music = load_music(gobj.res('bg.mp3'))
    bg_music.set_volume(60)
    bg_music.repeat_play()

    run_wav = load_wav(gobj.res('STB_1_1_00003.wav'))
    run_wav.set_volume(5)

    highscore.load()

    global state
    state = STATE_GAME_OVER
    start_game()
    
    pass
def check_enemy(e):
    global score
    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            dead = e.decrease_hp(b.power)
            if dead:
                e.remove()
                score+=1

            b.remove()
            return

def update():
    global state, run_wav
    if state != STATE_IN_GAME:
        return
    global score
    score +=gfw.delta_time
    
    gfw.world.update()
    generator.update(score)
    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

    hits, ends, item = check_collision()

    if item is not None:
        full = player.increase_life()
        if full:
            score+=3
    
    if ends:
        end_game()
    run_wav.play()
    pass

def draw():
    gfw.world.draw()

    score_pos = 30, get_canvas_height() - 30
    font.draw(*score_pos, 'Score: %.1f' % score, (255,255,255))
    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
        game_over_image.draw(*center)

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return
    elif e.type == SDL_MOUSEBUTTONDOWN:
        start_game()

    player.handle_event(e)


def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
