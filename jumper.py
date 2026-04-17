import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
x = 400
y = 400
background = pygame.image.load('GRID-OVERLAY-01-600x600.jpg')
box_1 = pygame.Rect(100,200,100,100)
box_2 = pygame.Rect(200,300,50,75)
box_3 = pygame.Rect(400,300,10,10)
platforms = [box_1, box_2, box_3]
clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background, (0,0))
    player = pygame.Rect(x,y,100,100)
    pygame.draw.rect(screen, (255, 0, 0), box_1, 2)
    pygame.draw.rect(screen, (255, 0, 0), box_2, 2)
    pygame.draw.rect(screen, (255, 0, 0), box_3, 2)
    pygame.draw.rect(screen, (0, 255, 0), player, 2)
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
    if player.colliderect(box_1):
        y = box_1.top - player.height
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
