import pygame
class Object():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.Surface([20,20])
        self.image.fill((0,0,255))
        self.rect= self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = (361,100)

    def blitme(self):
        self.screen.blit(self.image, self.rect)