import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, screen):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(400, 300, 3, 15)
        self.y = float(self.rect.centery)
        self.color = 60,60,60
        self.speed_factor = 1

    def update(self):
        self.y -= self.speed_factor
        self.rect.centery = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('MO')
    #bullet_rect = pygame.Rect(400, 300, 3, 15)
    bg_color = (230,230,230)
    #bullet_color = 60,60,60
    bullets = Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_bullet = Bullet(screen)
                    new_bullet.draw_bullet()
                    bullets.add(new_bullet)
        #new_bullet1 = Bullet(screen)
        #bullets.add(new_bullet1)

        screen.fill(bg_color)
        bullets.update()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()



run_game()