from game.utils.constants import ENEMY_2, SCREEN_HEIGHT,  SCREEN_WIDTH
from game.components.enemies.enemy import Enemy
import pygame
import random



class Enemy_2(Enemy):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60

    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    MOV_X = {0:'left', 1:'right'}

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.ENEMY_HEIGHT, SCREEN_WIDTH - self.ENEMY_WIDTH)
        self.speed_x = 8
        self.speed_y = 6
        self.move_x_for = random.randint(10, 50)

    
    def update(self, ships):
        self.rect.y += self.speed_y
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self,screen):
        super().draw(screen)

    def change_movement_x(self):
        super().change_movement_x()