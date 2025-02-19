
import pygame
import random
from pygame. sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet


class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60


    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 4
    MOV_X = {0:'left', 1:'right'}

    INITIAL_SHOOTING_TIME = 1000
    FINAL_SHOOTING_TIME = 2000

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_1, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.ENEMY_HEIGHT, SCREEN_WIDTH - self.ENEMY_WIDTH)
        self.rect.y - self.Y_POS
        self.speed_x = self. SPEED_X
        self.speed_y = self. SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.type = 'enemy'
        self.index_enemy = 0
        self.shooting_time = random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)
        self.resistance = 4
        self.points = 3 #puntos a sumar a score
        self.control_dis = True

    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)


        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()


        if self.rect.y >= SCREEN_HEIGHT :
            ships.remove(self)
            for heart in game.player.hearts:
                hearts_list = list(game.player.hearts)
                last_heart = hearts_list[-1] 
                if heart == last_heart:
                    game.player.hearts.remove(heart)
                    break

        vidas_disponibles = len(game.player.hearts) + 1
        if vidas_disponibles <= 1:
                game.death_count.update()
                game.playing = False
                pygame.time.delay(200)

        self.control_shoot(game)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


    # METODO CAMBIO DE DIRECCION EN X
    def change_movement_x(self):
        self.index += 1 
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH) :
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10 ):
            self.movement_x = 'right'
            self.index = 0


    #METODO DE DISPARO
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time and self.index_enemy == 0:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)


    #METODO DE CONTROL DE MOVIMIENTO
    def stop_movement(self):
        self.speed_y = 0
        self.speed_x = 0
        self.rect.y = self.rect.y
        self.rect.x = self.rect.x

    def ready_movement(self):
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        

    #METODOS PARA EL CONTROL DE LAS BALAS
    def stop_shoot(self):
        self.control_dis = False

    def control_shoot(self,game):
        bullet = self.shoot(game.bullet_manager)
        if bullet is not None and self.control_dis == True:
            game.bullet_manager.add_bullet(bullet)

        if self.control_dis == False:
            game.bullet_manager.enemy_bullets = []

    def ready_shoot(self):
        self.control_dis = True


    #METODO DE NIVEL DE RESISTENCIA DEL ENEMIGO A LAS BALAS
    def decrease_resistance(self,enemy,game):
        if enemy.resistance > 0:
            enemy.resistance -= 1
        elif enemy.resistance == 0:
            game.enemy_manager.enemies.remove(enemy)
            game.score.add_points(enemy) # SE SUMAN PUNTOS DE ENEMIGO AL SCORE




