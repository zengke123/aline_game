# -*- coding:utf-8 -*-
import pygame

#top, left, bottom, right
#center, centerx, centery

class Ship(object):

    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.ai_setting = ai_setting
        #load image
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #设置起始位置,居中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #与窗口底部对齐
        self.rect.bottom = self.screen_rect.bottom


        self.center = float(self.rect.centerx)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
            #self.rect.centerx += 1
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
            #self.rect.centerx -= 1
        if self.move_up and self.rect.top >0:
            self.rect.centery -= self.ai_setting.ship_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_setting.ship_speed_factor
        #根据center来更新rect
        self.rect.centerx = self.center

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom