
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]

# Colors for tetrominos
COLORS = [
    (0, 255, 255),  # Cyan (I)
    (255, 255, 0),  # Yellow (O)
    (128, 0, 128),  # Purple (T)
    (255, 165, 0),  # Orange (L)
    (0, 0, 255),    # Blue (J)
    (0, 255, 0),    # Green (S)
    (255, 0, 0),    # Red (Z)
]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

# Function to draw a tetromino
def draw_tetromino(tetromino, x, y):
    shape = SHAPES[tetromino["shape"]]
    color = COLORS[tetromino["color"]]
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        (x + col) * GRID_SIZE, (y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE
                    ),
                )

# Initialize game variables
board = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Get random tetromino shape
current_tetromino = {"shape": random.randint(0, len(SHAPES) - 1), "color": 0, "x": 4, "y": 0}

#current_tetromino = {"shape": 0, "color": 0, "x": 4, "y": 0}
score = 0

# Game loop
clock = pygame.time.Clock()
running = True

# Define a variable to store the time elapsed since the last tetromino movement
time_since_last_move = 0

# Set the desired falling speed (lower values mean faster falling)
FALL_SPEED = 0.5  # You can adjust this value

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if current_tetromino["x"] > 0:
            current_tetromino["x"] -= 1
    if keys[pygame.K_RIGHT]:
        if current_tetromino["x"] < GRID_WIDTH - len(SHAPES[current_tetromino["shape"]][0]):
            current_tetromino["x"] += 1
    if keys[pygame.K_DOWN]:
        if current_tetromino["y"] < GRID_HEIGHT - len(SHAPES[current_tetromino["shape"]]):
            current_tetromino["y"] += 1


    
    # Calculate the time elapsed since the last frame
    delta_time = clock.tick(30) / 1000.0  # Convert milliseconds to seconds

    # Update the timer
    time_since_last_move += delta_time

    # Check if it's time to move the tetromino down
    if time_since_last_move >= FALL_SPEED:
        # Reset the timer
        time_since_last_move = 0

        # Check for collisions before moving down
        if current_tetromino["y"] < GRID_HEIGHT - len(SHAPES[current_tetromino["shape"]]):
            current_tetromino["y"] += 1

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw the grid
    draw_grid()

    # Draw the current tetromino
    draw_tetromino(current_tetromino, current_tetromino["x"], current_tetromino["y"])

    # Update the display
    pygame.display.flip()

    # Control the game's speed
    clock.tick(20)

