from pico2d import *
import math

from pico2d import clear_canvas_now

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

c_x =400
c_y =90

moves=0

while True:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(c_x,c_y)

    if moves == 0:
        move_ractangle(c_x,c_y)

    elif moves == 1:
        move_triangle(c_x,c_y)

    elif moves == 2:
        move_circle(c_x,c_y)

    delay(0.01)

