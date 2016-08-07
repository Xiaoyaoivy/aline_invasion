# -*- coding: utf-8 -*-
import sys  # 退出模块
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()  # 定义类
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))

    # screen = pygame.display.set_mode()#创建和屏幕一样大的

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullet(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
