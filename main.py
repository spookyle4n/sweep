import random
import pygame

# Define game constants
WIDTH = 600
HEIGHT = 600
ROWS = 10
COLUMNS = 10
MINE_COUNT = 10
CELL_SIZE = 50
PADDING = 5
FONT_SIZE = 30
MINE = -1

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Minesweeper')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define colors
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Generate game board
board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
mines = []
for i in range(MINE_COUNT):
    while True:
        x = random.randint(0, ROWS-1)
        y = random.randint(0, COLUMNS-1)
        if (x, y) not in mines:
            mines.append((x, y))
            board[x][y] = MINE
            break
for i in range(ROWS):
    for j in range(COLUMNS):
        if board[i][j] != MINE:
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if i+dx >= 0 and i+dx < ROWS and j+dy >= 0 and j+dy < COLUMNS and board[i+dx][j+dy] == MINE:
                        count += 1
            board[i][j] = count

# Define cell class
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * (CELL_SIZE+PADDING), y * (CELL_SIZE+PADDING), CELL_SIZE, CELL_SIZE)
        self.is_revealed = False
        self.is_flagged = False

    def draw(self):
        if not self.is_revealed:
            pygame.draw.rect(screen, GRAY, self.rect)
            if self.is_flagged:
                flag_rect = pygame.Rect(self.x * (CELL_SIZE+PADDING), self.y * (CELL_SIZE+PADDING), CELL_SIZE, CELL_SIZE)
                pygame.draw.line(screen, RED, flag_rect.midtop, flag_rect.midbottom, 5)
                pygame.draw.line(screen, RED, flag_rect.midtop, flag_rect.midbottom, 5)
                pygame.draw.line(screen, RED, flag_rect.midtop, flag_rect.midbottom, 5)
        else:
            if board[self.x][self.y] == MINE:
                pygame.draw.rect(screen, RED, self.rect)
                pygame.draw.circle(screen, BLACK, self.rect.center, CELL_SIZE//4)
            else:
                pygame.draw.rect(screen, WHITE, self.rect)
                if board[self.x][self.y] > 0:
                    text = font.render(str(board[self.x][self.y]), True, BLUE)
                    text_rect = text.get_rect(center=self.rect.center)
                    screen.blit(text, text_rect)

    def reveal(self):
        if not self.is_revealed and not self.is_flagged:
            self.is_revealed = True
            if board[self.x][self.y
