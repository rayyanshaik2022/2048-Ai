import random
from itertools import groupby
import pygame

class Game:

    def __init__(self):

        self.board = [[0]*4 for i in range(4)]
        self.spawn_cell(2)
        
        self.score = 0
        self.turns = 0
         
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
    
    def call_move(self, move):
        
        if move == 'up':
            self.move_up()
        elif move == 'down':
            self.move_down()
        elif move == 'left':
            self.move_left()
        elif move == 'right':
            self.move_right()
        
        self.spawn_cell(1)
    
    def board_sum(self):
        
        total = 0
        for row in self.board:
            total += sum(row)
        return total
    
    def move_right(self):
        self.turns += 1
        for i, row in enumerate(self.board):

            self.board[i], points = self.shift_right(row)
            self.score += points
            
    def move_left(self):
        self.turns += 1
        for i, row in enumerate(self.board):
            self.board[i], points = self.shift_left(row)
            self.score += points
    
    def move_up(self):
        self.turns += 1
        for c in range(4):
            col = [self.board[3][c],self.board[2][c],self.board[1][c],self.board[0][c]]
            new_col, points = self.shift_right(col)
            
            self.board[3][c], self.board[2][c], self.board[1][c], self.board[0][c] = new_col
            self.score += points
    
    def move_down(self):
        self.turns += 1
        for c in range(4):
            col = [self.board[3][c],self.board[2][c],self.board[1][c],self.board[0][c]]
            new_col, points = self.shift_left(col)

            self.board[3][c], self.board[2][c], self.board[1][c], self.board[0][c] = new_col
            self.score += points
    
    def is_loss(self) -> bool:
        
        # First check if all spots are empty
        for i in range(len(self.board)):
            for c in range(len(self.board[i])):
                if self.board[i][c] == 0:
                    return False
        
        # Check if horizontals match
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1]:
                return False
            elif self.board[i][3] == self.board[i][2]:
                return False
            elif self.board[i][1] in (self.board[i][0], self.board[i][2]):
                return False
            elif self.board[i][2] in (self.board[i][1], self.board[i][3]):
                return False
        
        # Check if verticals match
        for i in range(len(self.board)):
            if self.board[0][i] == self.board[1][i]:
                return False
            elif self.board[3][i] == self.board[2][i]:
                return False
            elif self.board[1][i] in (self.board[0][i], self.board[2][i]):
                return False
            elif self.board[2][i] in (self.board[1][i], self.board[3][i]):
                return False
        
        return True
    
    def shift_right(self, row):
        row.reverse()
        merged = []
        point_add = 0
        for i in range(1,4):
            shift = 0
            if row[i] == row[i-1]:
                row[i-1] *= 2
                point_add += row[i-1]
                row[i] = 0
            while i-1-shift >= 0:
                if row[i-1-shift] == 0:
                    row[i-1-shift] = row[i-shift]
                    row[i-shift] = 0
                    shift += 1
                elif row[i-1-shift] == row[i-shift] and (i-1-shift) not in merged:
                    row[i-1-shift] *= 2
                    point_add += row[i-1-shift]
                    row[i-shift] = 0
                    shift += 1
                    merged.append(i-1-shift)
                else:
                    break
        row.reverse()
        return row, point_add
    
    def shift_left(self, row):
        merged = []
        point_add = 0
        for i in range(1,4):
            shift = 0
            if row[i] == row[i-1]:
                row[i-1] *= 2
                point_add += row[i-1]
                row[i] = 0
            while i-1-shift >= 0:
                if row[i-1-shift] == 0:
                    row[i-1-shift] = row[i-shift]
                    row[i-shift] = 0
                    shift += 1
                elif row[i-1-shift] == row[i-shift] and (i-1-shift) not in merged:
                    row[i-1-shift] *= 2
                    point_add += row[i-1-shift]
                    row[i-shift] = 0
                    shift += 1
                    merged.append(i-1-shift)
                else:
                    break
        return row, point_add
        