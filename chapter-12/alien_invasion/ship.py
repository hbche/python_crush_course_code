import pygame

class Ship:
    """模拟飞船实体"""

    def __init__(self, ai_game):
        """初始化飞船，并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像，并获取其外接矩形
        # self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('E:\python_crush_course_code\chapter-12\\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        # 梅艘飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """指定位置绘制飞船"""

        self.screen.blit(self.image, self.rect)