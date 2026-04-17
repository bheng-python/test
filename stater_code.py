import pygame

pygame.init()

debug_mode = True

screen = pygame.display.set_mode((600,336))

mario = pygame.image.load('mariomove.gif')
mario = pygame.transform.scale(mario, (mario.get_width()*.2, mario.get_height()*.2))

backg = pygame.image.load('background.png')
backg = pygame.transform.scale(backg, (backg.get_width()*2, backg.get_height()*2))

#floor_rect = pygame.Rect(0,300,600,36) #x,y,width, height

platforms = [
    pygame.Rect(0,300,600,36),
    pygame.Rect(200, 220, 120, 20),
    pygame.Rect(400, 160, 100, 20)
]

clock = pygame.time.Clock()

running = True
on_ground = False
x = 1
y = 240
vy = 0
gravity = 0.3

while running:
    #Single key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y-10



    #Continuous movement press/press and hold
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and (on_ground == True):
        vy = -8
        on_ground = False
    if keys[pygame.K_DOWN]:
        y = y+1
    if keys[pygame.K_LEFT]:
        x = x-1
    if keys[pygame.K_RIGHT]:
        x = x+1

    vy = gravity + vy
    y = vy + y

    screen.fill((0,0,0))


    mario_rect = mario.get_rect(topleft=(x,y))

    for platform in platforms:
        if mario_rect.colliderect(platform):
            if vy > 0:
                y = platform.top - mario_rect.height
                vy = 0
                on_ground = True
            elif vy < 0:
                y = platform.bottom
                vy = 0
            if x < platform.left-50:
                x = platform.left-mario_rect.width
            elif x > platform.right+50:
                x = platform.right
    screen.blit(backg, (0,0))
    screen.blit(mario, (x, y))

    if debug_mode == True:
        pygame.draw.rect(screen, (0, 255, 0), mario_rect, 2)
        #pygame.draw.rect(screen, (255, 255, 255), floor_rect, 2)
        for platform in platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform, 2)







    clock.tick(60)

    pygame.display.flip()

pygame.quit()
