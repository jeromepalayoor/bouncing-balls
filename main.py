import pygame
import random

from pygame.constants import K_SPACE

width = 1200
height = 700

pygame.display.set_caption("Bouncing Balls")
win = pygame.display.set_mode((width,height))

points = []

points.append([random.randint(10,width-10),random.randint(10,height-10),random.randint(-1000,1000)/50,random.randint(-1000,1000)/50,(random.randint(0,255),random.randint(0,255),random.randint(0,255))])

run = True
while run:
    print(len(points))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        for i in range(1):
            points.append([random.randint(10,width-10),random.randint(10,height-10),random.randint(-1000,1000)/50,random.randint(-1000,1000)/50,(random.randint(0,255),random.randint(0,255),random.randint(0,255))])
    if keys[pygame.K_c]:
        points = []
        points.append([random.randint(10,width-10),random.randint(10,height-10),random.randint(-1000,1000)/50,random.randint(-1000,1000)/50,(random.randint(0,255),random.randint(0,255),random.randint(0,255))])


    win.fill((255,255,255))

    for point in points:

        if point[0] + 5 + point[2] >= width:
            point[0] = width - 5
            point[2] *= -1
        elif point[0] - 5 + point[2] <= 0:
            point[0] = 5
            point[2] *= -1
        else:
            point[0] += point[2]
        
        if point[1] + 5 + point[3] >= height:
            point[1] = height - 5
            point[3] *= -1
        elif point[1] - 5 + point[3] <= 0:
            point[1] = 5
            point[3] *= -1
        else:
            point[1] += point[3]

        pygame.draw.circle(win,point[4],(point[0],point[1]),10)

    pygame.display.update()

pygame.quit()
exit()