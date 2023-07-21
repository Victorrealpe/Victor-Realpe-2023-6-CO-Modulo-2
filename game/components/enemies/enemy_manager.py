import random
import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.enemy_3 import Enemy_3


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_count = 0
        self.last_enemy_time = 0  # Variable para realizar un seguimiento del tiempo de creación del último enemigo

    def update(self, game):
        self.enemy_increment()



        for enemy in self.enemies:
            enemy.update(self.enemies,game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self, count):
        for _ in range(count):

            enemy_type = random.randint(1,3)

            if enemy_type == 1:
                enemy = Enemy()

            elif enemy_type ==2:
                enemy = Enemy_2()
                    
            else:
                enemy = Enemy_3()
                
            self.enemies.append(enemy)

    def enemy_increment(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_enemy_time >= 5000:  # Intervalo de 5 segundos
            self.enemy_count += 1
            self.add_enemy(self.enemy_count)
            self.last_enemy_time = current_time

    def reset(self):
        self.enemies = []
        self.enemy_count = 0 #reiniciar cuenta
        self.last_enemy_time = 0  # Reiniciar el tiempo de creación del último enemigo
