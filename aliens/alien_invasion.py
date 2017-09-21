import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from backgrounds import Moon

import game_fuctions as gf
def run_g():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings, screen)
    bullets = Group()
    backgrounds = Moon(screen)
    alien = Alien(ai_settings, screen)
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets, backgrounds)
        ##pygame.display.flip()


    
##一个策略射击游戏的想法，子弹会在大地图上无限飞翔直到击中目标，不断会有各种怪
##从远近战场各种地方不断刷新，只要没打死的敌人就会升级复活，因此从起点到终点，
##玩家面临的挑战是在节约弹药的前提下尽可能快多的杀死敌人，弹药有很多种，比如穿透和爆炸..
##升级项目则可以包括增大视野范围
run_g()
