import pygame
from game.utils.constants import BOMB_TYPE, EXPLOSION_1, EXPLOSION_10, EXPLOSION_11, EXPLOSION_12, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9, ICE_TYPE
from game.utils.constants import SHIELD_TYPE, SOUND_MUERTE, HEART_TYPE

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []


    def update(self, game):

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    sound_muerte = pygame.mixer.Sound(SOUND_MUERTE)
                    pygame.mixer.Sound.play(sound_muerte)

                    self.explosion(game,enemy)  
                    enemy.decrease_resistance(enemy,game)

                    self.player_bullets.remove(bullet)
                    for bullet in self.enemy_bullets:
                        self.enemy_bullets.remove(bullet)





        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                
                sound_muerte = pygame.mixer.Sound(SOUND_MUERTE)
                sound_muerte.play()
                if game.player.power_up_type != SHIELD_TYPE:
                    self.enemy_bullets.remove(bullet)
                    game.leader_board.update(game.score.count)
                    hearts_list = list(game.player.hearts)
                    vidas_disponibles = len(hearts_list)
                    last_heart = hearts_list[-1] 
                    hearts_list.remove(last_heart)
                    game.player.vidas -= 1
                    game.player.hearts = pygame.sprite.Group(hearts_list)

                    if vidas_disponibles == 1:
                        game.death_count.update()
                        game.playing = False
                        pygame.time.delay(1000)
                        break
                if game.player.power_up_type == SHIELD_TYPE:
                    self.enemy_bullets.remove(bullet)

                if game.player.power_up_type == HEART_TYPE:
                    for Heart in game.player.hearts:
                        game.player.hearts.add(Heart)
                        break

                if game.player.power_up_type == BOMB_TYPE:
                    game.player.power_up = False

                #if game.player.power_up_type == ICE_TYPE:
                 #   game.player.power_up = False
            


                    



    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.player_bullets:
            bullet.draw(screen)

    def explosion(self, game, enemigo):
        x = enemigo.rect.x + (enemigo.rect.width - EXPLOSION_1.get_width()) // 2
        y = enemigo.rect.y + (enemigo.rect.height - EXPLOSION_1.get_height()) // 2

        imagenes_explosion = [EXPLOSION_1, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9, EXPLOSION_10, EXPLOSION_11, EXPLOSION_12]

        for i, imagen_explosion in enumerate(imagenes_explosion):
            game.screen.blit(imagen_explosion, (x, y-10))

            pygame.display.flip()

    def add_bullet(self,bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 3:
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'player' and len(self.player_bullets) < 3:
            self.player_bullets.append(bullet)

    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []
    