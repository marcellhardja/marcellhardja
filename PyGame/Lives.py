import pygame
from pygame.sprite import Sprite

class Lives(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Lives,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:\\Users\\user\\PycharmProjects\\PyGame\\burger.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()