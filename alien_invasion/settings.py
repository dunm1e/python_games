class Settings:
    """存储游戏《alien_invation》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # self.ship_speed = 4.0
        self.ship_limit = 3

        # 子弹设置
        # self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 外星人设置
        # self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移动，为 -1 表示向左移动
        self.fleet_direction = 1

        # 以什么速度加快游戏的节奏
        self.speedup_scale = 1.5

        self.difficulty_level = 'medium'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        if self.difficulty_level == 'easy':
            self.ship_limit = 5
            self.bullets_allowed = 10
            self.ship_speed = 2.5
            self.bullet_speed = 1.5
            self.alien_speed = 1.5
        elif self.difficulty_level == 'medium':
            self.ship_limit = 3
            self.bullets_allowed = 5
            self.ship_speed = 3.0
            self.bullet_speed = 3.0
            self.alien_speed = 3.0
        elif self.difficulty_level == 'difficult':
            self.ship_limit = 2
            self.bullets_allowed = 3
            self.ship_speed = 4.0
            self.bullet_speed = 6.0
            self.alien_speed = 5.0

    def increase_speed(self):
        """提高速度设置的值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def set_difficulty(self, diff_setting):
        if diff_setting == 'easy':
            print('easy')
        elif diff_setting == 'medium':
            pass
        elif diff_setting == 'difficult':
            pass
