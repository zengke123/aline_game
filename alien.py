import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_setting, screen):
        super(Alien,self).__init__()
        self.ai_setting = ai_setting
        self.screen = screen

        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.alien_move_direction)
        self.rect.x = self.x


    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True




