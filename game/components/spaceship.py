import pygame

from pygame.sprite import Sprite

from game.components.bullets.bullet_player import BulletPlayer
from game.utils.constants import  SCREEN_HEIGHT, SPACESHIP, SCREEN_WIDTH, SOUND_BULLET_PLAYER

class Spaceship(Sprite):
    # declaramos constantes, estas siempre estaran escritas en mallusculas 
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEINGH = 60
    HALL_SCREEM_HEIGHT = SCREEN_HEIGHT // 2
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500 
    SPACESHIP_SPEED = 10
    SHOOT_DELAY = 200

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP,(self.SPACESHIP_WIDTH,self.SPACESHIP_HEINGH))
        self.rect = self.image.get_rect() 
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.last_shot_time = 0
        self.type = 'player'
        
        self.last_shot_time = 0


    def update(self, user_input, bullet_manager):

      if user_input[pygame.K_LEFT]:
        self.move_left()
        self.move_diag(user_input)

      

      elif user_input[pygame.K_RIGHT]:
        self.move_right()
        self.move_diag(user_input)


      elif user_input[pygame.K_UP]:
        self.move_up()


      elif user_input[pygame.K_DOWN]:
        self.move_down()


      if user_input[pygame.K_SPACE]:
          current_time = pygame.time.get_ticks()
          if current_time - self.last_shot_time >= self.SHOOT_DELAY:
              self.shoot(bullet_manager)
              self.last_shot_time = current_time


    #movimiento de jugador
    def move_left(self):
        self.rect.x -= self.SPACESHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH

    def move_right(self): 

        self.rect.x += self.SPACESHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > self.HALL_SCREEM_HEIGHT:
            self.rect.y -= self.SPACESHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEINGH:
            self.rect.y += self.SPACESHIP_SPEED

    def move_diag(self, user_input):
        
        if user_input[pygame.K_UP]:
           self.move_up()
        elif user_input[pygame.K_DOWN]:
          self.move_down()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        bullet = BulletPlayer(self)
        bullet_manager.add_bullet(bullet)

        #SONIDO
        sound_player= pygame.mixer.Sound(SOUND_BULLET_PLAYER)
        sound_player.set_volume(0.1) #CONTROL DE VOLUMEN
        pygame.mixer.Sound.play(sound_player)

    
       


    