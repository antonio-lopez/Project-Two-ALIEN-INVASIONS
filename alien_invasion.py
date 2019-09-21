import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from alien import Alien
import game_functions as gf


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create an instance to store game statistics
    stats = GameStats(ai_settings)

    # make a ship, group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in
    bullets = Group()
    aliens = Group()

    # make an alien
    # alien = Alien(ai_settings, screen)

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)   # game functions

        if stats.game_active:
            ship.update()

            # redraw the screen during each pass through the loop
            # make the most recently drawn screen visible
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # get rid of bullets that have disappeared
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
