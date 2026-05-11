import pygame
import time

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
x = -1550
y = -660
y_angle = 0

map = pygame.image.load('pixil-frame-0.png').convert()
map = pygame.transform.scale(map, (2000, 2000))

running = True
while running:
    screen.fill((26,82,31))
    rotated_map = pygame.transform.rotate(map, y_angle)
    screen.blit(rotated_map, (x, y))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                y_angle += 5
                print("y_angle_score", y_angle)
            if event.key == pygame.K_d:
                y_angle -= 5
                print("y_angle_score", y_angle)
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_UP]:
        y += 10
        print("y_score", y)
    if keys[pygame.K_DOWN]:
        y -= 10
        print("y_score", y)
    if keys[pygame.K_LEFT]:
        x += 10
        print("x_score", x)
    if keys[pygame.K_RIGHT]:
        x -= 10
        print("x_score", x)
    if keys[pygame.K_r]:
        x = -1550
        y = -660
    if y_angle > 360:
        y_angle = 0
    if y_angle < 0:
        y_angle = 360
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
