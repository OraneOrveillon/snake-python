import pygame
from pygame.locals import *
import time


from snake import Snake
from apple import Apple
import constants


class Game:
    def __init__(self):
        pygame.init()
        # Window's dimensions
        self._surface = pygame.display.set_mode((1000, 800))
        # Mixer's initialization (for sounds and music)
        pygame.mixer.init()
        # Start playing the background music
        self.play_background_music()
        # Window's background color
        self._surface.fill((110, 110, 5))
        # Initialize a snake
        self._snake = Snake(self._surface)
        # Draw the snake
        self._snake.draw()
        self._apple = Apple(self._surface)
        self._apple.draw()

    # TODO changer la logique de collision
    @staticmethod
    def is_collision(x1, y1, x2, y2):
        """Check if the snake is eating an apple"""
        if x2 <= x1 < x2 + constants.SIZE:
            if y2 <= y1 < y2 + constants.SIZE:
                return True
        return False

    def play(self):
        """The snake moves forwards by 1 each time this function is called
        Called continuously in run()"""
        # Put the background
        self.render_background()
        self._snake.walk()
        self._apple.draw()
        self.display_score()
        pygame.display.flip()

        # If the snake's head is touching the apple
        if self.is_collision(self._snake.x[0], self._snake.y[0], self._apple.x, self._apple.y):
            # Play the sound corresponding to eating an apple
            self.play_sound("ding")
            # Increasing snake's length and continue moving
            self._snake.increase_length()
            self._apple.move()

        # If the snake's head is touching its body -> Game over
        # Starting at index 1 because the snake cannot collide its ows head
        for i in range(1, self._snake.length):
            if self.is_collision(self._snake.x[0], self._snake.y[0], self._snake.x[i], self._snake.y[i]):
                # Play the sound corresponding to colliding its own body
                self.play_sound("crash")
                raise Exception("Collision Occurred")

    def show_game_over(self):
        # Clear the surface
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render("Game Over ! Your score is {}".format(self._snake.length), True, (200, 200, 200))
        self._surface.blit(line1, (200, 300))
        line2 = font.render("To play the game again press Enter.", True, (220, 220, 220))
        self._surface.blit(line2, (200, 350))
        # Update the window
        pygame.display.flip()
        # Stop playing the background music
        pygame.mixer.music.pause()

    def run(self):
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
                        pygame.mixer.music.unpause()
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

            # Snake's speed
            time.sleep(self._snake.speed)

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render("Score : {}".format(self._snake.length), True, (200, 200, 200))
        self._surface.blit(score, (800, 10))

    def reset(self):
        # Recreate a new snake and a new apple
        self._snake = Snake(self._surface)
        self._apple = Apple(self._surface)

    @staticmethod
    def play_sound(sound):
        sound = pygame.mixer.Sound("resources/{}.mp3".format(sound))
        pygame.mixer.Sound.play(sound)

    @staticmethod
    def play_background_music():
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        # Put the background image on the window at 0,0 position
        self._surface.blit(bg, (0, 0))



