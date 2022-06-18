import sys

import pygame

from screen import Screen

pygame.init()

class Alien:
    """Creating an alien"""

    def __init__(self):
        self.settings = Screen()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('C:\Python\python_intro/alien.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom 
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def run_game(self):
        while True:
            self.screen.fill(self.settings.color)
            self.blitme()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

ai = Alien()
ai.run_game()