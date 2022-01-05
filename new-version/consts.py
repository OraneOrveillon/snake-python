"""FIle containing all necessary constants for the project"""

"""The size of one snake's block and an apple --> a square of side x"""
BLOCK_SIZE = 48
"""
Coefficients used for the window's dimensions
HAS TO BE AN EVEN NUMBER
"""
WIDTH_COEFFICIENT = 20
HEIGHT_COEFFICIENT = 18
"""Window's dimensions, always are a multiple of BLOCK_SIZE thanks to the coefficients above"""
WINDOW_WIDTH = WIDTH_COEFFICIENT * BLOCK_SIZE
WINDOW_HEIGHT = HEIGHT_COEFFICIENT * BLOCK_SIZE
"""The snake's move speed"""
SNAKE_SPEED = 0.075
"""The 4 directions taken by the snake"""
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
"""General font for texts"""
FONT_NAME = 'impact'
"""General parameters for buttons"""
BUTTON_COLOR = 'white'
BUTTON_FONT_COLOR = 'black'
SELECTED_BUTTON_COLOR = '#484848'
SELECTED_BUTTON_FONT_COLOR = 'white'
"""Parameters for Menu's buttons (proportional to the rest window's dimensions)"""
MENU_BUTTON_WIDTH = BLOCK_SIZE * 8
MENU_BUTTON_HEIGHT = BLOCK_SIZE * 2
MENU_BUTTON1_Y = BLOCK_SIZE * 5
MENU_BUTTON2_Y = BLOCK_SIZE * 9
MENU_BUTTON3_Y = BLOCK_SIZE * 13
MENU_BUTTON_FONT_SIZE = BLOCK_SIZE
"""Font size for Menu's title (proportional to the rest window's dimensions)"""
MENU_TITLE_FONT_SIZE = BLOCK_SIZE * 3


