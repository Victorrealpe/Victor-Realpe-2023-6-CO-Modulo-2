import sys
import pygame
from game.components.button import Button
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BG_MENU, SOUND_BUTTON

class Menu:
  HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
  HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
  MENU_COLOR = (255, 255, 255)
  MESSAGE_COLOR = (255, 255, 255)

  def __init__(self, screen):
    screen.blit(BG_MENU, (0,0))
    self.screen = screen.blit(BG_MENU, (0,0))
    self.font = pygame.font.Font(FONT_STYLE, 30)
    self.show_button_menu = True
    self.show_buttons_muerte = False
    self.show_buttons_score = False
  
  def update(self, game):
    pygame.display.update()
    self.handle_events_on_menu(game)

  
  def draw(self, game, screen, message, x = HALF_SCREEN_WIDTH, y = HALF_SCREEN_HEIGHT, color = (0, 0, 0)):
    text = self.font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)

    if self.show_button_menu == True:
       self.buttons_menu(game,screen)
    elif self.show_buttons_muerte == True:
       self.buttons_muerte(game,screen)
    elif game.show_leader_board == True:
       self.buttons_score(game,screen)


  def handle_events_on_menu(self, game):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game.playing = False
        game.running = False
      elif event.type == pygame.KEYDOWN:
        if game.death_count.count > 0 and event.key == pygame.K_h:
          game.show_leader_board = True
        elif game.death_count.count > 0 and event.key == pygame.K_m:
          game.show_leader_board = False
        elif game.show_leader_board and event.key == pygame.K_s:
          game.show_leader_board = False
          game.run()
        else:
          game.show_leader_board = False
          game.run()
        
  def reset(self, screen):
    screen.blit(BG_MENU, (0,0))
    self.screen = screen.blit(BG_MENU, (0,0))
    
  def sonido_boton(self):
      sound_button= pygame.mixer.Sound(SOUND_BUTTON)
      pygame.mixer.Sound.play(sound_button)

  def update_message(self, message):
    self.text = self.font.render(message, True, self.MESSAGE_COLOR)
    self.text_rect = self.text.get_rect()
    self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

  def get_font(size): 
    return pygame.font.Font(FONT_STYLE, size)
  
  def buttons_menu(self,game,screen):
     
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = Menu.get_font(100).render("ATTACK IN SPACE", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(550, 80))

            PLAY_BUTTON = Button(image=pygame.image.load("game/assets/Play Rect.png"), pos=(550, 230), 
                                text_input="PLAY", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            
            SCORE_BUTTON = Button(image=pygame.image.load("game/assets/Options Rect.png"), pos=(550, 380), 
                                text_input="SCORE", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")

            QUIT_BUTTON = Button(image=pygame.image.load("game/assets/Quit Rect.png"), pos=(550, 530), 
                                text_input="QUIT", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")

            screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, SCORE_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    game.data_save()#-----------------------------------------------------------------------------
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.sonido_boton()
                        game.run()
                        self.menu_back = False 

                    if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.sonido_boton()
                        self.show_button_menu = False
                        game.show_leader_board = True
                        
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        game.data_save()#-----------------------------------------------------------------------------
                        self.sonido_boton()
                        game.playing = False
                        game.running = False
                        pygame.quit()
                        sys.exit()
     
  def buttons_muerte(self,game,screen):
     
    boton_grande0 = pygame.image.load("game/assets/Play Rect.png")
    boton_grande = pygame.transform.scale(boton_grande0, (200, 50))

    boton_load_2 = pygame.image.load("game/assets/Quit Rect.png")
    boton_scale_2 = pygame.transform.scale(boton_load_2, (230, 50))
     

    MENU_MOUSE_POS = pygame.mouse.get_pos()
    

    PLAY_BUTTON = Button(image=boton_grande, pos=(300, 400), 
        text_input="PLAY AGAIN", font=Menu.get_font(30), base_color="#d7fcd4", hovering_color="White")
        
    SCORE_BUTTON = Button(image=boton_scale_2, pos=(850, 400), 
        text_input="HIGH SCORES", font=Menu.get_font(30), base_color="#d7fcd4", hovering_color="White")
        
    for button in [PLAY_BUTTON, SCORE_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                self.sonido_boton()
                game.run()
                self.menu_back = False
             
            if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                self.sonido_boton()
                game.data_save()#-----------------------------------------------------------------------------
                #game.button_menu = None
                self.show_buttons_muerte = False
                game.show_leader_board = True
            
                

  def buttons_score(self, game, screen):
        
        boton_grande0 = pygame.image.load("game/assets/Play Rect.png")
        boton_grande = pygame.transform.scale(boton_grande0, (200, 50))

        boton_load_2 = pygame.image.load("game/assets/Quit Rect.png")
        boton_scale_2 = pygame.transform.scale(boton_load_2, (200, 50))
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        

        PLAY_BUTTON = Button(image=boton_grande, pos=(300, 400), 
            text_input="PLAY AGAIN", font=Menu.get_font(30), base_color="#d7fcd4", hovering_color="White")
            
        QUIT_BUTTON = Button(image=boton_scale_2, pos=(850, 400), 
            text_input="BACK", font=Menu.get_font(30), base_color="#d7fcd4", hovering_color="White")
            
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.data_save()#-----------------------------------------------------------------------------
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.sonido_boton()
                    game.run()
                    self.menu_back = False
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.sonido_boton()
                    game.show_leader_board = False
                    game.button_menu = False
