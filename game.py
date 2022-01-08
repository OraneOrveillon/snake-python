import pygame
from pygame.locals import *
import time

import consts
from mixer import Mixer
from text import Text
from snake import Snake
from apple import Apple


class Game:
    """
    Game's interface
    Deals with the game's development
    """
    def __init__(self, window):
        """
        Initializes the snake, an apple and the mixer
        Sets the pause state at false
        :param window: Application's window
        """
        self._window = window
        self._snake = Snake(self._window.screen)
        self._apple = Apple(self._window.screen)
        self._mixer = Mixer()
        self._pause = False

    def draw(self):
        """
        Plays the background music
        Draws the snake and the apple
        """
        self._mixer.play_background_music()
        self._snake.draw()
        self._apple.draw()

    def run(self):
        """
        - Keeps the window displaying until it's closed with Escape key or the cross
        - If the game is on pause : displays the game over screen and returns on Menu if Enter key is pressed
        - If the game is not on pause : calls play()
        - Moves the snake when a direction key is pressed
        """
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        if self._pause:
                            running = False
                            self._window.menu.draw()
                            self._window.menu.run()

                    if not self._pause:
                        if event.key == K_UP:
                            self._snake.move_up()

                        if event.key == K_DOWN:
                            self._snake.move_down()

                        if event.key == K_LEFT:
                            self._snake.move_left()

                        if event.key == K_RIGHT:
                            self._snake.move_right()

                elif event.type == QUIT:
                    running = False

            if not self._pause:
                self.play()
            else:
                self.show_game_over()

            # Basically the snake's speed
            time.sleep(self._snake.speed)

    def play(self):
        """
        - Sets the background
        - Draws the grid
        - Makes the snake walk
        - Redraws the apple
        - Displays the score
        - If the snake's is touching the apple --> increase score
        - If the snake's head is touching its body --> game over
        - If the snake's head is touching a wall --> game over
        """
        self._window.screen.fill('#071A30')
        self.draw_grid()
        self._snake.walk()
        self._apple.draw()
        self.display_score()

        if self._snake.is_colliding_object(self._apple.x, self._apple.y):
            self._mixer.play_sound("ding.mp3")
            self._snake.increase_length()
            # Move the apple and continue doing it while it is on the snake's body
            self._apple.move()
            while self._snake.is_colliding_object_body(self._apple.x, self._apple.y):
                self._apple.move()

        # Starting at index 1 because the snake cannot collide its own head
        for i in range(1, self._snake.length):
            if self._snake.is_colliding_object(self._snake.x[i], self._snake.y[i]):
                self._mixer.play_sound("crash.mp3")
                self._pause = True

        if self._snake.is_colliding_wall_x() or self._snake.is_colliding_wall_y():
            self._mixer.play_sound("crash.mp3")
            self._pause = True

        pygame.display.flip()

    def draw_grid(self):
        """Draws a grid on the window"""
        for i in range(0, consts.WINDOW_WIDTH, consts.BLOCK_SIZE):
            pygame.draw.line(self._window.screen, '#0E2F56', (i, 0), (i, consts.WINDOW_HEIGHT))
        for i in range(0, consts.WINDOW_HEIGHT, consts.BLOCK_SIZE):
            pygame.draw.line(self._window.screen, '#0E2F56', (0, i), (consts.WINDOW_WIDTH, i))

    def display_score(self):
        """Displays the actual score on the screen"""
        text = Text(self._window.screen, consts.FONT_NAME, 50, "Score : {}".format(self._snake.length), '#6184E3')
        text.display_text((consts.WINDOW_WIDTH / 2 - text.width / 2, 15))

    def show_game_over(self):
        """Displays the Game Over interface and pauses the background music"""
        self._window.screen.fill('#071A30')

        game_over_text = Text(self._window.screen, consts.FONT_NAME, 50, "Game Over !", '#6184E3')
        game_over_text.display_text((consts.WINDOW_WIDTH / 2 - game_over_text.width / 2, 300))

        score_text = Text(self._window.screen, consts.FONT_NAME, 50, "Your score : {}".format(self._snake.length),
                          '#6184E3')
        score_text.display_text((consts.WINDOW_WIDTH / 2 - score_text.width / 2, 350))

        try_again_text = Text(self._window.screen, consts.FONT_NAME, 50, "Press Enter to return on Menu", '#6184E3')
        try_again_text.display_text((consts.WINDOW_WIDTH / 2 - try_again_text.width / 2, 400))

        pygame.display.flip()
        self._mixer.pause_background_music()
