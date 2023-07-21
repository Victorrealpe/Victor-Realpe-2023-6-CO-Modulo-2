from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
import random

from game.components.enemies.enemy_3 import Enemy_3


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies,game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1,3)
        if len(self.enemies) < 1:

            if enemy_type == 1:
                enemy = Enemy()

            elif enemy_type ==2:
                enemy = Enemy_2()
                
            else:
                enemy = Enemy_3()
            
            self.enemies.append(enemy)

    def reset(self):
        self.enemies = []
