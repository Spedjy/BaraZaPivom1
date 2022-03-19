import sys
import pygame

from turtle import Screen
from setting import Settings
from game_stats import GameStats
from ship import Ship

from pygame.sprite import Group

import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана.
    bg_color = (31, 231, 255)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("BaraZaPivom")
    # Создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)
    
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
        screen.fill(ai_settings.bg_color)
        ship.update()
        ship.blitme()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()
