import pygame  # membutuhkan packages atau library pygame
import random

# Initialize the pygame
pygame.init()

# membuat tampilan windows pada prgoram
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Game Python DTS ProA-Academy Space Invades")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Membuat player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 380
playerX_change = 0

# Membuat lawan
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# membuat variabel untuk infinite loop sehingga tampilan game tetap menyala
running = True
while running:

    # Red, Green, Blue
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # membuat pengondisian untuk agar program
            running = False  # keluar ketika user klik sebuah button

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Menambahkan kondisi untuk membuat batas tampilan player ke window
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Menambahkan kondisi untuk membuat batas tampilan enemy ke window
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change += 0.3
        enemyY += enemyY_change
    elif enemyY >= 736:
        enemyX_change += 0.3
        enemyY += enemyY_change


    player(playerX, playerY)  # memanggil method player
    enemy(enemyX, enemyY)  # memanggil method enemy
    pygame.display.update()
