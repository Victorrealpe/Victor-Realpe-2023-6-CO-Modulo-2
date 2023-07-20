from game.utils.constants import ENEMY_3, SCREEN_HEIGHT,  SCREEN_WIDTH, BULLET, BULLET_ENEMY
from game.components.bullets.bullet import Bullet
from pygame. sprite import Sprite
import pygame

class BulletEnemyThree(Bullet):
    SPEED = 40
    def __init__(self, spaceship):
        super().__init__(spaceship)


