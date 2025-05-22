import pygame
import random
import numpy as np
from pygame.locals import *
import math

# 초기화
pygame.init()

# 화면 설정
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Snake Game')

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 피보나치 수열 계산 함수
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# 스네이크 클래스
class Snake:
    def __init__(self):
        self.positions = [(WIDTH//2, HEIGHT//2)]
        self.direction = [1, 0]
        self.length = 1
        self.score = 0
        self.speed = 5
        self.growth_count = 0
        self.tail_eaten = 0

    def move(self):
        current = self.positions[0]
        x = current[0] + self.direction[0] * self.speed
        y = current[1] + self.direction[1] * self.speed
        
        # 화면 경계 처리
        if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
            return False
            
        # 자기 자신과의 충돌 검사
        if (x, y) in self.positions[1:]:
            return False
            
        self.positions.insert(0, (x, y))
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def change_direction(self, new_direction):
        # 반대 방향으로는 이동할 수 없음
        if (self.direction[0] * -1, self.direction[1] * -1) != new_direction:
            self.direction = list(new_direction)

    def grow(self, is_tail=False):
        self.length += 1
        if is_tail:
            self.tail_eaten += 1
            self.score += 20
        else:
            self.score += 10

    def check_food_collision(self, food_position):
        # 머리와 먹이 충돌 검사
        if (abs(self.positions[0][0] - food_position[0]) < 20 and 
            abs(self.positions[0][1] - food_position[1]) < 20):
            self.grow(False)
            return True
            
        # 꼬리와 먹이 충돌 검사
        for i in range(1, len(self.positions)):
            if (abs(self.positions[i][0] - food_position[0]) < 20 and 
                abs(self.positions[i][1] - food_position[1]) < 20):
                self.grow(True)
                return True
                
        return False

    def draw(self, surface):
        for i, pos in enumerate(self.positions):
            # 3D 효과를 위한 크기 계산
            size = 20 - (i * 0.5)
            if size < 5:
                size = 5
                
            # 3D 효과를 위한 투명도 계산
            alpha = 255 - (i * 5)
            if alpha < 50:
                alpha = 50
                
            s = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.rect(s, (*GREEN, alpha), (0, 0, size, size))
            surface.blit(s, (pos[0] - size//2, pos[1] - size//2))

# 먹이 클래스
class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.size = 15

    def generate_position(self):
        x = random.randint(20, WIDTH-20)
        y = random.randint(20, HEIGHT-20)
        return (x, y)

    def draw(self, surface):
        pygame.draw.circle(surface, RED, self.position, self.size)

# 게임 객체 생성
snake = Snake()
food = Food()
clock = pygame.time.Clock()

# 게임 루프
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and not game_over:
            if event.key == K_UP:
                snake.change_direction((0, -1))
            elif event.key == K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == K_RIGHT:
                snake.change_direction((1, 0))
        elif event.type == KEYDOWN and game_over:
            if event.key == K_SPACE:
                # 게임 재시작
                snake = Snake()
                food = Food()
                game_over = False

    if not game_over:
        # 스네이크 이동
        if not snake.move():
            game_over = True

        # 충돌 검사
        if snake.check_food_collision(food.position):
            food.position = food.generate_position()

    # 화면 그리기
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    
    # 점수 표시
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {snake.score} (꼬리로 먹은 먹이: {snake.tail_eaten})', True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render('Game Over! Press SPACE to restart', True, WHITE)
        text_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit() 