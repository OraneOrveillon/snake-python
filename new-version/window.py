import pygame

import consts
from menu import Menu
from game import Game


class Window:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Python")
        self._menu = Menu(self)
        self._game = None

    def run(self):
        # Application starts at Menu interface
        self._menu.draw()
        self._menu.run()

    @property
    def screen(self):
        return self._screen

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value

    @property
    def menu(self):
        return self._menu
