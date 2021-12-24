import pygame
import constants


# TODO : Docstring
class Text:
    def __init__(self, parent_screen, font_name, size, content, rgb_color):
        self._parent_screen = parent_screen
        self._font_name = font_name
        self._size = size
        self._font = pygame.font.SysFont(font_name, size)
        self._content = content
        self._rgb_color = rgb_color
        self._text = self._font.render(content, True, rgb_color)
        self._width = self._text.get_width()
        self._height = self._text.get_height()

    def display_text(self, position: ()):
        self._parent_screen.blit(self._text, position)

    def set_bold(self, value):
        self._font.set_bold(value)
        self.regenerate_font()

    def set_italic(self, value):
        self._font.set_italic(value)
        self.regenerate_font()

    def set_underlined(self, value):
        self._font.set_underline(value)
        self.regenerate_font()

    def regenerate_font(self):
        self._text = self._font.render(self._content, True, self._rgb_color)

    # ---------- GETTERS / SETTERS SPACE ---------- #
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
