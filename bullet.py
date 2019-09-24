import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # a class to manage bullets fired from the ship
    def __init__(self, ai_settings, screen, ship):
        # create a bullet object at the ship's current position
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # move bullet up the screen
        # update the decimal position of the bullet
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        # draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

    def draw_button(self):
        # draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_ret.center = self.rect.center

