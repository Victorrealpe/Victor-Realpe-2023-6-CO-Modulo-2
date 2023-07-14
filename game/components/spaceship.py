import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship:
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGT = 60
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500 
    SPACESHIP_SPEED = 10
    



    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.last_shot_time = 0


    def update(self, user_input):

      if user_input[pygame.K_LEFT]:
        self.move_left()
        if user_input[pygame.K_UP]:
           self.move_up()
        if user_input[pygame.K_DOWN]:
          self.move_down()
      

      elif user_input[pygame.K_RIGHT]:
        self.move_right()
        if user_input[pygame.K_UP]:
           self.move_up()
        if user_input[pygame.K_DOWN]:
          self.move_down()


      elif user_input[pygame.K_UP]:
        self.move_up()


      elif user_input[pygame.K_DOWN]:
        self.move_down()


    def move_left(self):
        self.rect.x -= self.SPACESHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SPACESHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH - self.SPACESHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
      if self.rect.y > SCREEN_HEIGHT // 2:
        self.rect.y -= self.SPACESHIP_SPEED

    def move_down(self):
      if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGT:  
        self.rect.y += self.SPACESHIP_SPEED


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))