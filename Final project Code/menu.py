import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 500
        self.height = 500
        self.box_color = (0,0,0)
        self.txt_box_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont("Calibri", 50)

        self.rect = pygame.Rect(400,400,self.width, self.height)

        self.play_button = self.font.render("START", True, self.text_color, self.txt_box_color)
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (400,400)


    def draw_menu(self):
        self.screen.fill(self.box_color, self.rect)
        self.screen.blit(self.play_button, self.play_button_rect)

