import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_key_down_events(event, ai_settings, screen, ship, bullets):
    # respond to key presses
    if event.key == pygame.K_RIGHT:
        # move the ship to the right continuously
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a new bullet and add it to the bullets group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # respond to key presses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def create_fleet(ai_settings, screen, aliens):
    # create a full fleet of aliens
    # create an alien and find the number of aliens in a row
    # spacing between each alien is equal to one alien width

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # create the first row of aliens
    for alien_number in range(number_aliens_x):
        # create an alien and place it in the row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def fire_bullet(ai_settings, screen, ship, bullets):
    # fire a bullet if limit not reached
    # create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    # update position of bullets and get rid of old bullets
    # update bullet position
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # update images on the screen and flip to the new screen
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)

    # make the most recently drawn screen visible
    pygame.display.flip()
