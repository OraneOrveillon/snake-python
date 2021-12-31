import pygame

from text import Text
import consts


# TODO Docstring
class Button:
    def __init__(self, parent_screen, x, y, text):
        self._parent_screen = parent_screen
        self._x = x
        self._y = y
        self._text = text
        self._selected = False

        self.draw()

    def draw(self):
        rect_button = pygame.Rect(self._x, self._y, consts.BUTTON_WIDTH, consts.BUTTON_HEIGHT)
        pygame.draw.rect(self._parent_screen, consts.BUTTON_COLOR, rect_button)
        text_button = Text(
            self._parent_screen,
            consts.BUTTON_FONT_NAME,
            consts.BUTTON_FONT_SIZE,
            self._text,
            consts.BUTTON_FONT_COLOR)
        text_button.display_text((
            rect_button.centerx - text_button.width / 2,
            rect_button.centery - text_button.height / 2))

    def set_selected(self):
        self._selected = True
        self.draw()

    def __eq__(self, button):
        if self._x == button.x and self._y == button.y and self._text == button.text:
            return True
        return False

    # ---------- GETTERS / SETTERS SPACE ---------- #
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def text(self):
        return self._text
