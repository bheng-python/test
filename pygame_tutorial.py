import pygame
import time
pygame.init()

debug_mode = True

screen = pygame.display.set_mode((500,500))

pikachu = pygame.image.load('pikachu_unc.png').convert()
pikachu.set_colorkey((255, 255, 255))
pikachu = pygame.transform.scale(pikachu, (100, 100))
clock = pygame.time.Clock()
forest = pygame.image.load('Forest_Trees_Pixel_BackGround.jpg').convert()
forest = pygame.transform.scale(forest, (892, 500))
floor_rect = pygame.Rect(0,430,892,70) #x,y,width,height
bullet = pygame.image.load('bullet_blue.png').convert()
bullet.set_colorkey((0,0,0))
bullet = pygame.transform.scale(bullet, (50, 50))
lose_sign = pygame.image.load('lose_sign.jpg').convert()
lose_sign.set_colorkey((0,0,0))
x_background = 0
y_background = 0
x = 200
y = 200
x_bullet = int()
running = True
while running:
    screen.fill((0, 0, 0))
    #screen.blit(forest_big, (x_background-500,y_background))
    #screen.blit(forest_big, (x_background,y_background))
    screen.blit(forest, (0,0))
    screen.blit(pikachu, (x, y))
    pikachu_rect = pikachu.get_rect(topleft=(x,y))
    screen.blit(bullet, (x_bullet, 200))
    bullet_rect = bullet.get_rect(topleft=(x_bullet,200))
    x_bullet += 3
    if bullet_rect.colliderect(pikachu_rect):
        screen.blit(lose_sign, (200, 200))
        pygame.time.wait(5000)
        #when collided it breaks cuz its still collides with object
    if(debug_mode):
        pygame.draw.rect(screen, (0, 255, 0), pikachu_rect, 2)
        pygame.draw.rect(screen, (255, 255, 255), floor_rect, 2)
        pygame.draw.rect(screen, (255, 0, 0), bullet_rect, 2)
#movements for character
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y - 50
            if event.key == pygame.K_e:
                if debug_mode == True:
                    debug_mode = False
                elif debug_mode == False:
                    debug_mode = True
    keys = pygame.key.get_pressed()
#movement for character
    if keys[pygame.K_UP]:
        y = y - 1
    if keys[pygame.K_DOWN]:
        y = y + 1
        if pikachu_rect.colliderect(floor_rect):
            y = y -1
    if keys[pygame.K_LEFT]:
        x = x - 1
    if keys[pygame.K_RIGHT]:
        x = x + 1
    if keys[pygame.K_r]:
        x = 200
        y = 200
#    if keys[pygame.K_e]:
#        debug_mode = False
#    if keys[pygame.K_q]:
#        debug_mode = True
#movements for background
    #if keys[pygame.K_w]:
        #y_background = y_background - 1
    #if keys[pygame.K_s]:
        #y_background = y_background + 1
    #if keys[pygame.K_a]:
        #x_background = x_background - 1
    #if keys[pygame.K_d]:
        #x_background = x_background + 1
#resets movement(scroller(character))
    if(x > 500):
        x = -99
    if(x < -100):
        x = 499
    if(y > 500):
        y = -99
    if(y < -100):
        y = 499
#resets movement(bullets)
    if(x_bullet > 500):
        x_bullet = -99
    if(x_bullet < -100):
        x_bullet = 499
#resets movement(scroller(background))
#    if(x_background == 500):
#        x_background = -99
#    if(x_background == -100):
#        x_background = 499
#    if(y_background == 500):
#        y_background = -99
#    if(y_background == -100):
#        y_background = 499
    clock.tick(240)
    pygame.display.flip()
pygame.quit()
