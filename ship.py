import pygame


class Ship:
    # In Pygame, the origin (0, 0) is at the top-left corner of the screen
    # and coordinates increase as you go down and to the right
    def __init__(self, screen):
        # initialize the ship and set its starting position
        self.screen = screen

        # load ship image and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # movement flag
        self.moving_right = False

    def update(self):
        # update the ship's position based on the movement flag
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
