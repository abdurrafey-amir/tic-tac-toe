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
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

font = pygame.font.Font('freesansbold.ttf', 32)

# variables
turn = 0



board = [
    ['-', '-', '-'], 
    ['-', '-', '-'], 
    ['-', '-', '-']
    ]

def draw_board():
    for row in range(3):
        for col in range(3):
            rect = pygame.FRect((col * 200) + 100, (row * 200) , 200, 200)
            pygame.draw.rect(screen, white, rect, 5)
            text = font.render(board[row][col], True, white)
            screen.blit(text, (rect.x + 100, rect.y + 100))

def draw_x(row, col):
    board[row][col] = 'X'

def draw_o(row, col):
    board[row][col] = 'O'


rects = []

# main loop
running = True
while running:
    clock.tick(60)

    screen.fill(grey)
    draw_board()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # print(x, y)
            if x < 100 or x > 700:
                pass
            else: 
                row = y // 200
                col = x // 300
                # rect = pygame.Rect((col * 200) + 100, row * 200, 200, 200)
                # rects.append(rect)
                try:
                    if board[row][col] == '-':
                        if turn == 0:
                            draw_x(row, col)
                            turn = 1
                        else:
                            draw_o(row, col)
                            turn = 0
                except IndexError:
                    pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = [
                    ['-', '-', '-'], 
                    ['-', '-', '-'], 
                    ['-', '-', '-']
                    ]
                turn = 0
                rects = []
                running = True
        if event.type == pygame.MOUSEMOTION:
            # highlight boxes
            x, y = pygame.mouse.get_pos()
            if x < 100 or x > 700:
                pass
            else:
                row = y // 200
                col = x // 300
                rect = pygame.Rect((col * 200) + 100, row * 200, 200, 200)
                rects.append(rect)
                if len(rects) > 1:
                    rects.pop(0)

    for rect in rects:
        if turn == 0:
            pygame.draw.rect(screen, blue, rect, 5)
        else:
            pygame.draw.rect(screen, green, rect, 5)
    
    for row in board:
        # print(row)
        if (row[0] == row[1] == row[2]) and row[0] != '-':
            running = False
            print('You win!')
            break

    pygame.display.flip()

pygame.quit()