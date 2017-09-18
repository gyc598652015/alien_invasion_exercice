import sys

import pygame
from settings import Settings
from ship import Ship
from backgrounds import Moon

import game_fuctions as gf
def run_g():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    backgrounds = Moon(screen) 
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship, backgrounds)

        pygame.display.flip()


    


run_g()
