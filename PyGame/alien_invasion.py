import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf
def run_game():
     # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to score game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
     # Make an alien.
    alien = Alien(ai_settings, screen)
     # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
     # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

    pygame.mixer.music.load('C:\\Users\\user\\PycharmProjects\\PyGame\\song.mp3')
    pygame.mixer.music.play(-1)
     # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # Watch for keyboard and mouse events.
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # Make the most recently drawn screen visible.0
        # gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

        # pygame.display.flip()
        print("len : "+str(len(bullets)))

run_game()