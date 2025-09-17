from pico2d import *
import math

from pico2d import clear_canvas_now

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

c_x =400
c_y =90

moves=0
speed =10

def move_ractangle(x,y):
    if y==90 and x < 780:
         return x + speed, y
    elif x==780 and y < 550:
        return x, y+ speed
    elif y==550 and x >20:
        return x- speed, y
    elif x==20 and y >90:
        return x, y- speed


while True:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(c_x,c_y)

    if moves == 0:
        c_x,c_y = move_ractangle(c_x,c_y)

    # elif moves == 1:
    #     move_triangle(c_x,c_y)
    #
    # elif moves == 2:
    #     move_circle(c_x,c_y)

    delay(0.01)

