import pygame

class Ship:
    """模拟飞船实体"""

    def __init__(self, ai_game):
        """初始化飞船，并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像，并获取其外接矩形
        # self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('E:\python_crush_course_code\chapter-12\\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        # 每艘飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 初始化飞船的x坐标
        self.x = float(self.rect.x)

        # 持续左移
        self.moving_right = False
        # 持续右移
        self.moving_left = False


    def blitme(self):
        """指定位置绘制飞船"""

        self.screen.blit(self.image, self.rect)

    
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.x += 1
            self.x += self.settings.ship_speed
            # 根据 self.x 更新 rect 对象
            self.rect.x = self.x
        elif self.moving_left and self.rect.left > 0:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed
            # 根据 self.x 更新 rect 对象
            self.rect.x = self.x
