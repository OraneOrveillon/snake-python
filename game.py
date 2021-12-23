import pygame
from pygame.locals import *
import time

from snake import Snake
from apple import Apple
from mixer import Mixer
import constants


class Game:
    """Deal with the functional aspects of the game"""

    def __init__(self):
        """
        - Create a mixer and start playing background music
        - Initialize pygame library
        - Create the window with its dimensions
        - Create and draw an snake and an apple
        """
        self._mixer = Mixer()
        self._mixer.play_background_music()
        pygame.init()
        self._window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_LENGTH))
        self._snake = Snake(self._window)
        self._snake.draw()
        self._apple = Apple(self._window)
        self._apple.draw()

    def run(self):
        """Keep the game running until the game over state or when the window is closed"""
        # Keep the window running until it is closed
        # Moves the blocks when a direction key is pressed
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Closed with escape key
                    if event.key == K_ESCAPE:
                        running = False
                    # Restart the game
                    if event.key == K_RETURN:
                        # Restart the music
                        self._mixer.play_background_music()
                        # Un pause the game
                        pause = False

                    # Move the snake following the direction's key
                    if not pause:
                        if event.key == K_UP:
                            self._snake.move_up()

                        if event.key == K_DOWN:
                            self._snake.move_down()

                        if event.key == K_LEFT:
                            self._snake.move_left()

                        if event.key == K_RIGHT:
                            self._snake.move_right()

                # Closed with the cross
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception:
                self.show_game_over()
                pause = True
                self.reset()

            # Basically the snake's speed
            time.sleep(self._snake.speed)

    def play(self):
        """
        The snake moves forwards by 1 and the background is cleared each time this function is called
        Called continuously in run()
        Check for snake's collisions :
            - length++ and move the apple if colliding the apple
            - game over if colliding its body or a wall"""
        self.render_background()
        self._snake.walk()
        self._apple.draw()
        self.display_score()
        pygame.display.flip()

        # If the snake's head is touching the apple
        if self._snake.is_colliding_object(self._apple.x, self._apple.y):
            # Play the sound corresponding to eating an apple
            self._mixer.play_sound("ding")
            # Increasing snake's length and continue moving
            self._snake.increase_length()
            self._apple.move()

        # If the snake's head is touching its body -> Game over
        # Starting at index 1 because the snake cannot collide its ows head
        for i in range(1, self._snake.length):
            if self._snake.is_colliding_object(self._snake.x[i], self._snake.y[i]):
                # Play the sound corresponding to colliding its own body
                self._mixer.play_sound("crash")
                raise Exception("Collision Occurred")

        # If the snake's head is touching a wall -> Game over
        if self._snake.is_colliding_wall_x() or self._snake.is_colliding_wall_y():
            self._mixer.play_sound("crash")
            raise Exception("Collision Occurred")

    def render_background(self):
        """Regenerate the background at 0,0 position"""
        background = pygame.image.load("resources/background.jpg")
        self._window.blit(background, (0, 0))
        # Single color background (temporary)
        self._window.fill((7, 26, 48))

    def display_score(self):
        """Display the actual score on the screen"""
        font = pygame.font.SysFont('arial', 30)
        score = font.render("Score : {}".format(self._snake.length), True, (200, 200, 200))
        self._window.blit(score, (800, 10))

    def show_game_over(self):
        """Display the Game Over interface"""
        # Clear the surface
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render("Game Over ! Your score is {}".format(self._snake.length), True, (200, 200, 200))
        self._window.blit(line1, (200, 300))
        line2 = font.render("To play the game again press Enter.", True, (220, 220, 220))
        self._window.blit(line2, (200, 350))
        # Update the window
        pygame.display.flip()
        # Stop playing the background music
        self._mixer.pause_background_music()

    def reset(self):
        """Restart the game"""
        # Recreate a new snake and a new apple
        self._snake = Snake(self._window)
        self._apple = Apple(self._window)
