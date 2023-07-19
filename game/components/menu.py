
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame


class Menu:

    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    MENU_COLOR = (255, 255, 255)
    MESSAGE_COLOR = (0, 0, 0)

    def __init__(self, message, screen):
        screen.fill(self.MENU_COLOR)
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, self.MESSAGE_COLOR)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset(self, screen):
        screen.fill(self.MENU_COLOR)

    def update_message(self, message):
        self.text = self.font.render(message,True, self.MESSAGE_COLOR)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)



