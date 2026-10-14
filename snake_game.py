import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define Colors
BLACK = (15, 15, 15)
WHITE = (255, 255, 255)
GREEN = (46, 204, 113)
HEAD_COLOR = (39, 174, 96)
RED = (231, 76, 60)
GRAY = (52, 73, 94)

# Set Game Window Dimensions
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Setup display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Classic Snake Game - Python")

# Set frame rate (controls game speed)
clock = pygame.time.Clock()

# Fonts for UI
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

def display_score(score):
    value = score_font.render(f"Score: {score}", True, WHITE)
    window.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    # Initial Snake position (center of screen)
    x = WIDTH / 2
    y = HEIGHT / 2

    # Movement deltas
    x_change = CELL_SIZE
    y_change = 0

    # Snake body segments (list of coordinates)
    snake_body = []
    snake_length = 3

    # Generate initial food position on grid
    food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    while not game_over:

        while game_close:
            window.fill(GRAY)
            msg = font_style.render("Game Over! Press C-Play Again or Q-Quit", True, RED)
            window.blit(msg, [WIDTH / 6, HEIGHT / 3])
            display_score(snake_length - 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -CELL_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = CELL_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -CELL_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = CELL_SIZE
                    x_change = 0

        # Check boundary collisions (Wall death)
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(BLACK)

        # Draw Food
        pygame.draw.rect(window, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE], border_radius=4)

        # Update Snake Body
        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check self-collision (biting its own tail)
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw Snake
        for index, segment in enumerate(snake_body):
            color = HEAD_COLOR if index == len(snake_body) - 1 else GREEN
            pygame.draw.rect(window, color, [segment[0], segment[1], CELL_SIZE - 1, CELL_SIZE - 1], border_radius=3)

        display_score(snake_length - 3)
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            snake_length += 1

        # Control game speed (increases slightly as snake gets longer)
        speed = min(3 + (snake_length // 3), 25)
        clock.tick(speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()