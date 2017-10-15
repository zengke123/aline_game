# -*- coding:utf-8 -*-
class GameStats(object):
    '''游戏的统计信息'''

    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_active = False

        #一般情况下最高得分不会被重置，所以放在init中，而不是reset_stats
        #self.high_score = 0
        with open('.high_score','r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1

