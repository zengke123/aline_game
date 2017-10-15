# -*- coding:utf-8 -*-
class Setting(object):
    #控制游戏外观和飞船速度
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #飞船数量限制
        self.ship_limit = 2
        #子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.speedup = 1.1
        self.alien_point_up = 1.2
        self.init_setting()

    def init_setting(self):
        # 飞船速度
        self.ship_speed_factor = 1.5
        # 子弹速度
        self.bullet_speed_factor = 3
        # 外星人移动速度
        self.alien_speed_factor = 1
        # 外星人下降速度
        self.alien_drop_speed = 10
        # 外星人移动方向，1向右，-1向左
        self.alien_move_direction = -1

        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup
        self.alien_speed_factor *= self.speedup
        self.alien_drop_speed *= self.speedup
        self.alien_point = int(self.alien_point * self.alien_point_up)





