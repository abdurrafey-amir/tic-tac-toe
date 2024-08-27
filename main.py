import pygame


WIDTH = 800
HEIGHT = 600

# general setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

# colors
grey = pygame.Color('grey12')
white = (255, 255, 255)

# variables
turn = 0



board = [
    ['', '', ''], 
    ['', '', ''], 
    ['', '', '']
    ]

def draw_board():
    for row in range(3):
        for col in range(3):
            rect = pygame.FRect((col * 200) + 100, (row * 200) , 200, 200)
            pygame.draw.rect(screen, white, rect, 5)

def draw_x(row, col):
    pass

def draw_o(row, col):
    pass

# main loop
running = True
while running:
    clock.tick(60)


    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(grey)
    draw_board()

    pygame.display.flip()

pygame.quit()