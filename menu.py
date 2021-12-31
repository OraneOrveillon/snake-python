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

        pygame.display.flip()

    def draw_button(self, x, y, width, height, text):
        rect_button = Rect(x, y, width, height)
        pygame.draw.rect(self._window, consts.BUTTON_COLOR, rect_button)
        text_button = Text(
            self._window,
            consts.BUTTON_FONT_NAME,
            consts.BUTTON_FONT_SIZE,
            text,
            consts.BUTTON_FONT_COLOR)
        text_button.display_text((
            rect_button.centerx - text_button.width / 2,
            rect_button.centery - text_button.height / 2))

    @staticmethod
    def run():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Closed with escape key
                    if event.key == K_ESCAPE:
                        running = False
                    # Restart the game
                elif event.type == QUIT:
                    running = False


menu = Menu()
menu.run()
