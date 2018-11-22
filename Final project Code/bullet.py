import pygame
from pygame.sprite import Sprite

speed = int(input("Input bullet speed: "))
bullet_width = 30
bullet_speed_factor = speed
bullet_height = 10
bullet_color = (255,255,255)

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, screen):
        super(Bullet, self).__init__()
        self.screen = screen

        self.x_position = 10
        self.y_position = 90
        self.rect = pygame.Rect(self.x_position, self.y_position, bullet_width, bullet_height)

        self.color = bullet_color
        self.speed_factor = bullet_speed_factor

    def update(self):
        #Update the decimal position of the bullet
        self.x_position += self.speed_factor
        self.rect = pygame.Rect(self.x_position, self.y_position, bullet_width, bullet_height)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)