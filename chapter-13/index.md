## 第 13 章 外星人

本章将学习大型项目的文件管理，pygame 游戏开发中碰撞检测。

### 13.1 项目回顾

### 13.2 创建第一个外星人

与飞船相似，我们声明 Alien 类模拟外星人。

#### 13.2.1 创建外星人类

```python alien.py
from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    """模拟外星人"""

    def __init__(self, ai_game):
        """初始化"""

        super.__init__()
        self.screen = ai_game.screen

        # 加载外星人图片，并设置其 rect 属性
        self.image = pygame.image.load('E:\python_crush_course_code\\alien_invasion\images\alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精准水平坐标
        self.x = float(self.rect.x)
```

#### 13.2.2 创建 Alien 实例

```python
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

    def _create_fleet(self):
        """创建一个外星人舰队"""

        # 创建第一个外星人
        alien = Alien(self)
        self.aliens.add(alien)

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
```

注意绘制外星人的顺序，需要在 \_\_update_screen() 方法中，且需要在 self.screen.fill() 方法的后面，否则外星人将被背景色覆盖。

### 13.3 创建外星人舰队

要绘制外星舰队，需要确定如何使用外星人填充屏幕的上半部分，同时避免游戏窗口过于拥挤。实现这个目标的方式有很多，我们将采取如下方法：沿屏幕上边缘水平向右不断地添加外星人，直到填满一整行；然后重复这个过程，直到没有足够的垂直空间供我们再添加一行为止。

#### 13.3.1 创建一行外星人

我们以第一个外星人作为参照点，依次向右平铺，每个外星人之间间距一个外星人宽度的距离。

```python
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

    def _create_fleet(self):
        """创建一个外星人舰队"""

        # 创建第一个外星人
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        current_x = alien.rect.x + alien_width * 2
        while current_x < self.settings.screen_width - alien.rect.width * 2:
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += alien.rect.width * 2
        print(len(self.aliens))

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
```

#### 13.3.2 重构 \_create_fleet() 方法

我们将 \_create_fleet() 方法内部创建单个外星人的逻辑进行抽取，声明称 \_create_alien() 方法

```python
    def __init__():
        --snip--
        self._create_fleet()

    def _create_alien(self, current_x):
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """创建一个外星人舰队"""

        # 创建第一个外星人
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        current_x = alien.rect.x + alien_width * 2
        while current_x < self.settings.screen_width - alien.rect.width * 2:
            self._create_alien(current_x)
            current_x += alien.rect.width * 2
        print(len(self.aliens))
```

#### 13.3.3 创建多行外星人

```python
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
```

> 注意：每次第一层循环结束后，需要重置 `current_x` 的位置为屏幕左侧起始位置，否则下一行将在上一行最后一个的后面接着绘制，在屏幕之外，将无法看到。

### 13.4 让外星人舰队移动

#### 13.4.1 向右移动外星人舰队

在 Alien 类中声明 settings 记录外星人的设置，x 属性记录当前外星人的横坐标，update 方法用来更新外星人向右移动。

```python alien.py
from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    """模拟外星人"""

    def __init__(self, ai_game):
        """初始化"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图片，并设置其 rect 属性
        self.image = pygame.image.load('E:\python_crush_course_code\\alien_invasion\images\\alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 记录外星人的水平坐标
        self.x = self.rect.x

        # 存储外星人的精准水平坐标
        self.x = float(self.rect.x)

    def update(self):
        """向右移动外星人"""

        self.x += self.settings.alien_speed
        self.rect.x = self.x
```

在 alien_invasion.py 程序中，调用外星人元组 aliens.update() 方法来更新所有外星人的坐标，然后在 \_\_update_screen() 中调用 aliens.draw(self.screen) 将更新位置后的外星人绘制到屏幕上。

```python alien_invasion.py

def run_game(self):
    --snip--

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

def __update_aliens(self):
    """更新外星人的坐标"""
    self.aliens.update()

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
```

#### 13.4.2 检查外星人是否到达屏幕边缘

目前的逻辑如果不做修改的话，外星人在经过一定移动次数之后，将消失在屏幕的右方。

因此，我们需要增加外星人移动方向的设置，我们在 Setting 类中新增 fleet_direction 标识，如果为 1 则标识向右移动，如果为 -1 则标识向左移动。

```python
class Settings:
    --snip--
    # 外星舰队移动的速度
    self.alien_speed = 1.0
    # 外星舰队移动方向标识，1 表示向右移动， -1 表示向左移动
    self.fleet_direction = 1
    # 外星人舰队触碰边缘之后想下移动速度
    self.fleet_drop_speed = 10
```

同时我们需要更新 Alien 类的 update 方法，将结合 fleet_direction 进行坐标更新。通过 ai_game 实例参数我们可以将 settings 信息存储在 Alien 的 settings 属性中，方便后续方法访问设置参数。

```python alien.py
def update(self):
    """向右或向左移动外星人"""

    self.x += self.settings.alien_speed * self.settings.fleet_direction
    self.rect.x = self.x
```

#### 13.4.3 创建表示外星舰队移动方向的设置

为了修改外星人的移动方向，我们给 Alien 类增加一个检测外星人舰队触碰屏幕边缘的计算方法，为后续检测外星人舰队触碰屏幕两侧时改变移动方向做准备：

```python alien.py
def check_edges(self):
    """检测外星人是否到达屏幕边缘"""

    screen_rect = self.screen.get_rect()
    return self.rect.right >= screen_rect.right or self.rect.left <= 0
```

#### 13.4.4 向下移动外星人舰队并改变移动方向

alien_invasion.py 程序中，在更新外星人坐标时，先检测上次移动的位置是否存在碰撞，如果存在碰撞，需要修改飞船的移动方向和 y 坐标。

```python alien_invasion.py
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
```

### 13.5 击落外星人

我们创建了飞船和外星舰队，但子弹在击中外星人时，将穿过外星人，因为还没有检查碰撞。在游戏编程中，碰撞指的是游戏元素有重叠。为了让子弹能够击落外星人，我们将使用函数 sprite.groupcollide() 检测两个编组的成员之间的碰撞。

#### 13.5.1 检测子弹和外星人的碰撞
