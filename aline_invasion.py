# -*- coding: utf-8 -*-
import sys  # 退出模块
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_function as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()  # 定义类
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))

    # screen = pygame.display.set_mode()#创建和屏幕一样大的

    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()

    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)
        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)

            gf.update_aliens(ai_settings, screen, stats, sb,
                             ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)


run_game()
