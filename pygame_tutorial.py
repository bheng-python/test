import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

pikachu = pygame.image.load('pikachu_unc.png').convert()
pikachu.set_colorkey((255, 255, 255))
pikachu_small = pygame.transform.scale(pikachu, (100, 100))
clock = pygame.time.Clock()
forest = pygame.image.load('Forest_Trees_Pixel_BackGround.jpg').convert()
forest_big = pygame.transform.scale(forest, (892, 500))
x_background = 0
y_background = 0
x = 200
y = 400
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(forest_big, (x_background-500,y_background))
    screen.blit(forest_big, (x_background,y_background))
    screen.blit(pikachu_small, (200, 300))
    #x += 1
#movements for character
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y = y - 1
    if keys[pygame.K_DOWN]:
        y = y + 1
    if keys[pygame.K_LEFT]:
        x = x - 1
    if keys[pygame.K_RIGHT]:
        x = x + 1
    if keys[pygame.K_r]:
        x = 200
        y = 200
#movements for background
    if keys[pygame.K_w]:
        y_background = y_background - 1
    if keys[pygame.K_s]:
        y_background = y_background + 1
    if keys[pygame.K_a]:
        x_background = x_background - 1
    if keys[pygame.K_d]:
        x_background = x_background + 1
#resets movement(scroller)
    if(x == 500):
        x = -599
    if(x == -100):
        x = 999
    if(y == 500):
        y = -599
    if(y == -100):
        y = 999
    if(x_background == 500):
        x_background = -99
    if(x_background == -100):
        x_background = 499
    if(y_background == 500):
        y_background = -99
    if(y_background == -100):
        y_background = 499
    clock.tick(240)
    pygame.display.flip()
pygame.quit()
