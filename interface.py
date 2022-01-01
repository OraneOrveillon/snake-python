from abc import ABC, abstractmethod
import pygame

import consts


# TODO Docstring
# TODO finir d'implémenter
class Interface:
    def __init__(self):
        """Initialize pygame, create the window with its dimensions and add a title"""
        pygame.init()
        self._window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Python")

    def render_background_color(self, color):
        self._window.fill(color)

    def render_background_image(self, image):
        pass

    @abstractmethod
    def run(self):
        pass
