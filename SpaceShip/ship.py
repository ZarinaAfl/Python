import pygame

class SpaceShip:
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0



    def rotate(self):
        pass

    def move(self, pressed_list):
        if pressed_list[pygame.K_ESCAPE]:
            go = False
        if pressed_list[pygame.K_UP]:
            self.y0 -= 1
        if pressed_list[pygame.K_DOWN]:
            self.y0 += 1
        if pressed_list[pygame.K_RIGHT]:
            self.x0 += 1
        if pressed_list[pygame.K_LEFT]:
            self.x0 -= 1


    def render(self, surface):
        x = self.x0
        y = self.y0
        pygame.draw.rect(surface, (255, 0, 0), (x, y, 40, 70), 2)
        pygame.draw.polygon(surface, (255, 0, 0), [[x-60, y-100], [x-160, y], [x+40, y]], 2)
        pygame.draw.rect(surface, (255, 0, 0), (x-160, y, 40, 70), 2)

    def shoot(self):
        pass