import pygame

# Initialize the pygame
pygame.init()

# membuat tampilan windows pada prgoram
screen = pygame.display.set_mode((1000, 600))

#membuat variabel untuk infinite loop sehingga tampilan game tetap menyala
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #membuat pengondisian untuk agar program
            running = False             #keluar ketika user klik sebuah button
