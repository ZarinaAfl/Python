from IWeapon import Weapon
from PIL import Image
import pygame
import time

pygame.display.init()
M = 800
N = 800
screen = pygame.display.set_mode((M, N))
screen.fill((0, 0, 0))


#снаряд
class Shell(Weapon):
    DAMAGE = 10

    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 50)



    def draw(self):
        img = pygame.image.load("shell.png")
        img = pygame.transform.scale(img, (50, 50))
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(10)

    def shoot(self):
        pass

#бомба
class Bomb(Weapon):
    DAMAGE = 22

    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 65, 50)


    def draw(self):
        img = pygame.image.load("bomb.png")
        img = pygame.transform.scale(img, (65, 50))
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(10)

    def shoot(self):
        pass

class Rocket(Weapon):
    DAMAGE = 15

    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 50)



    def draw(self):
        img = pygame.image.load("rocket.png")
        img = pygame.transform.scale(img, (50, 50))
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(10)

    def shoot(self):
        pass

#летающая тарелка
class Saucer(Weapon):
    DAMAGE = 25

    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 50)


    def draw(self):
        img = pygame.image.load("saucer.png")
        img = pygame.transform.scale(img, (50, 50))
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(10)

    def shoot(self):
        pass





p = Saucer(screen)
p.draw()