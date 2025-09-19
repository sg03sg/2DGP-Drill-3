from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 꼭짓점 좌표 (시계방향)
points = [
    (400, 90),   # 시작점 (아래쪽 중앙)
    (700, 90),   # 오른쪽 아래
    (700, 300),  # 오른쪽 위
    (400, 300),  # 왼쪽 위
    (400, 90)    # 다시 시작점
]

current = 0

while True:
    next = (current + 1) % len(points)
    x1, y1 = points[current]
    x2, y2 = points[next]
    for t in range(0, 101, 2):
        clear_canvas()
        grass.draw(400, 30)
        x = x1 + (x2 - x1) * t / 100
        y = y1 + (y2 - y1) * t / 100
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    current = next

close_canvas()

