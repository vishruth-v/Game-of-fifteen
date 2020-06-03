from copy import deepcopy
from os import system
from random import randint, seed
from queue import Queue
import pygame

MAX_ROW = 4
MAX_COL = 4
SHUFFLE_MAGNITUDE = 10

class Board:
    def __init__(self):
        self.goal = [[' 1', ' 2', ' 3', ' 4'],
                     [' 5', ' 6', ' 7', ' 8'],
                     [' 9', '10', '11', '12'],
                     ['13', '14', '15', '__']]

        self.board = deepcopy(self.goal)
        
        self.e_loc = [MAX_ROW - 1, MAX_COL - 1]

        self.moves = {0:self.move_up, 1:self.move_right, 2:self.move_down, 3:self.move_left}
    
    def __repr__ (self):
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                print(self.board[i][j], end = ' ')
            print()
        
        return '' #__repr__ must return a string type
    
    def refresh(self):
        system('cls')
        print('Game of Fifteen!')
        print(self)
        print('Press Esc to exit')

        if self.goal == self.board:
            print("\nCONGRATS YOU'VE WON!\n")
            return False
        
        return True

    def shuffle(self):
        seed()
        for _ in range(SHUFFLE_MAGNITUDE):
            m = randint(0,3) 
            self.moves[m](self.board, self.e_loc)
        
        for _ in range(MAX_ROW):
            self.move_down(self.board, self.e_loc)
        for _ in range(MAX_COL):
            self.move_right(self.board, self.e_loc)
        

    def move(self, board, e_loc, x, y):
        #check legality of move
        if (e_loc[0] + x > MAX_ROW -1 or e_loc[1] + y > MAX_COL - 1
        or e_loc[0] + x < 0 or e_loc[1] + y < 0):
            return board, e_loc
 
        #swap the two locations
        board[e_loc[0]][e_loc[1]], board[e_loc[0] + x][e_loc[1] + y] = \
        board[e_loc[0] + x][e_loc[1] + y] , board[e_loc[0]][e_loc[1]]

        #update the e_loc
        e_loc[0] += x
        e_loc[1] += y

        return board, e_loc

    def move_up(self, board, e_loc):
        return self.move(board, e_loc, -1, 0)
    
    def move_down(self, board, e_loc):
        return self.move(board, e_loc, 1, 0)
    
    def move_right(self, board, e_loc):
        return self.move(board, e_loc, 0, 1)

    def move_left(self, board, e_loc):
        return self.move(board, e_loc, 0, -1)
    
    '''def solve(self):
        ''''''Solves the board using BFS algorithm''''''
        checked = []
        fringe = Queue()
    '''
    def solve(self):
        self.board = deepcopy(self.goal) 

    def drawboxes(self, e_loc, board,screen,newfont):
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
        