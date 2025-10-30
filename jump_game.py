import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Jumping Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Player settings
player_size = 50
player_x = 100
player_y = HEIGHT - player_size
player_y_velocity = 0
gravity = 0.8
jump_strength = -15
on_ground = True

# Obstacle settings
obstacle_width = 40
obstacle_height = 60
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height
obstacle_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# Main game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Jump if space pressed and player is on the ground
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                player_y_velocity = jump_strength
                on_ground = False

    # Update player position
    player_y += player_y_velocity
    player_y_velocity += gravity

    if player_y >= HEIGHT - player_size:
        player_y = HEIGHT - player_size
        on_ground = True

    # Move obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH + random.randint(100, 300)
        score += 1

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        print(f"Game Over! Final Score: {score}")
        pygame.quit()
        sys.exit()

    # Draw player and obstacle
    pygame.draw.rect(screen, BLACK, player_rect)
    pygame.draw.rect(screen, RED, obstacle_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)
