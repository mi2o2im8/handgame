import pygame
import sys
import math
import os

pygame.init()

# 게임 창 설정
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Character Game")

# 배경색
background_color = (240, 240, 255)

# 캐릭터 이미지 불러오기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

character_original = pygame.image.load(
    os.path.join(BASE_DIR, "chibee_character.png")
)


# 캐릭터 원본 크기 보관
character_size = (350, 550)

# 캐릭터 크기 조절
character = pygame.transform.smoothscale(
    character_original, character_size
)

# 머리랑 몸 분리
head_height= 222

# 몸 이미지(머리제거)
character_body= character.copy()
character_body.fill(
    (0,0,0,0),
    pygame.Rect(0,0,350,head_height)
)

# 머리 이미지
character_head= character.subsurface(
    (0,0,350,head_height)
).copy()

# 캐릭터 위치
character_rect = character.get_rect(
    center=(WIDTH // 2, HEIGHT // 2)
)

# 머리 클릭 판정 영역
head_rect= pygame.Rect(
    character_rect.x,
    character_rect.y,
    character_size[0],
    head_height
)

# 왼쪽 볼 클릭 영역
left_cheek_rect = pygame.Rect(
    character_rect.x + 75,
    character_rect.y + 125,
    75,
    65
)

# 오른쪽 볼 클릭 영역
right_cheek_rect = pygame.Rect(
    character_rect.x + 200,
    character_rect.y + 125,
    75,
    65
)

# 쓰다듬기 애니메이션
petting_start= None
animation_duration= 400

# 볼 늘리기 애니메이션
cheek_start= None
cheek_side= None
cheek_duration= 300

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

        # 마우스 클릭 허용
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if left_cheek_rect.collidepoint(event.pos):
                cheek_start= pygame.time.get_ticks()
                cheek_side= "left"

            elif right_check_rect.collidepoint(event.pos):
                cheek_start= pygame.time.get_ticks()
                cheek_side= "right"

            elif head_rect.collidepoint(event.pos):
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

    # 머리 클릭 영역 위치 갱신
    head_rect.topleft= character_rect.topleft

    # 볼 클릭 영역 위치 갱신
    

    # 화면 밖 탈출 금지
    character_rect.clamp_ip(screen.get_rect())

    screen.fill(background_color)
    
    # 몸 그리기
    screen.blit(character_body, character_rect)

    # 머리 쓰다듬기 애니메이션
    head_scale = 1.0

    if petting_start is not None:
        elapsed = pygame.time.get_ticks() - petting_start

        if elapsed < animation_duration:
            progress = elapsed / animation_duration
            head_scale = 1 - 0.12 * math.sin(progress * math.pi)
        else:
            petting_start = None

    # 머리 크기 조절
    new_head_height = int(head_height * head_scale)

    head_image = pygame.transform.smoothscale(
        character_head,
        (character_size[0], new_head_height)
    )

    # 머리 아래쪽 위치 고정
    screen.blit(
        head_image,
        (
            character_rect.x,
            character_rect.y + head_height - new_head_height
        )
    )

    pygame.display.update()
    clock.tick(60)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()


