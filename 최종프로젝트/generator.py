from pico2d import *
import gfw
from enemy import *
import random

enemy_count =10
item_count = 3
def update(score):
    Max_enemy_count = enemy_count + score/10
    while gfw.world.count_at(gfw.layer.enemy)<Max_enemy_count:
        generate_enemy(score)
    while gfw.world.count_at(gfw.layer.item) < item_count:
        generate_item(score)


def generate_enemy(score):
    x,y,dx,dy = get_coords(score)
    e = Enemy((x,y), (dx,dy))
    gfw.world.add(gfw.layer.enemy,e)
    
def generate_item(score):
    x,y,dx,dy = get_coords(score)
    e = E_can((x,y), (dx,dy))
    gfw.world.add(gfw.layer.item,e)

def get_coords(score):
    dx = random.random()
    
    dy =0

    mag = 1+score/60
    dx *=mag
    dy *=mag

    x= get_canvas_width()
    y = random.uniform(get_canvas_height()//4+80,get_canvas_height())

    return x,y,dx,dy
