import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理外星人入侵游戏，管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        # 调用 pygame 模块的 init 函数来初始化背景
        # 默认黑色背景色
        pygame.init()
        # 初始化设置
        self.settings = Settings()
        # 创建 pygame.time 模块中的 Clock 实例用于在循环中计时
        self.clock = pygame.time.Clock()
        # 调用 pygame 模块的 display.set_mode 创建一个显示窗口，这个游戏的所有图形元素都将在其中绘制。
        # set_mode 的参数是一个元组，设置游戏窗口的宽高尺寸
        # 将其保存在 screen 属性中，使得 AlienInvasion 内部所有方法都能够访问
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # # 初始化背景色属性
        # self.bg_color = (230, 230, 230)
        pygame.display.set_caption("外星人入侵")
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""

        # 事件循环，管理屏幕更新
        while True:
            # 事件循环，监听事件，根据事件的类型执行对应的逻辑
            # 通过 pygame.event.get 获取 Pygame 模块检测到的事件
            for event in pygame.event.get():
                # 当游戏玩家点击屏幕中的关闭按钮时将触发此事件
                if event.type == pygame.QUIT:
                    sys.exit()
                # 每次循环是都要重绘屏幕
                # 使用指定的背景色填充屏幕背景
                # self.screen.fill(self.bg_color)
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()
                # 让最近绘制的屏幕可见
                # 绘制空屏，擦除旧屏
                pygame.display.flip()
                # 暂停指定时长，以便保持相同的帧率
                # Clock实例的tick方法接受一个帧率的参数，表示每秒刷新的次数。此处设置60，即每秒运行60次
                self.clock.tick(60)


if __name__ == '__main__':
    # 创建游戏实例，并运行游戏
    ai = AlienInvasion()
    ai.run_game()