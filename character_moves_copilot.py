from pico2d import *
import math

open_canvas()

# 창 크기 정보 (pico2d 기본값: 800x600)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

# 경로 정의
MARGIN = 45
BOTTOM_Y = 90

# 사각형 꼭짓점
square_points = [
    (MARGIN, BOTTOM_Y),
    (WINDOW_WIDTH - MARGIN, BOTTOM_Y),
    (WINDOW_WIDTH - MARGIN, WINDOW_HEIGHT - MARGIN),
    (MARGIN, WINDOW_HEIGHT - MARGIN)
]
# 삼각형 꼭짓점
triangle_points = [
    (400, BOTTOM_Y),
    (700, 500),
    (100, 500)
]
# 원 경로 정보
circle_center = (400, 300)
circle_radius = 210
circle_start_angle = -math.pi/2  # 270도, 아래쪽

# 모드: 0=사각, 1=삼각, 2=원
mode = 0
mode_names = ['사각형', '삼각형', '원']

while True:
    if mode == 0:
        points = square_points
    elif mode == 1:
        points = triangle_points
    else:
        points = None  # 원은 points 사용 안함

    if mode in [0, 1]:
        # 다각형 경로
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i+1)%len(points)]
            for t in range(0, 101, 2):
                clear_canvas()
                grass.draw(WINDOW_WIDTH // 2, 30)
                x = x1 + (x2 - x1) * t / 100
                y = y1 + (y2 - y1) * t / 100
                character.draw(x, y)
                update_canvas()
                delay(0.01)
            # 한 바퀴 끝나면 시작점에 도달
            if (i+1)%len(points) == 0:
                break
    else:
        # 원 경로
        for deg in range(0, 361, 2):
            clear_canvas()
            grass.draw(WINDOW_WIDTH // 2, 30)
            rad = circle_start_angle + math.radians(deg)
            x = circle_center[0] + circle_radius * math.cos(rad)
            y = circle_center[1] + circle_radius * math.sin(rad)
            if y < BOTTOM_Y:
                y = BOTTOM_Y  # 잔디 아래로 내려가지 않게
            character.draw(x, y)
            update_canvas()
            delay(0.01)
        # 한 바퀴 끝나면 시작점에 도달
    # 모드 전환
    mode = (mode + 1) % 3

close_canvas()
