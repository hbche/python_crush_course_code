import pygame

class Ship:
    """模拟飞船"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取图像的外接矩形
        self.image = pygame.image.load('E:\python_crush_course_code\chapter-13\\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船都放在屏幕底部中间
        self.rect.midbottom = self.screen_rect.midbottom

        # 增加飞船移动标识
        self.moving_right = False
        self.moving_left = False
        # 存储飞船x坐标，存在小数值
        self.x = float(self.rect.x)

    def update(self):
        """限制飞船的移动范围，限制在游戏窗口范围内，根据移动速度和移动标识更新飞船的位置"""

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # 根据self.x 更新 self.rect
        self.rect.x = self.x

    def blitme(self):
        """将飞船绘制到游戏窗口上"""

        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船重置到屏幕底部中央"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)