import pygame

# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_heigh = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_heigh)) # 가로 세로
pygame.display.set_caption # 제목 설정

# 게임 루프
running = True  # 게임이 실행중인가
while running:
    # 이벤트 루프
    for even in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if even.type == pygame.QUIT: # 창이 닫히는 이벤트 인가
            running = False # 게임이 종료됨

pygame.quit()

