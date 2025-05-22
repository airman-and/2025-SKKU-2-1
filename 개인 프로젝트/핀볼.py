import pygame
import sys
import math
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("핀볼 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 공 클래스
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.dx = 0
        self.dy = 0
        self.gravity = 0.5
        self.friction = 0.99

    def update(self):
        self.dy += self.gravity
        self.x += self.dx
        self.y += self.dy
        self.dx *= self.friction
        self.dy *= self.friction

        # 벽 충돌 처리
        if self.x - self.radius < 0:
            self.x = self.radius
            self.dx *= -0.8
        elif self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.dx *= -0.8

        if self.y - self.radius < 0:
            self.y = self.radius
            self.dy *= -0.8
        elif self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.dy *= -0.8

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

# 플리퍼 클래스
class Flipper:
    def __init__(self, x, y, angle, is_left):
        self.x = x
        self.y = y
        self.angle = angle
        self.length = 100
        self.width = 20
        self.is_left = is_left
        self.rotation_speed = 0
        self.max_angle = 30 if is_left else -30
        self.min_angle = -30 if is_left else 30

    def update(self):
        keys = pygame.key.get_pressed()
        if self.is_left and keys[pygame.K_LEFT]:
            self.rotation_speed = -5
        elif not self.is_left and keys[pygame.K_RIGHT]:
            self.rotation_speed = 5
        else:
            self.rotation_speed = 0

        self.angle += self.rotation_speed
        self.angle = max(self.min_angle, min(self.max_angle, self.angle))

    def draw(self, screen):
        end_x = self.x + math.cos(math.radians(self.angle)) * self.length
        end_y = self.y + math.sin(math.radians(self.angle)) * self.length
        pygame.draw.line(screen, BLUE, (self.x, self.y), (end_x, end_y), self.width)

# 게임 객체 생성
ball = Ball()
left_flipper = Flipper(WIDTH//2 - 50, HEIGHT - 50, -30, True)
right_flipper = Flipper(WIDTH//2 + 50, HEIGHT - 50, 30, False)

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 업데이트
    ball.update()
    left_flipper.update()
    right_flipper.update()

    # 충돌 감지 (간단한 구현)
    if ball.y + ball.radius > HEIGHT - 50:
        ball.dy *= -0.8

    # 화면 그리기
    screen.fill(BLACK)
    ball.draw(screen)
    left_flipper.draw(screen)
    right_flipper.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
