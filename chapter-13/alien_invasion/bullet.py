from pygame.sprite import Sprite

import pygame

class Bullet(Sprite):
    """模拟子弹类"""

    def __init__(self, ai_game):
        """初始化子弹"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 用浮点数存储子弹的 y 坐标
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新子弹的准确位置
        self.y -= self.settings.bullet_speed
        # 更新表示子弹位置的 rect 的坐标
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""

        pygame.draw.rect(self.screen, self.color, self.rect)