import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 800, 600
BLACK = 0, 0, 0                              # ----------- BLACK is /variable/ - тобто змінна
WHITE = 255, 255, 255
YELLOW = 255, 255, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
RED = 255, 0, 0

main_surface = pygame.display.set_mode(screen)

# ------- ball's configuration
ball = pygame.Surface((20, 20))
ball.fill((WHITE))
ball_rect = ball.get_rect()
ball_speed = 4
is_working = True

# ------ enemy's configuration /def is function/ - тобто функція
def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RED)
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(1, 8)
    return [enemy, enemy_rect, enemy_speed]

# ------ bonus's configuration


CREATE_ENEMY = pygame.USEREVENT +1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []


# ---------------- main cycle
while is_working:

    FPS.tick(90) 

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
    
    

    #ball_rect = ball_rect.move(0, ball_speed)
    #if ball_rect.bottom >= height or ball_rect.top <= 0:
        #ball.fill(YELLOW)
        #ball_speed[1] = -ball_speed[1]

    #if ball_rect.right >= width:
        #ball.fill(BLUE)
        #ball_speed[0] = -ball_speed[0]

    #if ball_rect.left <= 0:
        #ball.fill(BLUE)
        #[0] = -ball_speed[0]
    

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys [K_DOWN] and not ball_rect.bottom >= height:
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_speed)
    
    if pressed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

    if pressed_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move(ball_speed, 0)
    
    main_surface.fill((BLACK)) 
    main_surface.blit(ball, ball_rect)

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])   # ------- / [] is index / - тобто індекс

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))    #------- 'CTRL + /' швидко закоментувати код(треба виділити і натиснути гарячі клавіші)
        
        if ball_rect.colliderect(enemy[1]):
            enemies.pop(enemies.index(enemy))

    
    # main_surface.fill((155, 155, 155))
    pygame.display.flip()