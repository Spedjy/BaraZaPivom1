import sys
import pygame

from turtle import Screen
from setting import Settings
from ship import Ship

from pygame.sprite import Group

import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана.
    bg_color = (230, 230, 230)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Создание Корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    aliens = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf,gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        screen.fill(ai_settings.bg_color)
        ship.update()
        ship.blitme()
        
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()
