import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_functions as gf


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in
    bullets = Group()

    # make an alien
    alien = Alien(ai_settings, screen)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)   # game functions
        ship.update()

        # redraw the screen during each pass through the loop
        # make the most recently drawn screen visible
        gf.update_bullets(bullets)
        # get rid of bullets that have disappeared
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
