
import pygame
import sys
import math

pygame.init()

# 게임 창 설정
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Character Game")

# 배경색
background_color = (240, 240, 255)

# 캐릭터 이미지 불러오기
character_original = pygame.image.load("chibee_character.png")

# 캐릭터 원본 크기 보관
character_size = (350, 550)

# 캐릭터 크기 조절
character = pygame.transform.smoothscale(
    character_original, character_size
)

# 캐릭터 위치
character_rect = character.get_rect(
    center=(WIDTH // 2, HEIGHT // 2)
)

# 쓰다듬기 애니메이션
petting_start= None
animation_duration= 400

speed= 5

# 화면 업데이트
pygame.display.update()

# FPS 설정
clock = pygame.time.Clock()

# 게임 실행
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 클릭 허용
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if character_rect.collidepoint(event.pos):
                print("캐릭터를 쓰다듬었어요!")
                petting_start = pygame.time.get_ticks()

    # 방향키
    keys= pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        character_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        character_rect.x += speed
    if keys[pygame.K_UP]:
        character_rect.y -= speed
    if keys[pygame.K_DOWN]:
        character_rect.y += speed

    # 화면 밖 탈출 금지
    character_rect.clamp_ip(screen.get_rect())

    # 애니메이션 초기화
    character= pygame.transform.smoothscale(
        character_original, character_size
    )

    # 쓰다듬기 애니메이션
    if petting_start is not None:
        elapsed= pygame.time.get_ticks() - petting_start

        if elapsed < animation_duration:
            profress= elapsed / animation_duration

        # 캐릭터가 살짝 커졌다가 돌아오기
        scale= 1+0.12*math.sin(progress*math.pi)

        new_size (
            int(character_size[0])
        )

    screen.fill(background_color)

    screen.blit(character, character_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()


