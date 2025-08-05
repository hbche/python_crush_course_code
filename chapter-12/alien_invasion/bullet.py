from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    """管理飞船锁发射的子弹类"""

    def __init__(self, ai_game):
        super()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color
        # 创建一个矩形
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # 将子弹设置在飞船的顶部
        self.rect.midtop = ai_game.ship.midtop

        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新子弹的准确位置
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的 rect 位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
