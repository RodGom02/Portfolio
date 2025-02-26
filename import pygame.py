import pygame

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

# Define colors
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)

#Load sprite
character_img = pygame.image.load("robot.jpg")  # Ensure this file exists in your project folder
character_img = pygame.transform.scale(character_img, (50, 50))

# Player setup
player_size = 40
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5
dash_time = 0
is_dashing = False
dash_speed = 12

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Delay to control frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not is_dashing:
        is_dashing = True
        dash_time = 10  # Dash lasts for 10 frames

    # Reduce dash time and reset speed
    if is_dashing:
        player_speed = dash_speed
        dash_time -= 1
        if dash_time <= 0:
            is_dashing = False
            player_speed = 5  # Reset to normal speed

    # Movement logic using WASD
    if keys[pygame.K_w]:  # Move up
        player_y -= player_speed
    if keys[pygame.K_s]:  # Move down
        player_y += player_speed
    if keys[pygame.K_a]:  # Move left
        player_x -= player_speed
    if keys[pygame.K_d]:  # Move right
        player_x += player_speed

    # Draw everything
    win.fill("white")
    win.blit(character_img, (player_x, player_y))
    pygame.display.update()

pygame.quit()
