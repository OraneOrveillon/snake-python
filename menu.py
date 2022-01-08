import pygame
from pygame.locals import *

import consts
from mixer import Mixer
from text import Text
from button import Button
from game import Game


class Menu:
    """Menu's interface"""
    def __init__(self, window):
        """
        - Initializes the buttons and put them in a tuple
        - Initializes the mixer
        - _selected_button is an index and is initialized at 0 : the first button "PLAY"
        :param window: Application's window
        """
        self._window = window

        self._buttons = (Button(self._window.screen,
                                consts.WINDOW_WIDTH / 2 - consts.MENU_BUTTON_WIDTH / 2,
                                consts.MENU_BUTTON1_Y,
                                "PLAY"),
                         Button(self._window.screen,
                                consts.WINDOW_WIDTH / 2 - consts.MENU_BUTTON_WIDTH / 2,
                                consts.MENU_BUTTON2_Y,
                                "SETTINGS"),
                         Button(self._window.screen,
                                consts.WINDOW_WIDTH / 2 - consts.MENU_BUTTON_WIDTH / 2,
                                consts.MENU_BUTTON3_Y,
                                "SCORES")
                         )

        self._selected_button = 0
        self._buttons[self._selected_button].set_selected()

        self._mixer = Mixer()

    def draw(self):
        """Set the background, the title and draws the buttons"""
        self._window.screen.fill("#A04C76")

        title = Text(self._window.screen, consts.FONT_NAME, consts.MENU_TITLE_FONT_SIZE, "Snake", 'black')
        title.display_text((consts.WINDOW_WIDTH / 2 - title.width / 2, 20))

        for i in range(len(self._buttons)):
            self._buttons[i].draw()

    def run(self):
        """
        - Keeps the window displaying until it's closed with Escape key or the cross
        - When the up or down key is pressed, switched the selected button and plays the the corresponding sound
        - Stops a sound before playing another to prevent from some sound glitches
        - When Enter key is pressed, runs the corresponding interface
        """
        running = True
        switch_sound = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
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
                            self._window.game = Game(self._window)
                            self._window.game.draw()
                            self._window.game.run()
                elif event.type == QUIT:
                    running = False
