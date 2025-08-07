import pygame
import sys
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet

class AlienInvasion:
    """模拟外星人入侵游戏"""

    def __init__(self):
        """初始化"""

        # 初始化游戏并创建资源
        pygame.init()
        # 初始化设置
        self.settings = Settings()
        # 创建空白屏幕，pygame.display.set_mode方法的参数是一个表示屏幕宽高的元组
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 初始化飞船
        self.ship = Ship(self)
        # 初始化子弹分组
        self.bullets = Group()
        # 设置标题
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self.__check_events()

            # 更新飞船的位置
            self.ship.update()
            self.__update_bullets()
            self.__update_screen()

    def __check_events(self):
        """事件检测"""
        
        # 监听键盘和鼠标点击事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.__check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event)

    def __check_keydown_events(self, event):
        """检测按键按下事件"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.__fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def __fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            # 增加子弹
            new_bullet = Bullet(self)
            # 向子弹分组中添加新加的子弹
            self.bullets.add(new_bullet)

    def __check_keyup_events(self, event):
        """检测按键松开事件"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def __update_bullets(self):
        # 更新子弹的位置，调用分组的update方法，该方法会调用元组内部所有子弹的update方法更新每个子弹自身的位置
        self.bullets.update()

        # 移除消失在屏幕外的子弹
        for bullet in self.bullets.copy():
            if bullet.y <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    
    def __update_screen(self):
        """更新屏幕"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 调用飞船实例的 blitme() 方法，在游戏窗口上绘制飞船
        self.ship.blitme()

        # 遍历子弹分组，绘制每个子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()         

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
