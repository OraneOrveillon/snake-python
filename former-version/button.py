import pygame

from text import Text
import consts


class Button:
    """Enable to create buttons on the screen
    Only visually, without associated commands
    """
    def __init__(self, parent_screen, x, y, text):
        """
        - Initialize a button with given parameters and draw it on the screen
        - Attribute _selected : If the button is selected or not by user
        :param parent_screen: The parent window
        :param x: X position
        :param y: Y position
        :param text: The text displayed on the button
        """
        self._parent_screen = parent_screen
        self._x = x
        self._y = y
        self._text = text
        self._selected = False

        self.draw()

    def draw(self):
        """
        - Create a rectangle with x and y position and constants for width and height
        - Draw the rectangle with a color given by a constant
        - The given constant changes depending of the attribute _selected
        - Create a text for the button
        - Display the text at the center of the rectangle
        - Update the screen
        """
        rect_button = pygame.Rect(self._x, self._y, consts.BUTTON_WIDTH, consts.BUTTON_HEIGHT)
        pygame.draw.rect(self._parent_screen,
                         (consts.BUTTON_COLOR, consts.SELECTED_BUTTON_COLOR)[self._selected],
                         rect_button)
        text_button = Text(
            self._parent_screen,
            consts.BUTTON_FONT_NAME,
            consts.BUTTON_FONT_SIZE,
            self._text,
            (consts.BUTTON_FONT_COLOR, consts.SELECTED_BUTTON_FONT_COLOR)[self._selected])
        text_button.display_text((
            rect_button.centerx - text_button.width / 2,
            rect_button.centery - text_button.height / 2))

        pygame.display.flip()

    def set_selected(self):
        """Switch the selected state and redraw the button"""
        self._selected = not self._selected
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
