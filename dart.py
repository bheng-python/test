#various imports
import pygame
import math
#first loads up pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))#might make bigger but just sets up the display and how big it is
clock = pygame.time.Clock()#sets up the clock code
#image setup
dart_orig = pygame.image.load("dart.png").convert_alpha()#this code loads the darts
dart_orig = pygame.transform.scale(dart_orig, (50, 15))#this code scales the dart properly
dart_orig = pygame.transform.rotate(dart_orig, 180)#this code rotates the dart so it faces the right direction when its still
dart_orig.set_colorkey((255,255,255))
#varraibles
mode = "Hard"
enemy_health_mult = 1
damage_mult = 1
dart_pos = [150, 450]#this is for the darts position along the game board
dart_vel = [0, 0]#this is for the current speed and direction for the dart
is_flying = False#this dectects if its flying such as when you release you mouse after you press down and drag
drag_start = None#None is nil which means theres no object in its memoery and it will still not give a error code
MAX_DRAG = 150  #this is how big you can drag the circle, change if you want it to go faster or slower
GRAVITY = 0.4 #change this to higher if you wont your dart to go down faster and lower if you want it to go more straight, also the downforce added each frame
running = True#first sets running to true
start = 0 #this is for running a animation for the start
animation_length = 60 #change this dev if you want it to last longer
while running:
    #if start < animation_length:
    if mode == "Easy":
        GRAVITY = 0.3
        enemy_health_mult = 0.7
        damage_mult = 1.5
    if mode == "Normal":
        GRAVITY = 0.5
        enemy_health_mult = 1
        damage_mult = 1
    if mode == "Hard":
        GRAVITY = 0.7
        damage_mult = 0.6
        enemy_health_mult = 1.3
    screen.fill((0, 0, 0))#fills the screen so the past images dont intefere with the game
    mouse_pos = pygame.mouse.get_pos()#allows for mouse movements
    for event in pygame.event.get():#gets various different events
        if event.type == pygame.QUIT:#dectects if you press the x button and quits the game
            running = False#quits the game
        if event.type == pygame.MOUSEBUTTONDOWN:#this dectects if the mouse is down and then runs the following code
            drag_start = event.pos#this sets the darts position to where you orgginaly pressed down with your mouse
            x, y = event.pos#because event.pos is a tuple you cant use ussal methods for declaring it so you have to remove the tuple part by setting it to two varabiles which i put as x and y
            if y < 300:
                y = 305
            if x > 250:
                x = 235
            drag_start = (x,y)
            dart_pos = list(drag_start)#this adds the darts position to the list
            is_flying = False#this sets is_flying to false because you havent released yet
        if event.type == pygame.MOUSEBUTTONUP and drag_start:#this dectects if the mouse is up
            # Calculate total distance dragged
            dx = event.pos[0] - drag_start[0]#cacluatles the distince between when you first clicked whcih is dragstart and when you release which is event.pos for x
            dy = event.pos[1] - drag_start[1]#cacluatles the distince between when you first clicked whcih is dragstart and when you release which is event.pos for y
            dist = math.hypot(dx, dy)#this caculates the length of the diagonal between the start point of x,y and the end point of x,y ysing pythagoreon theorem

            # If dragged too far, shrink the vector to MAX_DRAG, this is for limiting how far you can drag
            if dist > MAX_DRAG: #This checks if its dragged to far
                scale = MAX_DRAG / dist
                dx *= scale#this multiplies the dx by the scale
                dy *= scale#this multiplies the dy by the scale

            dart_vel = [dx * 0.15, dy * 0.15]#this gets the darts initally speed based on how far you draged
            is_flying = True#this changes is flying to true so it can print the dart, turns on pyhsics ofr the dart
            drag_start = None#resets the drag_start to None so it can be replayed

    #the code is used for physics
    if is_flying:
        dart_vel[1] += GRAVITY
        dart_pos[0] += dart_vel[0]
        dart_pos[1] += dart_vel[1]
        if dart_pos[1] < 300:
            dart_pos[1] = 300
            if dart_vel[1] < 0:
                dart_vel[1] *= -0.2
        angle = -math.degrees(math.atan2(dart_vel[1], dart_vel[0]))

    else:
        angle = 0 #if its not throwing its angle will be 0 so it will be flat, may change in future so it will follow the mouse

    #this code draws the launch area and the line
    if drag_start: #this checks if yur mouse is down and draws a circle around where you initally clicked down to limit how far you can drag
        # Draw a circle showing the max drag limit
        pygame.draw.circle(screen, (100, 100, 100), drag_start, MAX_DRAG, 2) #this draws a circle where you clicked down with a diamter of MAX_DRAG and this can change with variables


        dx = mouse_pos[0] - drag_start[0]#cacluates how many pixels moved between when you first clicked and when you released/dragged for the x axis
        dy = mouse_pos[1] - drag_start[1]#this caclualtes how many pixeks you moved when you first clikced and when you dragged for the y axis
        dist = math.hypot(dx, dy)#this finds the straight line distince between the dx and dy

        line_end = mouse_pos
        if dist > MAX_DRAG:#checks if the distince of the line you dragged is greater then the set amount and resets it back to its nearest point along the circle
            line_end = (drag_start[0] + dx * MAX_DRAG / dist, #this makes sure the line stops perfectly at 100 pixels because of dx * max_drag / dist such as if you dragged 200 to the ight it would be 200 * 100/200 which would = 100
                        drag_start[1] + dy * MAX_DRAG / dist) #this the same thing as the previous line but for the y axis, used a little yt to get this code cuz lwk kinda hard,

        pygame.draw.line(screen, (255, 255, 255), drag_start, line_end, 2)#this draws a line from where you iniitally pressed down and the line end math

    #draws the dart
    rotated_dart = pygame.transform.rotate(dart_orig, angle)#this draws the dart and changes its rotation as it goes along its trijcetory.
    rect = rotated_dart.get_rect(center=dart_pos)#this sets the center of the dart as its rotation point so not errors occur and make it look nicer
    screen.blit(rotated_dart, rect)#this finnaly blits the dart for each tick
    #code for wakks
    middle_wall = pygame.draw.line(screen, (0, 255, 0), (0,300), (800,300), 5)#theses are lines for the horzinatl axis so it can have more info on the top and not just be a dart playing game cuz thats boring
    bottom_wall = pygame.draw.line(screen, (0, 255, 0), (0, 597.5), (800, 597.5), 5)
    #code for the box you can fire in
    #pygame.draw.line(screen, (0, 255, 0), (0,450), (250, 450), 5)#this is for the horzantal line for inventory.
    small_wall_left = pygame.draw.line(screen, (0, 255, 0), (2.5, 300), (2.5,600), 5)
    small_wall_right = pygame.draw.line(screen, (0, 255, 0), (797.5, 300), (797.5,600), 5)
    small_wall_middle = pygame.draw.line(screen, (0, 255, 0), (250,300), (250,600), 5)#these are lines for a box so you can only fire the dart from a certain area.
    #if start < animation_length:
    start += 1
    pygame.display.flip()#shows the info on the screen
    clock.tick(60)#the tick rate

pygame.quit()#this finnaly quits the game after running is set the false, may make a end scene could be cool
