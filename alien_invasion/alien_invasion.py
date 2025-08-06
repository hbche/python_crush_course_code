import pygame
import sys
from settings import Settings
from ship import Ship

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
        self.ship = Ship(self)
        # 设置标题
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self.__check_events()

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
        elif event.key == pygame.K_q:
            sys.exit()

    def __check_keyup_events(self, event):
        """检测按键松开事件"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    
    def __update_screen(self):
        """更新屏幕"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 更新飞船的位置
        self.ship.update()
        # 调用飞船实例的 blitme() 方法，在游戏窗口上绘制飞船
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
