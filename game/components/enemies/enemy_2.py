from game.utils.constants import ENEMY_2, SCREEN_HEIGHT,  SCREEN_WIDTH
from game.components.enemies.enemy import Enemy
from game.components.bullets.bullet_enemy_two import BulletEnemyTwo
import pygame
import random



class Enemy_2(Enemy):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60

    Y_POS = 20
    SPEED_X = 2
    SPEED_Y = 1
    MOV_X = {0:'left', 1:'right'}


    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.ENEMY_HEIGHT, SCREEN_WIDTH - self.ENEMY_WIDTH)
        self.speed_x = 10
        self.speed_y = 1
        self.move_x_for = random.randint(10, 50)
        self.resistance = 0
        self.index_enemy = 1


    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time and self.index_enemy == 1:
            bullet = BulletEnemyTwo(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)
        
