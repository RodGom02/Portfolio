import pygame

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = [5, 5]
PADDLE_SPEED = 7
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Pong")

# Paddle & Ball settings
paddle_width, paddle_height = 15, 100
ball_size = 20

# Player Paddle
player_x, player_y = 50, (HEIGHT // 2) - (paddle_height // 2)
# AI Paddle
ai_x, ai_y = WIDTH - 50 - paddle_width, (HEIGHT // 2) - (paddle_height // 2)
# Ball
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Ball movement
ball_dx, ball_dy = BALL_SPEED

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_y < HEIGHT - paddle_height:
        player_y += PADDLE_SPEED

    # AI Paddle Movement (follows ball)
    if ai_y + paddle_height // 2 < ball_y:
        ai_y += PADDLE_SPEED
    elif ai_y + paddle_height // 2 > ball_y:
        ai_y -= PADDLE_SPEED

    # Ball Movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball Collision with Walls
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_dy *= -1  # Reverse ball direction

    # Ball Collision with Paddles
    if (
        player_x < ball_x < player_x + paddle_width and
        player_y < ball_y < player_y + paddle_height
    ) or (
        ai_x < ball_x + ball_size < ai_x + paddle_width and
        ai_y < ball_y < ai_y + paddle_height
    ):
        ball_dx *= -1  # Reverse direction on paddle hit

    # Reset Ball if it goes out of bounds
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1  # Reset direction

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (player_x, player_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (ai_x, ai_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))

    # Update screen
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
