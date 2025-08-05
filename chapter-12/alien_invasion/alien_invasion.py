import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

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
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # # 初始化背景色属性
        # self.bg_color = (230, 230, 230)
        pygame.display.set_caption("外星人入侵")
        # 初始化飞船
        self.ship = Ship(self)

        # 初始化字段编组
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""

        # 事件循环，管理屏幕更新
        while True:
            self._check_events()
            self.ship.update()
            # 调用 Sprite 编组的 update 方法，会调用编组内每个元素的 update() 方法，即 Bullet 类的 update() 方法
            self.bullets.update()
            self._update_screen()
            # 暂停指定时长，以便保持相同的帧率
            # Clock实例的tick方法接受一个帧率的参数，表示每秒刷新的次数。此处设置60，即每秒运行60次
            self.clock.tick(60)

    
    def _check_events(self):
        """响应按键和鼠标事件"""
        # 事件循环，监听事件，根据事件的类型执行对应的逻辑
        # 通过 pygame.event.get 获取 Pygame 模块检测到的事件
        for event in pygame.event.get():
            # 当游戏玩家点击屏幕中的关闭按钮时将触发此事件
            if event.type == pygame.QUIT:
                sys.exit()
            # 按键按下事件
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 按键松开事件
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键按下事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """响应按键释放事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹并将其存储在子弹编组中"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环是都要重绘屏幕
        # 使用指定的背景色填充屏幕背景
        # self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
        # 绘制子弹
        for bullet in self.bullets:
            bullet.draw_bullet()
        # 绘制飞船
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        # 绘制空屏，擦除旧屏
        pygame.display.flip()



if __name__ == '__main__':
    # 创建游戏实例，并运行游戏
    ai = AlienInvasion()
    ai.run_game()