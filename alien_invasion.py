import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(screen)

    # set up the background color
    # bg_color = (230, 230, 230)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ship)   # game functions

        # redraw the screen during each pass through the loop
        # make the most recently drawn screen visible
        gf.update_screen(ai_settings, screen, ship)


run_game()
