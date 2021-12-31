import pygame
import consts


class Text:
    def __init__(self, parent_screen, font_name, size, content, color):
        """
        - Generate a pygame object font with given parameters
        - Generate a pygame object text with given parameters
        - Save the text's width and height in attributes
        :param parent_screen: The parent window
        :param font_name: The font name ('arial', etc)
        :param size: The font size
        :param content: The string that will be displayed on the window
        :param color: The text's color in the (255, 255, 255) format
        """
        self._parent_screen = parent_screen
        self._font_name = font_name
        self._size = size
        self._font = pygame.font.SysFont(font_name, size)
        self._content = content
        self._color = color
        self._text = self._font.render(content, True, color)
        self._width = self._text.get_width()
        self._height = self._text.get_height()

    def display_text(self, position: ()):
        """
        Display the object on the window with the given position
        :param position: The text's position on the window in the (x, y) format
        """
        self._parent_screen.blit(self._text, position)

    def set_bold(self, value):
        """Change the font's bold attribute on True or False and regenerate the text"""
        self._font.set_bold(value)
        self.regenerate_text()

    def set_italic(self, value):
        """Change the font's italic attribute on True or False and regenerate the text"""
        self._font.set_italic(value)
        self.regenerate_text()

    def set_underlined(self, value):
        """Change the font's underlined attribute on True or False and regenerate the text"""
        self._font.set_underline(value)
        self.regenerate_text()

    def regenerate_text(self):
        """Regenerate the text, called when 1 or more attributes are changed"""
        self._text = self._font.render(self._content, True, self._color)

    # ---------- GETTERS / SETTERS SPACE ---------- #
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
