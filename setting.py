class Settings():
    def __init__(self):
        """初始化设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(255,255,255)
        # 子弹设置
        self.bullet_width = 7
        self.bullet_height = 17
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5
        # 外星人设置
        self.fleet_drop_speed = 10
        # 飞船设置
        self.ship_limit = 1
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 0.3
        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale