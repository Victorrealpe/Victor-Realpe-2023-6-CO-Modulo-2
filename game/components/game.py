import pygame
from game.components.counter import Counter
from game.components.leader_board import LeaderBoard
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.bullets.bullet_manager import BulletManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.menu import Menu
from game.utils.constants import  SOUND_BASE, HEART_TYPE,BOMB_TYPE, SOUND_BOMB, ICE_TYPE, SOUND_ICE
from game.components.count import Count
from game.components.heart import Heart 


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
        self.power_up_manager = PowerUpManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.score = Counter()
        self.death_count = Counter()
        self.leader_board = LeaderBoard()
        self.show_leader_board = False
        

    def execute(self):
        self.data_load()  #-----------------------------------------------------------------------------------------------------
        self.running = True
        while self.running:
            if not self.playing and not self.show_leader_board:
                self.show_menu()
            elif self.show_leader_board:
                
                self.show_higest_scores()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset()
        self.player.add_vida()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.data_save()#-----------------------------------------------------------------------------
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.enemy_manager.update(self)  
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        #self.data_save()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen, 'Score', (1000, 50))
        self.draw_power_up_time()
        self.player.hearts.draw(self.screen)
        pygame.display.update()
        #pygame.display.flip()

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


        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        icon = self.image = pygame.transform.scale(ICON, (80, 120))

        self.menu.reset(self.screen)

        if self.death_count.count == 0 and self.show_leader_board == False:

            self.menu.show_button_menu = True

            self.screen.blit(icon, (SCREEN_WIDTH - 180 , half_screen_height))
            self.screen.blit(icon, (100 , half_screen_height))
            self.menu.draw(self,self.screen, 'Press any key to start ...')
            

        elif self.death_count.count > 0:
            self.menu.show_button_menu = False
            self.menu.show_buttons_muerte = True
         
            
            self.screen.blit(icon, (half_screen_width - 50, 100))
            self.menu.draw(self,self.screen, 'Game over. Press any key to restart', half_screen_width, 250)
            self.menu.draw(self,self.screen, f'Your score: {self.score.count}', half_screen_width, 300)
            self.menu.draw(self,self.screen, f'Highest score: {self.leader_board.get_highest_score()}', half_screen_width, 350)
            self.menu.draw(self,self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 400)
            self.menu.draw(self,self.screen, f'Press "h" to see the list of highest scores', half_screen_width, 500)
            


        self.menu.update(self)
        
    def reset(self):
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.score.reset()
        self.player.reset()

    def show_higest_scores(self):
        
        half_screen_width = SCREEN_WIDTH // 2
        height = 100
        position = 1
    
        self.menu.reset(self.screen)
        
        self.menu.draw(self,self.screen, 'Highest Scores', half_screen_width, 50)
        for score in self.leader_board.highest_scores:
            self.menu.draw(self,self.screen, f'{position}: {score}', half_screen_width, height )
            height += 50
            position += 1
        self.menu.draw(self,self.screen, f'Press "m" to return to the previous menu', half_screen_width, height + 50)
        self.menu.draw(self,self.screen, f'Press "s" to start a new game', half_screen_width, height + 100)
    
        self.menu.update(self)


    def draw_power_up_time(self):

            if self.player.has_power_up:
                time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)

                if time_to_show >=0:
                    font = pygame.font.Font(FONT_STYLE, 30)
                    text = font.render(f'{str(self.player.power_up_type).capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                    text_rect = text.get_rect()
                    self.screen.blit(text,(540, 60))

                elif self.player.has_power_up and self.player.power_up_type == BOMB_TYPE:
                    font = pygame.font.Font(FONT_STYLE, 30)
                    text = font.render(f'{str(self.player.power_up_type).capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                    text_rect = text.get_rect()
                    self.screen.blit(text,(540, 60))

                elif self.player.has_power_up and self.player.power_up_type == ICE_TYPE:
                    font = pygame.font.Font(FONT_STYLE, 30)
                    text = font.render(f'{str(self.player.power_up_type).capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                    text_rect = text.get_rect()
                    self.screen.blit(text,(540, 60))

                else:
                    self.player_has_power_up = False
                    self.player.power_up_type = DEFAULT_TYPE
                    self.player.set_image()

            if self.player.has_power_up and self.player.power_up_type == HEART_TYPE:
                total_vidas = len(self.player.hearts)
                max_vidas = 10
                if total_vidas < max_vidas:
                    self.player.vidas += 1
                    x = 40 + self.player.vidas * 40
                    y = 20
                    heart_mas = Heart(x, y)
                    self.player.hearts.add(heart_mas) 
                    self.player.has_power_up = False

            if self.player.has_power_up and self.player.power_up_type == BOMB_TYPE:

                sound_bomb= pygame.mixer.Sound(SOUND_BOMB)
                pygame.mixer.Sound.play(sound_bomb)
                for enemy in self.enemy_manager.enemies:
                    
                    self.bullet_manager.explosion(self,enemy)
                    self.enemy_manager.enemies.remove(enemy)
                    self.score.add_points(enemy)
                       #self.score += 100
                    conteo_enemis=len(self.enemy_manager.enemies)
                    print(conteo_enemis)
                    

                    if conteo_enemis == 0:
                        self.player.has_power_up = False
                        self.enemy_manager.reset()




            if self.player.has_power_up and self.player.power_up_type == ICE_TYPE:
                sound_ice = pygame.mixer.Sound(SOUND_ICE)
                pygame.mixer.Sound.play(sound_ice)

                for enemy in self.enemy_manager.enemies:
                    enemy.stop_movement()
                    enemy.stop_shoot()
                
                
                if time_to_show <=0:
                    self.player_has_power_up = False
                    self.player.power_up_type = DEFAULT_TYPE
                    self.player.set_image()
                    for enemy in self.enemy_manager.enemies:
                        enemy.ready_movement()



                #self.player.has_power_up = False
            
            else:
                for enemy in self.enemy_manager.enemies:
                    enemy.ready_shoot()



    def data_save(self):
        # Convertir la lista de enteros a una cadena con números separados por comas
        datos_a_guardar = ','.join(str(numero) for numero in self.leader_board.highest_scores)

        # Abrir el archivo en modo escritura y guardar los datos
        with open('datos.txt', 'w') as archivo:
            archivo.write(datos_a_guardar)
    


    def data_load(self):
        with open('datos.txt', 'r') as archivo:
            informacion = archivo.read()
            informacion_int = [int(elemento) for elemento in informacion.split(',')]
            self.leader_board.highest_scores = informacion_int





