import pygame

from text import Text
import consts


class Button:
    """Enables to create buttons on the screen
    Only visually, without associated commands
    """
    def __init__(self, parent_screen, x, y, text):
        """
        - Initializes a button with given parameters
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

    def draw(self):
        """
        - Creates a rectangle with x and y position and constants for width and height
        - Draws the rectangle with a color given by a constant
        - Creates a text for the button
        - Displays the text at the center of the rectangle
        - The given constants for colors change depending of the attribute _selected
        - Update the screen
        """
        rect_button = pygame.Rect(self._x, self._y, consts.MENU_BUTTON_WIDTH, consts.MENU_BUTTON_HEIGHT)
        pygame.draw.rect(self._parent_screen,
                         (consts.BUTTON_COLOR, consts.SELECTED_BUTTON_COLOR)[self._selected],
                         rect_button)
        text_button = Text(
            self._parent_screen,
            consts.FONT_NAME,
            consts.MENU_BUTTON_FONT_SIZE,
            self._text,
            (consts.BUTTON_FONT_COLOR, consts.SELECTED_BUTTON_FONT_COLOR)[self._selected])
        text_button.display_text((
            rect_button.centerx - text_button.width / 2,
            rect_button.centery - text_button.height / 2))

        pygame.display.flip()

    def set_selected(self):
        """Switches the selected state and redraws the button"""
        self._selected = not self._selected
        self.draw()

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
