import pygame

class Ship:
    """Class for controling a ship"""

    def __init__(self, ai_game):
        """Define a ship and its start position"""
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()

        #Load ship image
        self.image = pygame.image.load('C:\Python\project#1\ship.bmp')
        self.rect = self.image.get_rect()

        #Create new ship on the bottom of the screen in the middle
        self.rect.midbottom = self.screen_rect.midbottom 
    def blitme(self):
        """Draw a ship in his current position"""
        self.screen.blit(self.image, self.rect)