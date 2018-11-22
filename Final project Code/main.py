import pygame
from pygame.locals import *
import pygame.surfarray
from pendulum import Pendulum
from gun import Gun
from bullet import Bullet
import os
from invisible_object import Object
from menu import Menu

# Set the position of the window of game
os.environ['SDL_VIDEO_WINDOW_POS'] = "300,20"


COLOR = {'black': (0, 0, 0),
         'red': (255, 0, 0),
         'green': (0, 255, 0),
         'blue': (0, 0, 255),
         'white': (255,255,255)}

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns.
    """
    mass = int(input("Input mass: "))

    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('Pendulum Simulation')

    # Import the gun
    gun = Gun(screen)
    bullet = Bullet(screen)
    invisible_object = Object(screen)
    menu = Menu(screen)

    # Create The Backgound
    background = pygame.Surface(screen.get_size())
    background.fill(COLOR['black'])

    # Prepare Objects
    clock = pygame.time.Clock()
    p1 = Pendulum(pivot_vect=SCREEN_CENTER, length=300, bob_radius=50, bob_mass=mass, init_angle= 3.1415926535)

    # A container class managing sprites
    free_group = pygame.sprite.Group(p1)

    menu.draw_menu()
    hit = True
    play = False

    # Main Loop
    while True:
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                play = True



        if(play):
            # To make the pendulum move
            free_group.update()
            # Display the background
            screen.blit(background, (0, 0))
            # To draw the bob and line
            free_group.draw(screen)
            # To show the gun
            gun.blitme()


            if hit == True:
                invisible_object.blitme()
                # Shooting the bullet
                bullet.draw_bullet()
                bullet.update()
            # When the bullet hits the invisible object, both bullet and object will be gone
            # If hit isn't changed to false, the invisible object and bullet will not be gone
            if pygame.sprite.collide_rect(bullet, invisible_object):
                hit = False




main()

"""Created by Craig Wm. Versek
    from https://gist.github.com/cversek/98dead0521677d0b7d4d4162715704be"""