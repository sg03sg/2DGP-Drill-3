from pico2d import *
import math

open_canvas()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

grass = load_image('grass.png')
character = load_image('character.png')

MARGIN = 45
BOTTOM_Y = 90

# 사각형 꼭짓점 (시작점 400,90)
square_points = [
    (400, BOTTOM_Y),
    (WINDOW_WIDTH - MARGIN, BOTTOM_Y),
    (WINDOW_WIDTH - MARGIN, WINDOW_HEIGHT - MARGIN),
    (MARGIN, WINDOW_HEIGHT - MARGIN),
    (MARGIN, BOTTOM_Y),
    (400, BOTTOM_Y)
]
# 삼각형 꼭짓점 (시작점 400,90)
triangle_points = [
    (400, BOTTOM_Y),
    (700, 500),
    (100, 500),
    (400, BOTTOM_Y)
]
# 원 경로 정보 (시작점 400,90, 시계방향)
circle_center = (400, 300)
circle_radius = 210
circle_start_angle = -math.pi/2  # 270도, 아래쪽

mode = 0  # 0=사각, 1=삼각, 2=원

while True:
    if mode == 0:
        points = square_points
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            for t in range(0, 101, 2):
                clear_canvas()
                grass.draw(WINDOW_WIDTH // 2, 30)
                x = x1 + (x2 - x1) * t / 100
                y = y1 + (y2 - y1) * t / 100
                character.draw(x, y)
                update_canvas()
                delay(0.01)
    elif mode == 1:
        points = triangle_points
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            for t in range(0, 101, 2):
                clear_canvas()
                grass.draw(WINDOW_WIDTH // 2, 30)
                x = x1 + (x2 - x1) * t / 100
                y = y1 + (y2 - y1) * t / 100
                character.draw(x, y)
                update_canvas()
                delay(0.01)
    else:
        # 원 경로: 270도(아래)에서 시작, 360도 시계방향(각도 감소)
        for deg in range(0, 361, 2):
            clear_canvas()
            grass.draw(WINDOW_WIDTH // 2, 30)
            rad = -math.pi/2 - math.radians(deg)  # 시계방향
            x = circle_center[0] + circle_radius * math.cos(rad)
            y = circle_center[1] + circle_radius * math.sin(rad)
            if y < BOTTOM_Y:
                y = BOTTOM_Y
            character.draw(x, y)
            update_canvas()
            delay(0.01)
    mode = (mode + 1) % 3

close_canvas()
