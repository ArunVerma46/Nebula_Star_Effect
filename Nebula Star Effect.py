import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nebula Star Effect")

# Colors for the nebula
COLORS = [
    (100, 50, 150),   # Purple
    (50, 150, 150),   # Cyan
    (200, 50, 100),   # Magenta
    (255, 150, 50),   # Orange
    (25, 25, 50)      # Dark Blue
]

# Star class
class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(1, 3)
        self.color = random.choice(COLORS)
        self.speed = random.uniform(0.1, 0.5)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.size, self.size))

# Particle class for the nebula
class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(5, 20)
        self.color = random.choice(COLORS)
        self.speed = random.uniform(0.5, 2.0)
        self.alpha = random.randint(10, 80)  # Transparency

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        # Create a surface with alpha for transparency
        s = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, self.color + (self.alpha,), (self.size, self.size), self.size)
        surface.blit(s, (self.x - self.size, self.y - self.size))

# Create lists of stars and particles
stars = [Star() for _ in range(200)]
particles = [Particle() for _ in range(50)]

running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with a dark color
    screen.fill((5, 5, 20))

    # Draw and move stars
    for star in stars:
        star.move()
        star.draw(screen)

    # Draw and move nebula particles
    for particle in particles:
        particle.move()
        particle.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()
