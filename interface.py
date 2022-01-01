from abc import ABC
import pygame

import consts


class Interface(ABC):
    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Python")
