import pygame.font
class Scoreboard():
    """显示得分信息的类"""
    def __init__(self,ai_settings, screen,stats):
        """初始化显示得分涉及的属性"""
        self.screen=screen
        self.screen.rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats
        # 显示得分信息时使用的字体设置
        self.text.color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #准备初始化图像
        self.prep_score()