from pico2d import *

open_canvas()

# 창 크기 정보 (pico2d 기본값: 800x600)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 꼭짓점 좌표 (창의 네 모서리, 잔디 높이 고려)
MARGIN = 45  # 캐릭터와 잔디가 화면 밖으로 나가지 않게 여백
points = [
    (MARGIN, MARGIN),  # 좌하단
    (WINDOW_WIDTH - MARGIN, MARGIN),  # 우하단
    (WINDOW_WIDTH - MARGIN, WINDOW_HEIGHT - MARGIN),  # 우상단
    (MARGIN, WINDOW_HEIGHT - MARGIN)  # 좌상단
]

current = 0

while True:
    next = (current + 1) % len(points)
    x1, y1 = points[current]
    x2, y2 = points[next]
    for t in range(0, 101, 2):
        clear_canvas()
        grass.draw(WINDOW_WIDTH // 2, 30)
        x = x1 + (x2 - x1) * t / 100
        y = y1 + (y2 - y1) * t / 100
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    current = next

close_canvas()
