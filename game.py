import random
from itertools import groupby
import pygame

class Game:

    def __init__(self):

        self.board = [[0]*4 for i in range(4)]
        self.spawn_cell(2) 
         
    def spawn_cell(self, n):
        open_slots = [(j, i) for i in range(4) for j in range(4) if self.board[i][j] == 0] # (x, y) format
        if len(open_slots) == 0:
            return
        elif len(open_slots) < n:
            n = len(open_slots)

        for i in range(n):
            slot = random.choice(open_slots)
            open_slots.remove(slot)

            if random.random() < 0.1: # 10% chance a 4 spawns
                value = 4
            else:
                value = 2
            
            # The [0,0] represents velocity
            self.board[slot[1]][slot[0]] = value #[value, [0,0]]
    
    def move_right(self):
        for i, row in enumerate(self.board):
            print(row)
            self.board[i] = self.shift_right(row)
            
    def move_left(self):
        for i, row in enumerate(self.board):
            print(row)
            self.board[i] = self.shift_left(row)
    
    def move_up(self):
        for c in range(4):
            col = [self.board[3][c],self.board[2][c],self.board[1][c],self.board[0][c]]
            new_col = self.shift_right(col)
            
            print(new_col)
            self.board[3][c], self.board[2][c], self.board[1][c], self.board[0][c] = new_col
    
    def move_down(self):
        for c in range(4):
            col = [self.board[3][c],self.board[2][c],self.board[1][c],self.board[0][c]]
            new_col = self.shift_left(col)
            
            print(new_col)
            self.board[3][c], self.board[2][c], self.board[1][c], self.board[0][c] = new_col
    
    def shift_right(self, row):
        row.reverse()
        merged = []
        for i in range(1,4):
            shift = 0
            if row[i] == row[i-1]:
                row[i-1] *= 2
                row[i] = 0
            while i-1-shift >= 0:
                if row[i-1-shift] == 0:
                    row[i-1-shift] = row[i-shift]
                    row[i-shift] = 0
                    shift += 1
                elif row[i-1-shift] == row[i-shift] and (i-1-shift) not in merged:
                    row[i-1-shift] *= 2
                    row[i-shift] = 0
                    shift += 1
                    merged.append(i-1-shift)
                else:
                    break
        row.reverse()
        return row
    
    def shift_left(self, row):
        merged = []
        for i in range(1,4):
            shift = 0
            if row[i] == row[i-1]:
                row[i-1] *= 2
                row[i] = 0
            while i-1-shift >= 0:
                if row[i-1-shift] == 0:
                    row[i-1-shift] = row[i-shift]
                    row[i-shift] = 0
                    shift += 1
                elif row[i-1-shift] == row[i-shift] and (i-1-shift) not in merged:
                    row[i-1-shift] *= 2
                    row[i-shift] = 0
                    shift += 1
                    merged.append(i-1-shift)
                else:
                    break
        return row
        
x = Game()
print(x.board)
print(x.shift_right([0,2,2,0]))
print(x.shift_left([2,8,0,4]))