import tkinter as tk
import random
import math

# 게임 창 크기 및 물리 상수 설정
WIDTH = 400
HEIGHT = 600
GRAVITY = 0.1
BALL_RADIUS = 10

# 장애물(버퍼) 설정: 중심으로 유도할 위치 주변에 배치
OBSTACLES = [
    {'x': WIDTH//2,     'y': HEIGHT//2 - 100, 'r': 20},
    {'x': WIDTH//2 - 100, 'y': HEIGHT//2 +  50, 'r': 20},
    {'x': WIDTH//2 + 100, 'y': HEIGHT//2 +  50, 'r': 20},
]

class Ball:
    def __init__(self, canvas, obstacles):
        self.canvas = canvas
        self.obstacles = obstacles
        start_x = WIDTH // 2
        start_y = HEIGHT // 4
        self.id = canvas.create_oval(start_x - BALL_RADIUS, start_y - BALL_RADIUS,
                                     start_x + BALL_RADIUS, start_y + BALL_RADIUS, fill='white')
        self.vx = random.choice([-3, -2, 2, 3])
        self.vy = 0

    def update(self, flippers):
        # 중력 가속도 적용
        self.vy += GRAVITY
        # 현재 위치
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2

        # 공 이동
        self.canvas.move(self.id, self.vx, self.vy)

        # 벽과 충돌 처리
        if cx - BALL_RADIUS <= 0:
            self.vx = abs(self.vx)
        if cx + BALL_RADIUS >= WIDTH:
            self.vx = -abs(self.vx)
        if cy - BALL_RADIUS <= 0:
            self.vy = abs(self.vy)

        # 플리퍼와 충돌 처리
        for flipper in flippers:
            if flipper.hit(cx, cy, BALL_RADIUS):
                angle = math.radians(flipper.angle + (-90 if flipper.direction == 1 else 90))
                speed = math.hypot(self.vx, self.vy)
                self.vx = speed * math.cos(angle)
                self.vy = -abs(speed * math.sin(angle))

        # 장애물과 충돌 처리 및 중심으로 유도
        for obs in self.obstacles:
            dx = cx - obs['x']
            dy = cy - obs['y']
            dist = math.hypot(dx, dy)
            if dist <= obs['r'] + BALL_RADIUS:
                # 반사
                nx, ny = dx/dist, dy/dist
                dot = self.vx * nx + self.vy * ny
                self.vx -= 2 * dot * nx
                self.vy -= 2 * dot * ny
                # 중앙 방향 힘 추가
                cdx = (WIDTH/2) - cx
                cdy = (HEIGHT/2) - cy
                clen = math.hypot(cdx, cdy)
                if clen > 0:
                    self.vx += (cdx / clen) * 0.5
                    self.vy += (cdy / clen) * 0.5

        # 바닥에 떨어지면 리셋
        if cy + BALL_RADIUS >= HEIGHT:
            self.canvas.coords(self.id,
                               WIDTH // 2 - BALL_RADIUS, HEIGHT // 4 - BALL_RADIUS,
                               WIDTH // 2 + BALL_RADIUS, HEIGHT // 4 + BALL_RADIUS)
            self.vx = random.choice([-3, -2, 2, 3])
            self.vy = 0

class Flipper:
    def __init__(self, canvas, pivot_x, pivot_y, length, closed_angle, open_angle, direction):
        self.canvas = canvas
        self.pivot = (pivot_x, pivot_y)
        self.length = length
        self.closed_angle = closed_angle
        self.open_angle = open_angle
        self.angle = closed_angle
        self.direction = direction  # 왼쪽=-1, 오른쪽=1
        self.id = canvas.create_line(*self.get_coords(), width=6, fill='red')

    def get_coords(self):
        x0, y0 = self.pivot
        rad = math.radians(self.angle)
        x1 = x0 + self.length * math.cos(rad)
        y1 = y0 - self.length * math.sin(rad)
        return (x0, y0, x1, y1)

    def draw(self):
        self.canvas.coords(self.id, *self.get_coords())

    def flip(self, event=None):
        self.angle = self.open_angle
        self.draw()

    def release(self, event=None):
        self.angle = self.closed_angle
        self.draw()

    def hit(self, cx, cy, radius):
        x0, y0, x1, y1 = self.get_coords()
        dx, dy = x1 - x0, y1 - y0
        if dx == 0 and dy == 0:
            return False
        t = ((cx - x0) * dx + (cy - y0) * dy) / (dx*dx + dy*dy)
        t = max(0, min(1, t))
        px = x0 + t * dx
        py = y0 + t * dy
        return math.hypot(cx - px, cy - py) <= radius + 3

def main():
    root = tk.Tk()
    root.title("Pinball Game")
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
    canvas.pack()

    # 장애물(버퍼) 그리기
    for obs in OBSTACLES:
        x, y, r = obs['x'], obs['y'], obs['r']
        obs['id'] = canvas.create_oval(x-r, y-r, x+r, y+r, fill='blue')

    # 왼쪽/오른쪽 플리퍼 생성
    left_flipper  = Flipper(canvas, WIDTH//2 - 50, HEIGHT - 100, 80,  30,  60, -1)
    right_flipper = Flipper(canvas, WIDTH//2 + 50, HEIGHT - 100, 80, 150, 120,  1)
    flippers = [left_flipper, right_flipper]

    # 키 바인딩
    root.bind('<Left>',  left_flipper.flip)
    root.bind('<KeyRelease-Left>',  left_flipper.release)
    root.bind('<Right>', right_flipper.flip)
    root.bind('<KeyRelease-Right>', right_flipper.release)

    # 공 생성
    ball = Ball(canvas, OBSTACLES)

    def game_loop():
        ball.update(flippers)
        for f in flippers:
            f.draw()
        root.after(16, game_loop)

    game_loop()
    root.mainloop()

if __name__ == '__main__':
    main()
