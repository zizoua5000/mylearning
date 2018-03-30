import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
# from alien import Alien


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets and aliens
    bullets = Group()
    aliens = Group()
    # Make alien
    # alien = Alien(ai_settings, screen)

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        # print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
         # print(str(datetime.datetime.time(datetime.datetime.now())))


run_game()
