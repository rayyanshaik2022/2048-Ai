import pygame
from pygame import Color
from settings import *
from rounded_rect import *
from game import Game

class Gui:
    def __init__(self, game):
        pygame.init()
        pygame.font.init()
        pygame.freetype.init()
        
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.game = game
        
    def new(self):
        
        font = 'Fonts/ClearSans-Medium.ttf'
        self.title_font = pygame.freetype.Font(font, size=85)
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Controls update speed (FPS per second)
            self.events()
            self.update()
            self.draw()

    def close(self):
        pygame.quit()
        quit()

    def update(self):
        pass

    def draw(self):

        self.screen.fill(COLORS['background'])
        title_font = pygame.font.Font(self.font, 80)
        render = self.title_font.rect("2048 Game", fgcolor=Color['text'])
        
        self.screen.blit(render,(WIDTH//2 - render.get_width()//2,100))
        
        # Draw main frame
        main_frame_rect = ((WIDTH-450)//2,250,450,450)
        AAfilledRoundedRect(self.screen, main_frame_rect, COLORS['frame1'], 0.05)

        # Draw tiles
        for i in range(4):
            for j in range(4):
                o_rect = (main_frame_rect[0]+(SPACING*(j+1))+(TILESIZE*j), main_frame_rect[1]+(SPACING*(i+1))+(TILESIZE*i), TILESIZE, TILESIZE)
                AAfilledRoundedRect(self.screen, o_rect, COLORS['frame2'], 0.1)

                # Draw actual tiles
                if self.game.board[i][j] != 0:
                    rect = (main_frame_rect[0]+(SPACING*(j+1))+(TILESIZE*j), main_frame_rect[1]+(SPACING*(i+1))+(TILESIZE*i), TILESIZE, TILESIZE)
                    AAfilledRoundedRect(self.screen, rect, COLORS[self.game.board[i][j]], 0.1)

        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
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


# create the game object
g = Gui(Game())
g.new()
g.run()