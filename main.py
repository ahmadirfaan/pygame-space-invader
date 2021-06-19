import pygame  # membutuhkan packages atau library pygame

# Initialize the pygame
pygame.init()

# membuat tampilan windows pada prgoram
screen = pygame.display.set_mode((1000, 600))
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Title and Icon
pygame.display.set_caption("Game Python DTS ProA-Academy Space Invades")

# membuat variabel untuk infinite loop sehingga tampilan game tetap menyala
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # membuat pengondisian untuk agar program
            running = False  # keluar ketika user klik sebuah button

    # RGB - Red Green and Blue untuk background gambar screen-nya
    screen.fill((0, 0, 0))
    pygame.display.update()
