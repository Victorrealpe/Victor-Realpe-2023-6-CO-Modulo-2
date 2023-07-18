from game.utils.constants import ENEMY_2, SCREEN_HEIGHT,  SCREEN_WIDTH, BULLET, BULLET_ENEMY
from game.components.bullets.bullet import Bullet
from pygame. sprite import Sprite

import pygame
import random



class BulletPlayer(Bullet, Sprite):

    def __init__(self, spaceship):
        super().__init__(spaceship)


    def update(self, bullets):
        self.rect.y -= self.speed

        if self.rect.y < 0:
            bullets.remove(self)
