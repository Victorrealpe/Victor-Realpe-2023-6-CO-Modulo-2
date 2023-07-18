from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
import random


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, bullet_manager):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies,bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1,2)
        if len(self.enemies) < 2:

            if enemy_type == 1:
                enemy = Enemy()
            else:
                enemy = Enemy_2()
            
            self.enemies.append(enemy)
