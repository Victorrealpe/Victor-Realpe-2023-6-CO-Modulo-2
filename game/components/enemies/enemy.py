
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
    SPEED_Y = 2
    MOV_X = {0:'left', 1:'right'}

    INITIAL_SHOOTING_TIME = 2000
    FINAL_SHOOTING_TIME = 4000

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
        self.shooting_time = random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)

    def update(self, ships, bullet_manager):
        self.rect.y += self.speed_y
        self.shoot(bullet_manager)


        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()


        if self.rect.y >= SCREEN_HEIGHT :
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def change_movement_x(self):
        self.index += 1 
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH) :
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10 ):
            self.movement_x = 'right'
            self.index = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)




