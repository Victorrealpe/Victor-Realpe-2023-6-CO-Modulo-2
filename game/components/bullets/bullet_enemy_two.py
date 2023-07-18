from game.utils.constants import ENEMY_2, SCREEN_HEIGHT,  SCREEN_WIDTH, BULLET, BULLET_ENEMY
from game.components.bullets.bullet import Bullet
from pygame. sprite import Sprite
import pygame

class BulletEnemyTwo(Bullet):
    def __init__(self, spaceship):
        super().__init__(spaceship)
        self.stop_time = None
        self.is_stopped = False

    def update(self, bullets):
        current_time = pygame.time.get_ticks()

        if not self.is_stopped:
            self.rect.y += self.speed

        if self.rect.y > SCREEN_HEIGHT / 2 and not self.is_stopped:
            # La bala alcanzó la posición donde se detiene
            self.is_stopped = True
            self.stop_time = current_time + 2000  # Detener durante 2 segundos
            print("Se detiene")
            

        if self.is_stopped and current_time >= self.stop_time:
            # Han pasado los segundos de detención, la bala vuelve a moverse
            self.is_stopped = True
            self.rect.y += self.speed + 20
            print("Vuelve a moverse")

        if self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)
            self.is_stopped = False

