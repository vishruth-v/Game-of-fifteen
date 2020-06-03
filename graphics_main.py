import pygame
from pygame.locals import *
from Board import Board

screen = None
newfont = None

def main():
    b = Board()
    pygame.init()
    pygame.font.init()
    board = [[' 1', ' 2', ' 3', ' 4'],
                [' 5', ' 6', ' 7', ' 8'],
                [' 9', '10', '11', '12'],
                ['13', '14', '15', '__']]

    newfont = pygame.font.SysFont('arial', 50)
    screen = pygame.display.set_mode((470,470))
    bgnd = (255,255,255)
    WIN_W = 470
    WIN_H = 470
    WIN = (WIN_W, WIN_H)

    pygame.display.set_caption("Game of Fifteen")
    screen.fill(bgnd)
    pygame.display.flip()

    j = 0
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #if(j == 0):
        drawboxes([1,1], board,screen,newfont)
        pygame.display.flip()
        j += 1

def init(screen,newfont):
    pygame.init()
    pygame.font.init()
    newfont = pygame.font.SysFont('arial', 50)
    screen = pygame.display.set_mode((470,470))
    bgnd = (255,255,255)
    pygame.display.set_caption("Game of Fifteen")
    screen.fill(bgnd)
    pygame.display.flip()

    
def numbers(board, num,x,y):
    #for i in board:
        #for j in board:
    number = newfont.render(num, True, (255,255,255))
    screen.blit(number,[x,y])

def drawboxes(e_loc, board,screen,newfont):
    e_row = e_loc[0]*120
    e_col = e_loc[1]*120
    cnt = 0
    for i in range(0,480,120):
        for j in range(0,480,120):
            if j == e_row and i == e_col:
                pygame.draw.rect(screen, (255,255,255), (j,i,110,110))
            else:
                cnt += 1
                pygame.draw.rect(screen, (255,0,0), (j,i,110,110))
                no = newfont.render(str(cnt), True, (255,255,255))
                screen.blit(no, [(2*j +110)//2 - 50, (2*i+110)//2 - 50])
    pygame.display.flip()



if __name__ == '__main__':
    main()