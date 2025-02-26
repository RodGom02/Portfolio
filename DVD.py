import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver - Perfect Corner Glitch")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Load and scale DVD logo
dvd_logo = pygame.image.load("dvd_logo.png")  # Ensure you have a DVD logo image
logo_width, logo_height = 100, 50
dvd_logo = pygame.transform.scale(dvd_logo, (logo_width, logo_height))

# Initial position and speed
x, y = random.randint(0, WIDTH - logo_width), random.randint(0, HEIGHT - logo_height)
dx, dy = 4, 4  # Movement speed

# Game loop
running = True
clock = pygame.time.Clock()
corner_hit = False  # Track if it hit a perfect corner

while running:
    screen.fill(BLACK)

    # Move the logo
    x += dx
    y += dy

    # Check for wall collisions
    hit_left = x <= 0
    hit_right = x >= WIDTH - logo_width
    hit_top = y <= 0
    hit_bottom = y >= HEIGHT - logo_height

    if hit_left or hit_right:
        dx *= -1  # Reverse X direction

    if hit_top or hit_bottom:
        dy *= -1  # Reverse Y direction

    # Check for perfect corner hit
    if (hit_left or hit_right) and (hit_top or hit_bottom):
        corner_hit = True

    # If it hits a corner, make the screen go crazy
    if corner_hit:
        for _ in range(10):  # Flash 10 times
            screen.fill(random.choice(COLORS))
            pygame.display.flip()
            pygame.time.delay(50)
        corner_hit = False  # Reset after glitch effect

    # Draw the DVD logo
    screen.blit(dvd_logo, (x, y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)  # Limit FPS

pygame.quit()
