import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Dice Roller")

# Load dice images and resize
dice_images = [pygame.image.load(f'Dice0{i}.png') for i in range(1, 7)]
dice_images = [pygame.transform.scale(img, (150, 150)) for img in dice_images]

# Set initial dice face
current_face = random.randint(0, 5)

# Font for instruction text
font = pygame.font.SysFont("Arial", 24)

# Variables for animation
rolling = False
roll_start = 0
ROLL_DURATION = 1.0  # seconds

# Clock for FPS control
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill((30, 30, 30))  # Background color

    # Show dice image
    screen.blit(dice_images[current_face], (125, 100))

    # Show instructions
    text = font.render("Press SPACE to roll", True, (220, 220, 220))
    screen.blit(text, (110, 30))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start dice roll animation
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rolling = True
            roll_start = time.time()

    # Animate roll
    if rolling:
        if time.time() - roll_start < ROLL_DURATION:
            current_face = random.randint(0, 5)
        else:
            rolling = False
            current_face = random.randint(0, 5)

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # 30 frames per second

# Quit Pygame
pygame.quit()
