# -*- coding:utf-8 -*-
import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

def check_event(ai_setting, screen, ship, bullets, stats, play_button, score):
    #按键监测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, stats, play_button, mouse_x, mouse_y, score)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            elif event.key == pygame.K_LEFT:
                ship.move_left =True
            elif event.key == pygame.K_UP:
                ship.move_up =True
            elif event.key == pygame.K_DOWN:
                ship.move_down =True
            elif event.key == pygame.K_LALT:
                new_bullet = Bullet(ai_setting, screen, ship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_q:
                sys.exit()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False
            elif event.key == pygame.K_UP:
                ship.move_up = False
            elif event.key == pygame.K_DOWN:
                ship.move_down = False

def update_screen(ai_setting, screen, ship, aliens, bullets, stats, play_button, score):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #加载ship
    ship.blitme()
    aliens.draw(screen)
    score.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_setting, screen, ship, aliens, bullets, stats, score):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets, stats, score)


def check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets, stats, score):
    # 子弹与外星人碰撞检测
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        #修复一个子弹同时消灭多个外星人计分
        for alien_num in collisions.values():
            stats.score += ai_setting.alien_point*len(alien_num)
            score.prep_score()
        check_high_score(stats, score)
    # 外星人为空，重新创建
    if len(aliens) == 0:
        bullets.empty()
        #通过提高速度来提高游戏等级
        ai_setting.increase_speed()
        #显示等级提升
        stats.level += 1
        score.prep_level()
        create_aliens(ai_setting, screen, aliens, ship)



def get_alien_num(ai_setting, alien_width):
    '''获取每行外星人数量'''
    available_alien_x = ai_setting.screen_width - (2 * alien_width)
    number_alien = int(available_alien_x / (2 * alien_width))
    return number_alien

def get_alien_row(ai_setting, alien_height, ship_height):
    '''获取外星人行数'''
    available_alien_y = ai_setting.screen_height - 3*alien_height - ship_height
    rows_alien = int(available_alien_y / (2*alien_height))
    return rows_alien


def create_alien(ai_setting, screen, aliens, number_alien, row_alien):
    '''创建单个外星人'''
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * number_alien * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * row_alien * alien_height
    aliens.add(alien)

def create_aliens(ai_setting, screen, aliens, ship):
    '''创建外星人群'''
    alien = Alien(ai_setting, screen)
    nums = get_alien_num(ai_setting, alien.rect.width)
    rows = get_alien_row(ai_setting, alien.rect.height, ship.rect.height)
    for row_alien in range(rows):
        for number_alien in range(nums):
            create_alien(ai_setting,screen, aliens, number_alien, row_alien)

def check_alien_edge(ai_setting, aliens):
    '''检测外星人到达边缘两侧，则更改移动方向'''
    for alien in aliens.sprites():
        if alien.check_edge():
            change_alien_direction(ai_setting, aliens)
            break

def check_alien_bottom(ai_setting, screen, ship, aliens, bullets, stats):
    '''检测外星人是否到底底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, screen, ship, aliens, bullets, stats)
            break


def change_alien_direction(ai_setting, aliens):
    '''更改移动方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.alien_drop_speed
    ai_setting.alien_move_direction *= -1


def update_aliens(ai_setting, screen, ship, aliens, bullets, stats):
    check_alien_edge(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, screen, ship, aliens, bullets, stats)
    check_alien_bottom(ai_setting, screen, ship, aliens, bullets, stats)

def ship_hit(ai_setting, screen, ship, aliens, bullets, stats):
    if stats.ship_left > 0:
        #飞船数量减1
        stats.ship_left -= 1
        #清空子弹及外星人
        aliens.empty()
        bullets.empty()
        #重新创建外星人
        create_aliens(ai_setting, screen, aliens, ship)
        #飞船恢复初始位置
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False

def check_play_button(ai_setting, stats, play_button, mouse_x, mouse_y, score):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        ai_setting.init_setting()
        stats.game_active = True
        #重置等级和得分
        score.prep_level()
        score.prep_score()

def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()


