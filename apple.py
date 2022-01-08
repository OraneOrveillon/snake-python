import pygame
import random

import consts


class Apple:
    """The object that the snake is going to eat to increase score"""

    def __init__(self, parent_screen):
        """
        - Loads the apple image
        - Initializes it's first coordinates x, y at 0, then moves it to a random position with move()
        :param parent_screen: The parent window
        """
        self._image = pygame.image.load("assets/snowflake.png").convert_alpha()
        self._parent_screen = parent_screen
        self._x = self._y = 0
        self.move()

    def draw(self):
        """Makes appear the apple image on the screen"""
        self._parent_screen.blit(self._image, (self._x, self._y))

    def move(self):
        """Changes apple's position randomly on the screen"""
        self._x = random.randint(1, consts.WINDOW_WIDTH / consts.BLOCK_SIZE - 1) * consts.BLOCK_SIZE
        self._y = random.randint(1, consts.WINDOW_HEIGHT / consts.BLOCK_SIZE - 1) * consts.BLOCK_SIZE

    # ---------- GETTERS / SETTERS SPACE ---------- #
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
