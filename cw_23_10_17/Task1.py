import math
import pygame
import time

pygame.display.init()

M = 800
N = 800

screen = pygame.display.set_mode((M, N))

r = 50
x0 = 400
y0 = 400
color = (0, 0, 255)

t = time.time()
frames = 0
delta = 1
r_max = 300
r_min = 50
go = True
change_size_time = time.time()

while go:
    screen.fill((0,0,0))
    screen.lock()
    pygame.draw.circle(screen, (180, 0, 0), (x0, y0), r, 3)

    '''
    for x in range(x0 - r, x0 + r + 1):
        y = int (round((r * r - (x - x0) ** 2) ** 0.5 + y0))
        screen.set_at((x,y), color)
        y = int (round(-(r * r - (x - x0) ** 2) ** 0.5 + y0))
        screen.set_at((x, y), color)
    '''



    screen.unlock()
    pygame.display.flip()
    frames += 1
    if time.time() - t > 1:
        print ("FPS: %s" % frames)
        t = time.time()
        frames = 0

    pygame.event.pump()
    pressed_list = pygame.key.get_pressed()
    if pressed_list[pygame.K_ESCAPE]:
        go = False
    if pressed_list[pygame.K_UP]:
        y0 -= 1
    if pressed_list[pygame.K_DOWN]:
        y0 += 1
    if pressed_list[pygame.K_RIGHT]:
        x0 += 1
    if pressed_list[pygame.K_LEFT]:
        x0 -= 1
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        go = False

    if (time.time() - change_size_time > 0.01):
        r+=delta
        change_size_time = time.time()
    if (r == r_max):
        delta =-1
    elif (r == r_min):
        delta =1

time.sleep(10)
pygame.display.quit()



