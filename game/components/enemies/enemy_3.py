from game.utils.constants import ENEMY_3, SCREEN_HEIGHT,  SCREEN_WIDTH
from game.components.enemies.enemy import Enemy
from game.components.bullets.bullet_enemy_three import BulletEnemyThree
import pygame
import random



class Enemy_3(Enemy):
    ENEMY_WIDTH = 60
    ENEMY_HEIGHT = 80

    Y_POS = 20
    SPEED_X = 0
    SPEED_Y = 8
    MOV_X = {0:'left', 1:'right'}


    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_3, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.ENEMY_HEIGHT, SCREEN_WIDTH - self.ENEMY_WIDTH)
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.resistance = 0
        self.index_enemy = 1
        self.points = 10


    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time and self.index_enemy == 1:
            bullet = BulletEnemyThree(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME - 500, self.FINAL_SHOOTING_TIME - 1000)

    def update(self, ships, game):
        self.rect.y += 20
        self.shoot(game.bullet_manager)

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

    def change_movement_x(self):
        pass