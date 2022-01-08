import pygame

import consts
from menu import Menu
from game import Game


class Window:
    """The top hierarchy of the application, deals with running different interfaces"""
    def __init__(self):
        """
        - Initializes pygame
        - Displays the application's window
        - Has an attribute for each interface of the application
        """
        pygame.init()
        self._screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Python")
        self._menu = Menu(self)
        self._game = None

    def run(self):
        """Draws the menu and runs it"""
        # Application starts at Menu interface
        self._menu.draw()
        self._menu.run()

    # ---------- GETTERS / SETTERS SPACE ---------- #
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
