import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

pikachu = pygame.image.load('pikachu_unc.png').convert()
pikachu.set_colorkey((255, 255, 255))

clock = pygame.time.Clock()

x = 0


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(pikachu, (x,0))
    x += 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if(x == 500):
        x = -500
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
