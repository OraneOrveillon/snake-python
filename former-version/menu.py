import pygame
from pygame.locals import *


from interface import Interface
from button import Button
from text import Text
from game import Game
from mixer import Mixer
import consts


# TODO Docstring
class Menu(Interface):
    """
    The menu interface
    The element which is firstly displayed when the project is ran
    Enables to access to the rest of the application
    """
    def __init__(self):
        super(Menu, self).__init__()

        # Set background
        self.render_background_color("#A04C76")

        # Set title
        title = Text(self._window, 'impact', 150, "Snake", 'black')
        title.display_text((consts.WINDOW_WIDTH / 2 - title.width / 2, 20))

        # Set buttons
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

        self._mixer = Mixer()

    def run(self):
        running = True
        switch_sound = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Closed with escape key
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        if self._selected_button > 0:
                            if switch_sound:
                                self._mixer.stop_sound(switch_sound)
                            switch_sound = self._mixer.play_sound("button-switch.wav")
                            self._buttons[self._selected_button].set_selected()
                            self._selected_button -= 1
                            self._buttons[self._selected_button].set_selected()
                    if event.key == K_DOWN:
                        if self._selected_button < len(self._buttons) - 1:
                            if switch_sound:
                                self._mixer.stop_sound(switch_sound)
                            switch_sound = self._mixer.play_sound("button-switch.wav")
                            self._buttons[self._selected_button].set_selected()
                            self._selected_button += 1
                            self._buttons[self._selected_button].set_selected()
                    if event.key == K_RETURN:
                        if self._selected_button == 0:
                            running = False
                            game = Game()
                            game.run()
                elif event.type == QUIT:
                    running = False
