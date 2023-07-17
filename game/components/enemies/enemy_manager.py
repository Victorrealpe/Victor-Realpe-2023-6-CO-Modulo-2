from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
import random


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            enemy_2 = Enemy_2()
            enemies = [enemy,enemy_2]
            enemigo = enemies[random.randint(0,1)]
            
            self.enemies.append(enemigo)
