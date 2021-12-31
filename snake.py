import pygame
import random

import consts


class Snake:
    """The object that the player is going to control"""
    def __init__(self, parent_screen):
        """
        - Start with a length of 1 and the speed defined in consts.py
        - Load the snake images for the head and for the body
        - Initialize it's first coordinates x, y at the middle of the screen
        - Start with the up direction
        :param parent_screen: The parent window
        """
        self._length = 1
        self._speed = consts.SNAKE_SPEED
        self._parent_screen = parent_screen
        self._head_block = pygame.image.load("resources/snowball-head.png").convert_alpha()
        self._body_block = pygame.image.load("resources/snowball.png").convert_alpha()
        self._x = [consts.WIDTH_COEFFICIENT / 2 * consts.BLOCK_SIZE]
        self._y = [consts.HEIGHT_COEFFICIENT / 2 * consts.BLOCK_SIZE]
        self._direction = consts.UP

    def draw(self):
        """Draw all snake's blocks at corresponding positions"""
        # Snake's head
        self._parent_screen.blit(self._head_block, (self._x[0], self._y[0]))
        # Snake's body
        for i in range(1, self._length):
            self._parent_screen.blit(self._body_block, (self._x[i], self._y[i]))
        pygame.display.flip()

    def move_up(self):
        """Change the snake's direction and orient its head to to up"""
        if self._direction == consts.DOWN:
            self._head_block = pygame.transform.rotate(self._head_block, 180)
        if self._direction == consts.LEFT:
            self._head_block = pygame.transform.rotate(self._head_block, 270)
        if self._direction == consts.RIGHT:
            self._head_block = pygame.transform.rotate(self._head_block, 90)

        self._direction = consts.UP

    def move_down(self):
        """Change the snake's direction and orient its head to to down"""
        if self._direction == consts.UP:
            self._head_block = pygame.transform.rotate(self._head_block, 180)
        if self._direction == consts.LEFT:
            self._head_block = pygame.transform.rotate(self._head_block, 90)
        if self._direction == consts.RIGHT:
            self._head_block = pygame.transform.rotate(self._head_block, 270)

        self._direction = consts.DOWN

    def move_left(self):
        """Change the snake's direction and orient its head to left"""
        if self._direction == consts.UP:
            self._head_block = pygame.transform.rotate(self._head_block, 90)
        if self._direction == consts.DOWN:
            self._head_block = pygame.transform.rotate(self._head_block, 270)
        if self._direction == consts.RIGHT:
            self._head_block = pygame.transform.rotate(self._head_block, 180)

        self._direction = consts.LEFT

    def move_right(self):
        """Change the snake's direction and orient its head to to right"""
        if self._direction == consts.UP:
            self._head_block = pygame.transform.rotate(self._head_block, 270)
        if self._direction == consts.DOWN:
            self._head_block = pygame.transform.rotate(self._head_block, 90)
        if self._direction == consts.LEFT:
            self._head_block = pygame.transform.rotate(self._head_block, 180)

        self._direction = consts.RIGHT

    def walk(self):
        """
        Increase the snake's length and change its block's position
        Each block takes the position of the previous one
        Redraw it with the new coordinates
        """
        for i in range(self._length - 1, 0, -1):
            self._x[i] = self._x[i - 1]
            self._y[i] = self._y[i - 1]

        if self._direction == consts.UP:
            self._y[0] -= consts.BLOCK_SIZE
        if self._direction == consts.DOWN:
            self._y[0] += consts.BLOCK_SIZE
        if self._direction == consts.LEFT:
            self._x[0] -= consts.BLOCK_SIZE
        if self._direction == consts.RIGHT:
            self._x[0] += consts.BLOCK_SIZE

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
        if self._x[0] > consts.WINDOW_WIDTH - consts.BLOCK_SIZE or self._x[0] < 0:
            return True
        return False

    def is_colliding_wall_y(self):
        """
        :return: True if the snake's head's y coordinate overstep the window's dimensions
        """
        if self._y[0] > consts.WINDOW_HEIGHT - consts.BLOCK_SIZE or self._y[0] < 0:
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
