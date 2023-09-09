import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
PACMAN_SIZE = 30
DOT_SIZE = 10
WHITE = (255, 255, 255)
PACMAN_COLOR = (255, 255, 0)
DOT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Lite")

# Initialize Pac-Man position and velocity
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Create a list of dots
dots = [(100, 100), (200, 200), (300, 300), (400, 400), (500, 500)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle Pac-Man movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    elif keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    elif keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    elif keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Check for collision with dots
    eaten_dots = []
    for dot in dots:
        dot_rect = pygame.Rect(dot[0], dot[1], DOT_SIZE, DOT_SIZE)
        pacman_rect = pygame.Rect(pacman_x, pacman_y, PACMAN_SIZE, PACMAN_SIZE)

        if pacman_rect.colliderect(dot_rect):
            eaten_dots.append(dot)

    for dot in eaten_dots:
        dots.remove(dot)

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw Pac-Man
    pacman = pygame.draw.circle(screen, PACMAN_COLOR, (pacman_x, pacman_y), PACMAN_SIZE // 2, 0)

    # Draw dots
    for dot in dots:
        pygame.draw.circle(screen, DOT_COLOR, dot, DOT_SIZE // 2, 0)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
