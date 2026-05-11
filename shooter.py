import pygame
import time

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
x = 0
y = 0
map = pygame.image.load('dart_board.png').convert()
dart = pygame.image.load('dart.png').convert_alpha()
dart = pygame.transform.scale(dart, (32,32))
dart.set_colorkey((255, 255, 255))
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(map, (x, y))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x = 0
                y = 0
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_UP]:
        y -= 10
        print("y_score", y)
    if keys[pygame.K_DOWN]:
        y += 10
        print("y_score", y)
    if keys[pygame.K_LEFT]:
        x -= 10
        print("x_score", x)
    if keys[pygame.K_RIGHT]:
        x += 10
        print("x_score", x)
    if keys[pygame.K_r]:
        x = 0
        y = 0
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
