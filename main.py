import pygame  # membutuhkan packages atau library pygame

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


def player():
    screen.blit(playerImg, (playerX, playerY))


# membuat variabel untuk infinite loop sehingga tampilan game tetap menyala
running = True
while running:

    #Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # membuat pengondisian untuk agar program
            running = False  # keluar ketika user klik sebuah button

    # RGB - Red Green and Blue untuk background gambar screen-nya
    player() #memanggil method player
    pygame.display.update()
