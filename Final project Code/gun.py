import pygame


class Gun():
    def __init__(self, screen):
#Initialize the gun and set its starting position
        self.screen = screen

#Load the gun image
        self.image = pygame.image.load("C:\\Users\\user\\PycharmProjects\\Programming Exercise\\Final Project\\gun_pic.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = (20, 110)

    def blitme(self):
# Draw the gun at its current location.
        self.screen.blit(self.image, self.rect)
