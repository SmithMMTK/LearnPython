import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Initialize Snake
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = "RIGHT"

# Initialize Food
food_position = (random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
                 random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE)

# Score
score = 0

def message(text, color):
    font = pygame.font.Font(None, 36)
    text = font.render(text, True, color)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    
def game_over():
    message("Game Over. Your Score: " + str(score), WHITE)
    pygame.display.flip()
    pygame.time.wait(2000)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move Snake
    if snake_direction == "UP":
        head = (snake[0][0], snake[0][1] - SNAKE_SIZE)
    if snake_direction == "DOWN":
        head = (snake[0][0], snake[0][1] + SNAKE_SIZE)
    if snake_direction == "LEFT":
        head = (snake[0][0] - SNAKE_SIZE, snake[0][1])
    if snake_direction == "RIGHT":
        head = (snake[0][0] + SNAKE_SIZE, snake[0][1])

    snake.insert(0, head)

    # Check if Snake eats Food
    if snake[0] == food_position:
        score += 1
        food_position = (random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
                         random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE)
    else:
        snake.pop()

    # Check if Snake hits the boundary
    if (
        snake[0][0] >= WIDTH
        or snake[0][0] < 0
        or snake[0][1] >= HEIGHT
        or snake[0][1] < 0
    ):
        running = False

    # Check if Snake hits itself
    for segment in snake[1:]:
        if snake[0] == segment:
            running = False

    screen.fill((0, 0, 0))
    
    # Draw Food
    pygame.draw.rect(screen, GREEN, (food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw Snake
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.update()

    clock.tick(FPS)

game_over()
pygame.quit()
