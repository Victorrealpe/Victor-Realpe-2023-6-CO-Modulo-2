import pygame
from game.components import game

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []


    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    if bullet in self.player_bullets:  # Verificar si el elemento está en la lista
                        self.player_bullets.remove(bullet)
                    if enemy in game.enemy_manager.enemies:  # Verificar si el enemigo está en la lista
                        if enemy.resistance > 0: # SIMPLIFICAR TODA ESTA PARTE EN UN METODO EN ENEMYYYYYYYYYYYYYYYY ----------------------------------------------------------------------------
                            enemy.resistance -= 1
                        elif enemy.resistance == 0:
                            game.enemy_manager.enemies.remove(enemy)
                    break



    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self,bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 3:
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'player' and len(self.player_bullets) < 3:
            self.player_bullets.append(bullet)
    