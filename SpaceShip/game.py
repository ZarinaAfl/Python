import pygame
from ship import SpaceShip
import time


pygame.display.init()

M = 800
N = 800

screen = pygame.display.set_mode((M, N))
screen.fill((0, 0, 0))
screen.lock()

spaceship = SpaceShip(300, 300)

def start():
    spaceship.render(screen)
    screen.unlock()
    pygame.display.flip()
    time.sleep(20)


def play():
    while True:
        pygame.event.pump()
        pressed_list = pygame.key.get_pressed()
        spaceship.move(pressed_list)

start()