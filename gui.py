import pygame
import pygame.freetype
from pygame import Color
from settings import *
from rounded_rect import *
from game import Game
import time
from montecarlo import MonteCarlo

from copy import deepcopy

AUTO = True
delay = 0.001

class Gui:
    def __init__(self, game, delay, simulations, theme):
        
        self.delay = delay
        self.simulations = simulations
        pygame.init()
        pygame.font.init()
        pygame.freetype.init()
        
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.game = game
        
        self.theme = THEMES[theme.lower()]
        
    def new(self):
        
        self.font = 'Fonts/ClearSans-Medium.ttf'
        #self.title_font = pygame.freetype.Font(self.font, size=85)
        self.start_time = 0
        
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Controls update speed (FPS per second)
            self.events()
            self.update()
            self.draw()

    def close(self):
        pygame.display.quit()
        pygame.quit()
        self.playing = False

    def update(self):
        
        if AUTO and time.time() - self.start_time > self.delay:
            predictor = MonteCarlo(deepcopy(self.game.board), self.simulations)
            self.game.call_move(predictor.solve())
            
            self.start_time = time.time()
            

    def draw(self):

        if not self.playing:
            return
        
        self.screen.fill(self.theme['background'])
        #title_font = pygame.font.Font(self.font, 80)
        
        '''Fix rendering text'''
        #render_ = self.title_font.render("2048 Game", fgcolor=Color['text'])
        
        #self.screen.blit(render,(WIDTH//2 - render.get_width()//2,100))
        
        # Draw main frame
        main_frame_rect = ((WIDTH-450)//2,120,450,450)
        AAfilledRoundedRect(self.screen, main_frame_rect, self.theme['frame1'], 0.05)

        # Draw tiles
        for i in range(4):
            for j in range(4):
                o_rect = (main_frame_rect[0]+(SPACING*(j+1))+(TILESIZE*j), main_frame_rect[1]+(SPACING*(i+1))+(TILESIZE*i), TILESIZE, TILESIZE)
                AAfilledRoundedRect(self.screen, o_rect, self.theme['frame2'], 0.1)

                # Draw actual tiles
                if self.game.board[i][j] != 0:
                    rect = (main_frame_rect[0]+(SPACING*(j+1))+(TILESIZE*j), main_frame_rect[1]+(SPACING*(i+1))+(TILESIZE*i), TILESIZE, TILESIZE)
                    AAfilledRoundedRect(self.screen, rect, self.theme[self.game.board[i][j]], 0.1)

        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.game.move_right()
                    self.game.spawn_cell(1)
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.game.move_left()
                    self.game.spawn_cell(1)
                elif event.key in [pygame.K_w, pygame.K_UP]:
                    self.game.move_up()
                    self.game.spawn_cell(1)
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.game.move_down()
                    self.game.spawn_cell(1)
            
            if event.type == pygame.QUIT:
                self.close()


