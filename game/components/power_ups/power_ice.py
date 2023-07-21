from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  ICE, ICE_TYPE, DEFAULT_TYPE


class Ice(PowerUp):
    def __init__(self):
        super().__init__(ICE, ICE_TYPE)

    def use_power_ice(self, game, time_to_show):
        print("usa poder")

        for enemy in game.enemy_manager.enemies:
            enemy.stop_movement()
            enemy.stop_shoot()
                
        # PODER SE DETIENE CUANDO EL TIEMPO SE ACABA
        if time_to_show <=0:
            game.player_has_power_up = False
            game.player.power_up_type = DEFAULT_TYPE
            game.player.set_image()
            for enemy in game.enemy_manager.enemies:
                enemy.ready_movement()
                enemy.ready_shoot()