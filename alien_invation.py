import pygame

from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from board import Scoreboard
def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('MO')
    ship = Ship(screen, ai_setting)

    bullets = Group()
    aliens = Group()
    gf.create_aliens(ai_setting, screen, aliens, ship)

    stats = GameStats(ai_setting)
    score = Scoreboard(ai_setting, screen, stats)
    play_button = Button(ai_setting, screen, 'PLAY')
    while True:
        gf.check_event(ai_setting, screen, ship, bullets, stats, play_button, score)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets, stats, score)
            gf.update_aliens(ai_setting, screen, ship, aliens, bullets, stats)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets, stats, play_button, score)



run_game()
