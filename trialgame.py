import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Rectangle starting position and size
rect_x, rect_y, rect_width, rect_height = 100, 100, 200, 150
speed = 5  # Speed of movement
direction_x = 1  # Movement direction (1 = right, -1 = left)
direction_y = 1  # Movement direction (1 = down, -1 = up)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rectangle position automatically
    rect_x += speed * direction_x
    rect_y += speed * direction_y

    # Reverse direction when hitting screen borders
    if rect_x + rect_width > screen.get_width() or rect_x < 0:
        direction_x *= -1
    if rect_y + rect_height > screen.get_height() or rect_y < 0:
        direction_y *= -1

    # Print the position to check if it is changing
    print(f"Rectangle Position: ({rect_x}, {rect_y})")

    # Fill the screen with a background color
    screen.fill((255, 255, 255))  # White background

    # Draw the moving rectangle
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Set FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
