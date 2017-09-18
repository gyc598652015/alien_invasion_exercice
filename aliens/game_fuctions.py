import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship, backgrounds):
        screen.fill(ai_settings.bg_color)
## pay attention to orders, screen first, then the ship        
        ship.blitme()
        backgrounds.blitme()
