import pygame
import random

import constants


class Snake:
    """The object that the player is going to control"""
    def __init__(self, parent_screen):
        """
        - Start with a length of 1 and the speed defined in constants.py
        - Load the snake images for the head and for the body
        - Initialize it's first coordinates x, y at the middle of the screen
        - Start at a random direction
        :param parent_screen: The parent window
        """
        self._length = 1
        self._speed = constants.SNAKE_SPEED
        self._parent_screen = parent_screen
        self._head_block = pygame.image.load("resources/blue-ball.png").convert_alpha()
        self._body_block = pygame.image.load("resources/snowball.png").convert_alpha()
        self._x = [constants.WIDTH_COEFFICIENT / 2 * constants.BLOCK_SIZE]
        self._y = [constants.LENGTH_COEFFICIENT / 2 * constants.BLOCK_SIZE]
        self._direction = constants.DIRECTIONS[random.randint(0, 3)]

    def draw(self):
        """Draw all snake's blocks at corresponding positions"""
        # Snake's head
        self._parent_screen.blit(self._head_block, (self._x[0], self._y[0]))
        # Snake's body
        for i in range(1, self._length):
            self._parent_screen.blit(self._body_block, (self._x[i], self._y[i]))
        pygame.display.flip()

    def move_up(self):
        """Change the snake's direction to up"""
        self._direction = constants.DIRECTIONS[0]

    def move_down(self):
        """Change the snake's direction to down"""
        self._direction = constants.DIRECTIONS[1]

    def move_left(self):
        """Change the snake's direction to left"""
        self._direction = constants.DIRECTIONS[2]

    def move_right(self):
        """Change the snake's direction to right"""
        self._direction = constants.DIRECTIONS[3]

    def walk(self):
        """
        Increase the snake's length and change its block's position
        Each block takes the position of the previous one
        Redraw it with the new coordinates
        """
        for i in range(self._length - 1, 0, -1):
            self._x[i] = self._x[i - 1]
            self._y[i] = self._y[i - 1]

        if self._direction == constants.DIRECTIONS[0]:
            self._y[0] -= constants.BLOCK_SIZE
        if self._direction == constants.DIRECTIONS[1]:
            self._y[0] += constants.BLOCK_SIZE
        if self._direction == constants.DIRECTIONS[2]:
            self._x[0] -= constants.BLOCK_SIZE
        if self._direction == constants.DIRECTIONS[3]:
            self._x[0] += constants.BLOCK_SIZE

        self.draw()

    def is_colliding_object(self, x, y):
        """
        :param x: Object's x coordinate
        :param y: Object's y coordinate
        :return: True if the snake's head's coordinates are the same has object's coordinates
        """
        if x <= self._x[0] == x and self._y[0] == y:
            return True
        return False

    def is_colliding_object_body(self, x, y):
        """
        Works the same as is_colliding_object but for the whole snake's body
        :param x: Object's x coordinate
        :param y: Object's y coordinate
        :return: True if the snake's body's coordinates are the same has object's coordinates
        """
        for i in range(self._length):
            if self._x[i] == x and self._y[i] == y:
                return True
        return False

    def is_colliding_wall_x(self):
        """
        :return: True if the snake's head's x coordinate overstep the window's dimensions
        """
        if self._x[0] > constants.WINDOW_WIDTH - constants.BLOCK_SIZE or self._x[0] < 0:
            return True
        return False

    def is_colliding_wall_y(self):
        """
        :return: True if the snake's head's y coordinate overstep the window's dimensions
        """
        if self._y[0] > constants.WINDOW_LENGTH - constants.BLOCK_SIZE or self._y[0] < 0:
            return True
        return False

    def increase_length(self):
        """Increase the snake's length by 1"""
        self._length += 1
        self._x.append(-1)
        self._y.append(-1)

    # ---------- GETTERS / SETTERS SPACE ---------- #
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def length(self):
        return self._length

    @property
    def speed(self):
        return self._speed
