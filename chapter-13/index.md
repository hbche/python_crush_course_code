## 第 13 章 外星人

本章将学习大型项目的文件管理，pygame 游戏开发中碰撞检测。

### 13.1 项目回顾

1. 初始化游戏、主循环、事件监听
2. 初始化设置类
3. 初始化背景
4. 初始化飞船、移动飞船、限制飞船移动范围
5. 初始化子弹、发射子弹、更新子弹位置、移除消失的子弹、限制子弹数量

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
    # 创建多行外星人，给飞船和外星人舰队之间留大于两个外星人小于三个外星人的高度
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

sprite.groupcollide() 函数将一个编组中每个元素的 rect 与另一个编组中每个元素的 rect 进行比较。在这里，是将每颗子弹的 rect 与每个外星人的 rect 进行比较，并返回一个字典，其中包含发生了碰撞的子弹和外星人。在这个字典中，键表示特定的子弹，而关联的值表示被该子弹击中的外星人。

```python alien_invasion.py
def __update_bullets(self):
    # 更新子弹的位置，调用分组的update方法，该方法会调用元组内部所有子弹的update方法更新每个子弹自身的位置
    self.bullets.update()

    # 移除消失在屏幕外的子弹
    for bullet in self.bullets.copy():
        if bullet.y <= 0:
            self.bullets.remove(bullet)

    # 检查子弹与外星人之间的碰撞
    # 如果存在碰撞则删除对应的子弹和外星人
    collisions = sprite.groupcollide(self.bullets, self.aliens, True, True)
```

两个值为 True 的实参告诉 Pygame 在发生碰撞时删除对应的子弹和外星人。要模拟能够飞到屏幕上边缘的高能子弹（它会消灭击中的每个外星人，但自己不受影响）​，可将第一个布尔实参设置为 False，并保留第二个布尔实参为 True。这样被击中的外星人将消失，但所有的子弹始终有效，直到抵达屏幕的上边缘后消失。

#### 13.5.2 为测试创建大量子弹

为了加速游戏测试，可能需要缩小屏幕尺寸减少外星人数量或者增加飞船的子弹限制，或者增大飞船的子弹尺寸。

```python
class Settings:
    def __init__(self):
    --snip--
        # 子弹的宽度
        self.bullet_width = 300
        --snip--
```

#### 13.5.3 生成新的外星舰队

要在一个外星舰队被击落后显示另一个外星舰队，首先需要检查编组 aliens 是否为空。如果是，就调用 \_create_fleet()。我们将在 \_update_bullets() 末尾执行这项任务，因为外星人都是在这里被击落的：

```python
def __update_bullets(self):
    --snip--

    # 检测外星人的数量，如果外星人舰队全部被消灭了，重新生成一组外星人舰队，同时清空子弹
    if len(self.aliens) == 0:
        self.bullets.empty()
        self._create_fleet()
```

#### 13.5.4 加快子弹的速度

自己上手试玩，尝试找到最合适的 bullet_speed 设置

#### 13.5.5 重构 \_\_update_bullets() 方法

将 update_bullets 方法中的碰撞检测部分进行抽取，使得该方法只做子弹位置更新的操作。

```python alien_invasion.py
def __update_bullets(self):
    --snip--

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
```

### 13.6 结束游戏

#### 13.6.1 检测外星人与飞船的碰撞

spritecollideany() 函数接受两个实参：一个精灵和一个编组。它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生碰撞的成员后停止遍历编组。这里，它遍历 aliens 编组，并返回找到的第一个与飞船发生碰撞的外星人。

如果没有发生碰撞，spritecollideany() 将返回 None，因此 ❶ 处的 if 代码块不会执行。如果找到了与飞船发生碰撞的外星人，它就返回这个外星人，因此 if 代码块将执行：打印 Ship hit!!!（见 ❷）​。当有外星人撞到飞船时，需要执行一系列操作：删除余下的外星人和子弹，让飞船重新居中，以及创建一个新的外星舰队。编写完成这些任务的代码前，需要确定检测外星人和飞船碰撞的方法是否可行，而最简单的方式就是调用函数 print()。

```python
def __update_aliens(self):
    # """更新外星人的坐标，并且检测外星人舰队是否触碰边缘，如果触碰需要修改舰队的移动方向和位置"""
    self.__check_fleet_edges()
    self.aliens.update()

    # 检查是否存在外星人与飞船发生碰撞的
    if sprite.spritecollideany(self.ship, self.aliens):
        print("Ship hit!!!")
```

#### 13.6.2 响应外星人和飞船的碰撞

我们不是销毁 Ship 实例再创建一个新的，而是通过跟踪游戏的统计信息来记录飞船被撞了多少次（跟踪统计信息还有助于记分）​。

下面来编写一个用于跟踪游戏统计信息的新类 GameStats，并将其保存为文件 game_stats.py：:

```python
class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行初期可能变化的统计信息"""

        # 飞船的生命指数，当消耗殆尽时，游戏结束
        self.ships_left = self.settings.ship_limit
```

在游戏运行期间，只创建一个 GameStats 实例，但每当玩家开始新游戏时，都需要重置一些统计信息。为此，在 reset_stats() 方法中初始化大部分统计信息，而不是在**init**() 中直接初始化。然后在 **init**() 中调用这个方法，这样在创建 GameStats 实例时将妥善地设置这些统计信息。在玩家开始新游戏时，也能调用 reset_stats()。

从 Python 标准库的模块 time 中导入 sleep() 函数，以便能够在飞船被外星人撞到后让游戏暂停一会儿。此外，还导入了 GameStats。

在 alien_invasion.py 中增加统计信息的初始化和更新

```python
def __init__(self):
    --snip--
    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    # 创建一个统计信息
    self.game_stats = GameStats(self)
    --snip--
```

当有外星人撞到飞船时，将余下的飞船数减 1，创建一个新的外星舰队，并将飞船重新放在屏幕底部的中央。另外，让游戏暂停一会儿，让玩家意识到发生了碰撞，并在创建新的外星舰队前重整旗鼓。

```python alien_invasion.py

```

同时新增外星舰队与飞船碰撞的响应

```python
    def __update_aliens(self):
        # """更新外星人的坐标，并且检测外星人舰队是否触碰边缘，如果触碰需要修改舰队的移动方向和位置"""
        self.__check_fleet_edges()
        self.aliens.update()
        # 检查是否存在外星人与飞船发生碰撞的
        if sprite.spritecollideany(self.ship, self.aliens):
            self.__ship_hit()

    def __ship_hit(self):
        # 将 ship_left 减 1
        self.game_stats.ships_left -= 1

        # 清空外星舰队和子弹
        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()
        # 暂停 0.5秒
        sleep(0.5)
```

给 Ship 类新增一个 `center_ship()` 方法用于重置飞船的默认位置

```python Ship.py
class Ship:
    --snip--

    def center_ship(self):
        """将飞船重置到屏幕底部中央"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
```

#### 13.6.3 外星人到达屏幕下边缘

如果有外星人到达屏幕的下边缘，游戏应该像有外星人撞到飞船那样做出响应。我们新增检测外星人与屏幕下方碰撞的检测方法：

```python
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
```

#### 13.6.4 游戏结束

现在这个游戏看起来更完整了，但它永远都不会结束 —ships_left 只会不断地变成越来越小的负数。下面添加标志 game_active，以便在玩家的飞船用完后结束游戏。

```python
def __init__(self):
    --snip--
    # 游戏启动后处于活跃状态
    self.game_active = True
```

在更新外星人舰队中判断是否存在碰撞，包括飞船碰撞、屏幕底部碰撞，如果发生碰撞则对飞船数量减一。

```python
def __ship_hit(self):
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
```

### 13.7 确定应运行游戏的哪些部分

我们需要确定游戏的哪些部分在所有情况下都应运行，哪些部分仅在游戏处于活动状态时才运行:

```python alien_invasion.py
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
```
