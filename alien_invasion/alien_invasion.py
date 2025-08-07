import pygame
import sys
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien

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
        # 初始化外星人分组
        self.aliens = Group()
        # 设置标题
        pygame.display.set_caption("Alien Invasion")

        self.clock = pygame.time.Clock()

        self._create_fleet()

    def _create_alien(self, current_x, current_y):
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        new_alien.y = current_y
        new_alien.rect.y = current_y
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """创建一个外星人舰队"""

        # 创建第一个外星人
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_x = alien_width
        current_y = alien_height
        # 创建多行外星人
        while current_y < self.settings.screen_height - alien_height * 3:
            # 创建一行外星人
            while current_x < self.settings.screen_width - alien.rect.width * 2:
                self._create_alien(current_x, current_y)
                current_x += alien.rect.width * 2
            # 重置下一行起始外星人的横坐标
            current_x = alien_width
            current_y += alien_height * 2
            print(len(self.aliens))

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self.__check_events()

            # 更新飞船的位置
            self.ship.update()
            # 更新子弹的坐标
            self.__update_bullets()
            # 更新外星人的坐标
            self.__update_aliens()
            # 更新屏幕
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

    def __update_aliens(self):
        # """更新外星人的坐标，并且检测外星人舰队是否触碰边缘，如果触碰需要修改舰队的移动方向和位置"""
        self.__check_fleet_edges()
        self.aliens.update()

    def __check_fleet_edges(self):
        """在有外星人触碰边缘时采取相应的措施"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.__change_fleet_direction()
                """如果存在外星人触碰了边缘，则直接结束遍历"""
                break
            
    def __change_fleet_direction(self):
        """调整外星人舰队向下移动，并调整移动顺序"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def __update_screen(self):
        """更新屏幕"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 调用飞船实例的 blitme() 方法，在游戏窗口上绘制飞船
        self.ship.blitme()

        # 遍历子弹分组，绘制每个子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()         

        # 在屏幕上绘制外星人分组
        self.aliens.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
