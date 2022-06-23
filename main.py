import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))    # 800px width, 600px height

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# PLayer
playerImg = pygame.image.load('player.png')    # spaceship size is 64 x 64 px
playerX = 370
playerY = 480
playerX_dx = 0  # d = delta = change of x
                # the higher dx, the faster spaceship moves
# Enemy
enemyImg = pygame.image.load('enemy.png')    # spaceship size is 64 x 64 px
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_dx = 0

def player(x, y):
    screen.blit(playerImg, (x, y))  # draw img in coordinate (pX, pY)
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:
    pygame.display.update()
    
    # background color RGB
    screen.fill((0,0,0))    # screen should be drawn first, below all others
    
    # X+: moves to right; X-: moves to left
    # Y+: moves down; Y-: moves up
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed, check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_dx = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_dx = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_dx = 0
        
    if(playerX >= 740):
        playerX = 740
    elif(playerX <= 0):
        playerX = 0
    else:
        playerX += playerX_dx
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    