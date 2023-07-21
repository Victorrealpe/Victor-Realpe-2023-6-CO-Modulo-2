import random
import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.power_heart import Heart
from game.components.power_ups.power_bomb import Bomb
from game.components.power_ups.power_ice import Ice

from game.utils.constants import SPACESHIP_SHIELD,SHIELD_TYPE,HEART_TYPE,SPACESHIP,BOMB_TYPE, ICE_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up(game)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up.rect):
                
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)

                if game.player.power_up_type == SHIELD_TYPE:
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)

                elif game.player.power_up_type == HEART_TYPE:
                    nave = SPACESHIP
                    game.player.set_image((40, 60), nave)
                    self.power_ups.remove(power_up)

                elif game.player.power_up_type == BOMB_TYPE:
                    nave = SPACESHIP
                    game.player.set_image((40, 60), nave)
                    self.power_ups.remove(power_up)

                elif game.player.power_up_type == ICE_TYPE:
                    nave = SPACESHIP
                    game.player.set_image((40, 60), nave)
                    self.power_ups.remove(power_up)

                else:
                    game.player.set_image((65, 75))
                    self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self, game):

        power_up = Shield()
        power_heart = Heart()
        power_bomb = Bomb()
        power_ice = Ice()
        
        power_selec = [power_up,power_heart,power_bomb,power_ice]
        power_random = power_selec[random.randint(0,3)]
        self.when_appears += random.randint(5000, 10000)



        self.power_ups.append(power_ice)