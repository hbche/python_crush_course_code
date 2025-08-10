import pygame
import sys
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from pygame import sprite
from game_stats import GameStats
from time import sleep

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

        # 创建一个用于存储游戏统计信息的实例
        self.game_stats = GameStats(self)

        # 初始化时钟
        self.clock = pygame.time.Clock()

        # 游戏启动后处于活跃状态
        self.game_active = True

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

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self.__check_events()
            
            if self.game_active:
                # 更新飞船的位置
                self.ship.update()
                # 更新子弹的坐标
                self.__update_bullets()
                # 更新外星人的坐标
                self.__update_aliens()
            # 更新屏幕
            self.__update_screen()
            self.clock.tick(60)

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
        self.__check_bullet_alien_collisions()

    def __check_bullet_alien_collisions(self):
        
        # 检查子弹与外星人之间的碰撞
        # 如果存在碰撞则删除对应的子弹和外星人
        collisions = sprite.groupcollide(self.bullets, self.aliens, True, True)

        # 检测外星人的数量，如果外星人舰队全部被消灭了，重新生成一组外星人舰队，同时清空子弹
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
                
    def __update_aliens(self):
        # """更新外星人的坐标，并且检测外星人舰队是否触碰边缘，如果触碰需要修改舰队的移动方向和位置"""
        self.__check_fleet_edges()
        self.aliens.update()
        # 检查是否有外星人到达屏幕下边缘
        self._check_aliens_bottom()
        # 检查是否存在外星人与飞船发生碰撞的
        if sprite.spritecollideany(self.ship, self.aliens):
            self.__ship_hit()

    def _check_aliens_bottom(self):
        """是否有外星人到达屏幕的下边缘"""

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 像碰撞飞船一样处理
                self.__ship_hit()
                break
        
    def __ship_hit(self):
        print(self.game_stats.ships_left)
        if self.game_stats.ships_left > 0:
            # 将 ship_left 减 1
            self.game_stats.ships_left -= 1 

            # 清空外星舰队和子弹
            self.bullets.empty()
            self.aliens.empty() 

            # 重新创建外星人舰队
            self._create_fleet()
            # 将飞船重置在屏幕底部中间
            self.ship.center_ship()
            # 暂停 0.5秒
            sleep(0.5)
        else:
            self.game_active = False

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

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
