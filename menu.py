import pygame
from pygame.locals import *

from button import Button
import consts


# TODO Docstring
class Menu:
    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Python")

        # Set background
        self._window.fill("#A04C76")

        self._buttons = (Button(self._window,
                                consts.WINDOW_WIDTH / 2 - consts.BUTTON_WIDTH / 2,
                                consts.BUTTON1_Y,
                                "PLAY"),
                         Button(self._window,
                                consts.WINDOW_WIDTH / 2 - consts.BUTTON_WIDTH / 2,
                                consts.BUTTON2_Y,
                                "SETTINGS"),
                         Button(self._window,
                                consts.WINDOW_WIDTH / 2 - consts.BUTTON_WIDTH / 2,
                                consts.BUTTON3_Y,
                                "SCORES")
                         )

        self._selected_button = 0
        self._buttons[self._selected_button].set_selected()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Closed with escape key
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        if self._selected_button > 0:
                            self._buttons[self._selected_button].set_selected()
                            self._selected_button -= 1
                            self._buttons[self._selected_button].set_selected()
                    if event.key == K_DOWN:
                        if self._selected_button < len(self._buttons) - 1:
                            self._buttons[self._selected_button].set_selected()
                            self._selected_button += 1
                            self._buttons[self._selected_button].set_selected()
                elif event.type == QUIT:
                    running = False


menu = Menu()
menu.run()
