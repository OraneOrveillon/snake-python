import pygame
import random

import constants


class Apple:
    """The object that the snake is going to eat to increase score"""

    def __init__(self, parent_screen):
        """
        - Load the apple image
        - Initialize it's first coordinates x, y at 0, then move it to a random position with move()
        :param parent_screen: The parent window
        """
        self._image = pygame.image.load("resources/apple.jpg").convert()
        self._parent_screen = parent_screen
        # self._x = constants.SNAKE_SIZE * 3
        # self._y = constants.SNAKE_SIZE * 3
        self._x = self._y = 0
        self.move()

    def draw(self):
        """Make appear the apple image on the screen"""
        self._parent_screen.blit(self._image, (self._x, self._y))
        pygame.display.flip()

    def move(self):
        """Change apple's position randomly on the screen"""
        # Window's width / SIZE - 1 -> 1000 / 40 - 1 = 25
        self._x = random.randint(1, constants.WINDOW_WIDTH / constants.SNAKE_SIZE -1) * constants.SNAKE_SIZE
        # Window's length / SIZE - 1 -> 800 / 40 - 1 = 20
        self._y = random.randint(1, constants.WINDOW_LENGTH / constants.SNAKE_SIZE - 1) * constants.SNAKE_SIZE

    # ---------- GETTERS / SETTERS SPACE ---------- #
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
