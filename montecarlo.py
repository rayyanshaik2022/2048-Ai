from game import Game
import random
import numpy as np
from copy import deepcopy

MOVES = ['up','down','left','right']
SIMULATIONS = 30 # simulations per move

class MonteCarlo:
    
    def __init__(self, board, simulations):
        
        self.simulations = simulations
        self.original_board = board
        self.move_scores = [0,0,0,0] # scores by move
    
    def solve(self):
        
        for i, move in enumerate(MOVES):
            for c in range(self.simulations):
                simulation = Game()
                simulation.board = [row[:] for row in self.original_board] #deepcopy(self.original_board)
                simulation.call_move(move)
                
                while not simulation.is_loss():
                    simulation.call_move(random.choice(MOVES))
                
                self.move_scores[i] += simulation.board_sum()

        index = np.argmax(self.move_scores)
        best_move = MOVES[index]
        
        return best_move