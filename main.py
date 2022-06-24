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

# Background load image
background = pygame.image.load('background.png')

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
enemyX_dx = 0.15
enemyY_dy = 35  # moving up/down 35px

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480   # bulletY = playerY
bulletY_dy = 0.3        # speed of the bullet
bullet_state = "ready"  # "ready": cant be seen on screen
                        # "fire": bullet is moving

def player(x, y):
    screen.blit(playerImg, (x, y))  # draw img in coordinate (pX, pY)
def enemy(x, y):
    screen.blit(enemyImg, (x, y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+18, y+10))

# Game Loop
running = True
while running:
    pygame.display.update()
    
    # background color RGB
    screen.fill((0,0,0))    # screen should be drawn first, below all others
    
    # Background print
    screen.blit(background, (0, 0))
    
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
            if event.key == pygame.K_SPACE:
                bullet_state = "fire"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_dx = 0
      
    # Checking for boundaries of spaceship
    playerX += playerX_dx  
    if(playerX >= 740):
        playerX = 740
    elif(playerX <= 0):
        playerX = 0
        
    # Enemy movement
    enemyX += enemyX_dx
    if(enemyX >= 740 or enemyX <= 0):
        enemyX_dx *= -1
        enemyY += enemyY_dy
        
    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_dy   # moving upwards
        
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    