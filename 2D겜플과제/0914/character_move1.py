from pico2d import *


open_canvas()

image = load_image('../res/character.png')


image.draw_now(300,200)
image.draw_now(500,400)

delay(2)

clear_canvas_now()

for x in range(0,9):
    for y in range(0,7):
        image.draw_now(x*100,y*100)
        

delay(2)


clear_canvas_now()

grass = load_image('../res/grass.png')
character = load_image('../res/character.png')

grass.draw_now(400,30)
character.draw_now(400,80)

delay(2)

clear_canvas_now()

x=0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,80)
    x+=2
    delay(0.1)


delay(2)

clear_canvas_now()
x=0
while(x<800):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,90)
    x+=2
    update_canvas()
    delay(0.01)
    get_events()

delay(2)

clear_canvas_now()

character = load_image('../res/run_animation.png')
x=0
frame=0

while(x<800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    frame= (frame+1)%8
    x+=5
    delay(0.05)
    get_events()

delay(2)

x=0
frame_index = 0
action = 0
character = load_image('../res/animation_sheet.png')
while x<800:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(100 * frame_index,100*action,100,100,x,85)
    update_canvas()
    get_events()
	
    x+=2
    if x %100==0:
        action=(action+1) % 4
        
    frame_index=(frame_index+1) % 8
    delay(0.05)
    
delay(2)
close_canvas()
