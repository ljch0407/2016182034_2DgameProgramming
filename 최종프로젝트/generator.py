from pico2d import *
import gfw
from enemy import *
import random

enemy_count =10

def update(score):
    Max_enemy_count = enemy_count + score/10
    if gfw.world.count_at(gfw.layer.enemy)<Max_enemy_count:
        generate_enemy(score)


def generate_enemy(score):
    x,y,dx,dy = get_coords(score)
    e = Enemy((x,y), (dx,dy))
    gfw.world.add(gfw.layer.enemy,e)

def get_coords(score):
    dx = random.random()
    
    dy =0

    mag = 1+score/60
    dx *=mag
    dy *=mag

    x= get_canvas_width()
    y = random.uniform(get_canvas_height()//4+80,get_canvas_height())

    return x,y,dx,dy
