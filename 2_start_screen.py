import pygame

# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) # 원 그리기 *위치, 색깔, 중심위치, 반지름 두께





# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_heigh = 720 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_heigh)) # 가로 세로
pygame.display.set_caption # 제목 설정

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120) # 가로 세로 , 위 아래
start_button.center = (120, screen_heigh - 120) # 가로 세로

# 색깔
BLACK = (0, 0, 0) # RGB 값
WHITE = (255, 255, 255)


# 게임 루프
running = True  # 게임이 실행중인가
while running:
    # 이벤트 루프
    for even in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if even.type == pygame.QUIT: # 창이 닫히는 이벤트 인가
            running = False # 게임이 종료됨

    # 화면 검정색 채우기
    screen.fill(BLACK)

    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()

# 기본작인 파이게임 틀