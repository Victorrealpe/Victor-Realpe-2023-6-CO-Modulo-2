import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE

class Count():

    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.high_score_list = []
        self.index_list = 0
        self.death_count = 0





    def show_score(self,game):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score:{game.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        game.screen.blit(text, text_rect)

        if game.score > game.high_score:
            game.high_score = game.score


    def add_high_score(self, game):
        if self.index_list < 10 and game.score >= game.high_score:
            self.high_score_list.append(game.high_score)
            self.index_list +=1
        self.show_high_score()

    def add_death(self,game):
        game.death_count += 1

        
    def show_high_score(self):
        print(self.high_score_list)