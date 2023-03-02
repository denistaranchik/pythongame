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

font = pygame.font.SysFont('Arial Black', 20)
main_surface = pygame.display.set_mode(screen)




# ------- ball's configuration
#ball = pygame.Surface((20, 20))
#ball.fill((WHITE))
ball = pygame.image.load('player.png').convert_alpha()
ball_rect = ball.get_rect()
ball_speed = 6
is_working = True

# ------ enemy's configuration /def is function/ - тобто функція
def create_enemy():
    #enemy = pygame.Surface((20, 20))
    #enemy.fill(RED)
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(1, 8)
    return [enemy, enemy_rect, enemy_speed]

# ------ bonus's configuration
def create_bonus():
   # bonus = pygame.Surface((20, 20)) # --- bonus size
    #bonus.fill(GREEN) # --- bonus color
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size()) # --- bonus call
    bonus_speed = random.randint(1, 5) # -- bonus speed
    return [bonus, bonus_rect, bonus_speed]

bg = pygame.transform.scale(pygame.image.load('background.png'), screen)
bgx = 0
bgx2 = bg.get_width()
bg_speed = 3

CREATE_ENEMY = pygame.USEREVENT +1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT +2
pygame.time.set_timer(CREATE_BONUS, 3000)

enemies = []
bonuses = []
scores = 0


# ---------------- main cycle
while is_working:

    FPS.tick(90) 

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
    

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys [K_DOWN] and not ball_rect.bottom >= height:
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_speed)
    
    if pressed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

    if pressed_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move(ball_speed, 0)
    
    #main_surface.fill((BLACK)) 
    #main_surface.blit(bg, (0, 0))

    bgx -= bg_speed
    bgx2 -= bg_speed

    if bgx < -bg.get_width():
        bgx = bg.get_width()
    if bgx2 < -bg.get_width():
        bgx2 = bg.get_width()

    main_surface.blit(bg,(bgx, 0))
    main_surface.blit(bg,(bgx2, 0))

    main_surface.blit(ball, ball_rect)
    main_surface.blit(font.render(str(scores), True, BLUE), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])   # ------- / [] is index / - тобто індекс

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))    #------- 'CTRL + /' швидко закоментувати код(треба виділити і натиснути гарячі клавіші)
        
        if ball_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, 2)
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom >= height:
            bonuses.pop(bonuses.index(bonus))
        
        if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1
    
    # main_surface.fill((155, 155, 155))
    pygame.display.flip()