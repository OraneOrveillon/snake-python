import pygame
import random

import constants


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = constants.SIZE * 3
        self.y = constants.SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    # TODO Constantes pour longueur, largeur de l'écran et deuxième paramètre de randit (width/SIZE-1 et length/SIZE-1)
    def move(self):
        # Window's width / SIZE - 1 -> 1000 / 40 - 1 = 25
        self.x = random.randint(1, 24) * constants.SIZE
        # Window's length / SIZE - 1 -> 800 / 40 - 1 = 20
        self.y = random.randint(1, 19) * constants.SIZE
