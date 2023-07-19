import pygame
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.count import Count


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Spaceship()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu('Press Any Key To Start...', self.screen)
        self.running = False
        self.count = Count()
        self.death_count = self.count.death_count
        self.score = self.count.high_score
        self.high_score = self.count.high_score

    def execute(self):

        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score = 0
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()
        #FALTA RESET DE PLAYER------------------------------------------------------------
        #FALTA RESET DE PODERES------------------------------------------------------------
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.enemy_manager.update(self.bullet_manager)  
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.count.show_score(self) # aqui instanciar la nueva claseeeee counttttttttttt--------------
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    





    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT //2

        score = f'Score: {str(self.score)}'
        death = f'Death: {str(self.death_count)}' 
        hScore = f'High Score: {str(self.high_score)}'

        mensajes =[score,death,hScore]
        list_score = self.count.high_score_list
        #count_list = len(self.count.high_score_list)

        self.menu.reset_screen_color(self.screen)
    

        if self.death_count > 0 and self.playing == False:
            self.menu.update_message(mensajes, self.screen, self, list_score)

        else:
            self.menu.main_menu(self.screen,self)

        if not self.menu.high_score_list_on:
            icon = pygame.transform.scale (ICON, (80,120))
            self.screen.blit(icon, (half_screen_width - 50, half_screen_height -250))


        self.menu.draw(self.screen)
        self.menu.update(self)




