import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    # FIXME Constantes pour longueur, largeur de l'écran et deuxième paramètre de randit (width/SIZE-1 et length/SIZE-1)
    def move(self):
        # Window's width / SIZE - 1 -> 1000 / 40 - 1 = 25
        self.x = random.randint(1, 24) * SIZE
        # Window's length / SIZE - 1 -> 800 / 40 - 1 = 20
        self.y = random.randint(1, 19) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        # Load the image
        self.block = pygame.image.load("resources/block.jpg").convert()
        # Initialize the coordinates with arrays -> [40, 40, 40, 40] for length == 4
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def draw(self):
        """Draw a snake with x and y coordinates"""
        for i in range(self.length):
            # Draw the image at a position
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        # Window's dimensions
        self.surface = pygame.display.set_mode((1000, 800))
        # Mixer's initialization (for sounds and music)
        pygame.mixer.init()
        # Start playing the background music
        self.play_background_music()
        # Window's background color
        self.surface.fill((110, 110, 5))
        # Initialize a snake
        self.snake = Snake(self.surface, 1)
        # Draw the snake
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    # FIXME changer la logique de collision
    def is_collision(self, x1, y1, x2, y2):
        """Check if the snake is eating an apple"""
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        """The snake moves forwards by 1 each time this function is called
        Called continuously in run()"""
        # Put the background
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # If the snake's head is touching the apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            # Play the sound corresponding to eating an apple
            self.play_sound("ding")
            # Increasing snake's length and continue moving
            self.snake.increase_length()
            self.apple.move()

        # If the snake's head is touching its body -> Game over
        # Starting at index 1 because the snake cannot collide its ows head
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                # Play the sound corresponding to colliding its own body
                self.play_sound("crash")
                raise Exception("Collision Occurred")

    def show_game_over(self):
        # Clear the surface
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render("Game Over ! Your score is {}".format(self.snake.length), True, (200, 200, 200))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play the game again press Enter.", True, (220, 220, 220))
        self.surface.blit(line2, (200, 350))
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
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

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
            time.sleep(0.3)

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render("Score : {}".format(self.snake.length), True, (200, 200, 200))
        self.surface.blit(score, (800, 10))

    def reset(self):
        # Recreate a new snake and a new apple
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def play_sound(self, sound):
        sound = pygame.mixer.Sound("resources/{}.mp3".format(sound))
        pygame.mixer.Sound.play(sound)

    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        # Put the background image on the window at 0,0 position
        self.surface.blit(bg, (0, 0))


if __name__ == '__main__':
    game = Game()
    game.run()
