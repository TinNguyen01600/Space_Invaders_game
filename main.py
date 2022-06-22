import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))    # 800px width, 600px height

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# PLayer
playerImg = pygame.image.load('ss1.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
    pygame.display.update()
    # background color RGB
    screen.fill((0,0,0))    # screen should be drawn first, below all others
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player()
    