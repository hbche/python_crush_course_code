## 第 12 章 武装飞船

本章开始使用 `pygame` 模块开发《外星人入侵》的游戏。

### 12.1 规划项目

### 12.2 安装 pygame

通过如下命令行安装：

```bash
python -m pip install --user pygame
```

运行结果：

```bash
Collecting pygame
  Downloading pygame-2.6.1-cp313-cp313-win_amd64.whl.metadata (13 kB)
Downloading pygame-2.6.1-cp313-cp313-win_amd64.whl (10.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 5.8 MB/s  0:00:02
Installing collected packages: pygame
Successfully installed pygame-2.6.1
```

### 12.3 开始游戏项目

#### 12.3.1 创建 pygame 窗口及响应用户输入

```python alien_invasion.py
import pygame
import sys

class AlienInvasion:
    """模拟外星人入侵游戏"""

    def __init__(self):
        """初始化"""

        # 初始化游戏并创建资源
        pygame.init()
        # 创建空白屏幕，pygame.display.set_mode方法的参数是一个表示屏幕宽高的元组
        self.screen = pygame.display.set_mode((1200, 800))
        # 设置标题
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            # 监听键盘和鼠标点击事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

调用 `pygame.init()` 初始化背景设置，让 Pygame 能够正常的工作。再调用 `pygame.display.set_mode()` 来创建一个显示窗口，游戏的所有元素都在其中绘制。实参 `(1200, 800)` 是一个元组，指定了游戏窗口的尺寸，宽是 1200 像素，高度是 800 像素，可根据自己屏幕的实际尺寸进行调整。后续所有绘制都是在这个显示窗口上绘制，所以我们需要将这个实例存起来 `self.screen = pygame.display.set_mode((1200, 800))`，方便后续方法调用是访问。

最后声明一个 `run_game` 的方法，使得外部能够通过调用该方法来启动游戏。该方法包含一个 while 循环，而这个循环包含事件监听和屏幕更新的代码。为了访问事件，我们使用了函数 `pygame.event.get()`。这个函数返回一个列表，其中包含上一次被调用后发生的所有事件。在每个循环中，我们处理用户的按鼠标和键盘事件，通过 if 判断特定事件。例如当用户点击游戏窗口的关闭按钮时，将检测到 `pygame.QUIT`事件，进而调用 `sys.exit()`来退出游戏。

调用 `pygame.display.flip()`方法让最近绘制的屏幕可见。在这里，它在每次执行 while 循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。我们移动游戏元素时，`pygame.display.flip()` 将不断更新屏幕，以显示元素的新位置，并且在原来的位置隐藏元素，从而营造平滑移动的效果。

#### 12.3.2 设置背景色

```python
import pygame
import sys

class AlienInvasion:
    """模拟外星人入侵游戏"""

    def __init__(self):
        """初始化"""

        # 初始化游戏并创建资源
        pygame.init()
        # 创建空白屏幕，pygame.display.set_mode方法的参数是一个表示屏幕宽高的元组
        self.screen = pygame.display.set_mode((1200, 800))
        # 设置标题
        pygame.display.set_caption("Alien Invasion")
        # 设置背景色
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            # 监听键盘和鼠标点击事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

### 12.3.3 创建设置类

每次给游戏添加新功能时，通常也将引入一些新设置。下面来编写一个名为 settings 的模块，在其中包含一个名为 Settings 的类，用于将所有设置都存储在一个地方，以免在代码中到处添加设置。这样，每当需要访问设置时，只需使用一个设置对象。另外，在项目增大时，这使得修改游戏的外观和行为更容易：要修改游戏，只需修改（接下来将创建的）settings.py 中的一些值，而无须查找散布在项目中的各种设置。

```python settings.py
class Settings:
    """模拟设置参数"""

    def __init__(self):
        """初始化设置参数"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```

alien_invasion.py 文件中涉及配置的地方改为从 settings 实例中取：

```python alien_invasion.py
import pygame
import sys
from settings import Settings

class AlienInvasion:
    """模拟外星人入侵游戏"""

    def __init__(self):
        """初始化"""

        # 初始化游戏并创建资源
        pygame.init()
        self.settings = Settings()
        # 创建空白屏幕，pygame.display.set_mode方法的参数是一个表示屏幕宽高的元组
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置标题
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            # 监听键盘和鼠标点击事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

### 12.4 添加飞船图像

在游戏中几乎可以使用任何类型的图像文件，但使用位图（.bmp）文件最为简单，因为 Pygame 默认加载位图。虽然可配置 Pygame 以使用其他文件类型，但有些文件类型要求你在计算机上安装相应的图像库。

选择图像时，要特别注意背景色。请尽可能选择背景为透明或纯色的图像，便于使用图像编辑器将其背景替换为任意颜色。图像的背景色与游戏的背景色匹配时，游戏看起来最漂亮。你也可以将游戏的背景色设置成图像的背景色。

#### 12.4.1 创建 Ship 类

```python ship.py
import pygame

class Ship:
    """模拟飞船"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取图像的外接矩形
        self.image = pygame.image.load('E:\python_crush_course_code\\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船都放在屏幕底部中间
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """将飞船绘制到游戏窗口上"""

        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
```

Pygame 之所以高效，是因为它让你能够像处理矩形（rect 对象）一样处理所有的游戏元素，即便其形状并非矩形。像处理矩形一样处理游戏元素之所以高效，是因为矩形是简单的几何形状。例如，通过将游戏元素视为矩形，Pygame 能够更快地判断出它们是否发生了碰撞。这种做法的效果通常很好，游戏玩家几乎注意不到我们处理的并不是游戏元素的实际形状。在这个类中，我们将把飞船和屏幕作为矩形进行处理。

我们可以调用 `pygame.image.load()` 来加载我们的飞船资源，该函数返回一个表示飞船的 surfac，我们将其存在 `self.image` 属性中。之后我们可以调用 `self.image.get_rect()` 来获取飞船图片的外接矩形，后面我们可以通过该属性指定飞船的位置。

> 注意：在 Pygame 中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。在 1200 × 800 的屏幕上，原点位于左上角，而右下角的坐标为(1200,800)。这些坐标对应的是游戏窗口，而不是物理屏幕。

最后我们通过定义 `blitme` 方法将飞船图片绘制在游戏窗口的指定位置。

#### 12.4.2 在屏幕上绘制飞船

修改 alien_invasion.py 程序，初始化 ship 实例，在循环绘制时调用 `ship.blitme()` 绘制飞船

```python
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

    def run_game(self):
        """开始游戏的主循环"""

        while True:
            # 监听键盘和鼠标点击事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)

            # 调用飞船实例的 blitme() 方法，在游戏窗口上绘制飞船
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

### 12.5 重构: \_check_events()方法和\_update_screen()方法

我们优化 `run_game` 方法，将其逻辑进行分类，可分为事件检测和屏幕更新两部分，所有我们将对应逻辑抽取成两个方法。

在 python 中辅助方法的名称一般使用下划线打头。

```python
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

    def __update_screen(self):
        """更新屏幕上的元素，并绘制到游戏窗口上"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 调用飞船实例的 blitme() 方法，在游戏窗口上绘制飞船
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

#### 12.5.1 \_check_events() 方法

#### 12.5.2 \_update_screen() 方法

### 12.6 驾驶飞船

实现通过按键移动飞船。

#### 12.6.1 响应按键

更新事件检测

```python
def __check_events(self):
    """事件检测"""

    # 监听键盘和鼠标点击事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.rect.x += 1
            elif event.key == pygame.K_LEFT:
                self.ship.rect.x -= 1
```

#### 12.6.2 允许持续移动

我们发现无法响应按键持续按下的事件，即持续按下左右键时，发现飞船只移动了一像素。我们做如下优化：

修改 Ship 类，增加移动标识、移动速度、飞船 x 坐标和更新坐标函数

```python ship.py
import pygame

class Ship:
    """模拟飞船"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取图像的外接矩形
        self.image = pygame.image.load('E:\python_crush_course_code\\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船都放在屏幕底部中间
        self.rect.midbottom = self.screen_rect.midbottom

        # 增加飞船移动标识
        self.moving_right = False
        self.moving_left = False
        # 飞船的移动速度
        self.ship_speed = 1.5
        # 存储飞船x坐标，存在小数值
        self.x = float(self.rect.x)

    def update(self):
        """限制飞船的移动范围，限制在游戏窗口范围内，根据移动速度和移动标识更新飞船的位置"""

        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed

        # 根据self.x 更新 self.rect
        self.rect.x = self.x

    def blitme(self):
        """将飞船绘制到游戏窗口上"""

        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
```

更新 alien_invasion.py 程序：

```python
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
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
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

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

#### 12.6.3 左右移动

#### 12.6.4 调整飞船的速度

#### 12.6.5 限制飞船的活动范围

#### 12.6.6 重构 \_check_events() 方法

我们发现，`__check_events()` 方法逻辑可以分类，我们对该方法进行优化拆分：

```python

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

    def __check_keyup_events(self, event):
        """检测按键松开事件"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
```

#### 12.6.7 按键 Q 退出

优化 `__check_keydown_events()` 方法中检测按下 Q 键退出游戏。注意输入法。注意按键 Q 对应 `pygame.K_q`。

```python
    def __check_keydown_events(self, event):
        """检测按键按下事件"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
```

#### 12.6.8 控制帧率

我们发现目前控制飞船移动存在一个问题，每次循环内，我们持续触发 `ship.update` 方法去更新飞船坐标，在重新绘制时发现飞船在一个循环内移动了很多单位。

此时我们需要控制循环内更新飞船的频次。

理想情况下，游戏在所有的系统中都应以相同的速度（帧率）运行。对于可在多种系统中运⾏的游戏，控制帧率是个复杂的问题，好在 Pygame 提供了一种相对简单的方式来达成这个目标。我们将创建一个时钟（clock）​，并确保它在主循环每次通过后都进⾏计时（tick）​。当这个循环的通过速度超过我们定义的帧率时，Pygame 会计算需要暂停多长时间，以便游戏的运⾏速度保持一致。

初始化 pygame 后，创建 pygame.time 模块中的 Clock 类的一个实例，然后在 run_game() 的 while 循环末尾让这个时钟进行计时：

```python
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
```

#### 12.6.8 在全屏模式下运行游戏

### 12.7 简单回顾

### 12.8 射击

添加射击功能。

#### 12.8.1 添加子弹设置

在 seeings.py 文件中增加子弹设置参数：

```python
class Settings:
    """模拟设置参数"""

    def __init__(self):
        """初始化设置参数"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        # 子弹的移动速度
        self.bullet_speed = 2.0
        # 子弹的宽度
        self.bullet_width = 3
        # 子弹的高度
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
```

#### 12.8.2 创建 Bullet 类

定义子弹类：

```python bullet.py
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
```

#### 12.8.3 将子弹存储在编组中

更新 alien_invasion.py 程序，给添加子弹编组存储发射的子弹，在时间监听中监听按键发射子弹，在更新函数中更新子弹位置，绘制子弹。

```python alien_invasion.py
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
            # 增加子弹
            new_bullet = Bullet(self)
            # 向子弹分组中添加新加的子弹
            self.bullets.add(new_bullet)
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

        # 更新子弹的位置，调用分组的update方法，该方法会调用元组内部所有子弹的update方法更新每个子弹自身的位置
        self.bullets.update()
        # 遍历子弹分组，绘制每个子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

#### 12.8.4 开火

优化逻辑，将新增子弹的逻辑抽取成 \_\_fire_bullet() 方法，在 \_\_check_events() 方法中调用

```python
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


    def __update_screen(self):
        """更新屏幕"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 更新飞船的位置
        self.ship.update()
        # 调用飞船实例的 blitme() 方法，在游戏窗口上绘制飞船
        self.ship.blitme()

        # 更新子弹的位置，调用分组的update方法，该方法会调用元组内部所有子弹的update方法更新每个子弹自身的位置
        self.bullets.update()
        # 遍历子弹分组，绘制每个子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

#### 12.8.5 删除消失的子弹

当前，虽然子弹会在抵达屏幕上边缘后消失，但这仅仅是因为 Pygame 无法在屏幕外绘制它们。这些子弹实际上依然存在，它们的 y 坐标为负数且越来越小。这是个问题，因为它们将继续消耗系统的内存和处理能力。

我们需要将这些已消失的子弹删除，否则游戏所做的无谓工作将越来越多，进而变得越来越慢。为此，需要检测表示子弹的 rect 的 bottom 属性是否为零。如果是，就表明子弹已飞过屏幕上边缘：

```python
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


    def __update_screen(self):
        """更新屏幕"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 更新飞船的位置
        self.ship.update()
        # 调用飞船实例的 blitme() 方法，在游戏窗口上绘制飞船
        self.ship.blitme()

        # 更新子弹的位置，调用分组的update方法，该方法会调用元组内部所有子弹的update方法更新每个子弹自身的位置
        self.bullets.update()

        # 移除消失在屏幕外的子弹
        for bullet in self.bullets.copy():
            if bullet.y <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        # 遍历子弹分组，绘制每个子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

#### 12.8.6 限制子弹数量

更新 Setting 类，增加子弹数量限制

```python
class Settings:
    """模拟设置参数"""

    def __init__(self):
        """初始化设置参数"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        # 子弹的移动速度
        self.bullet_speed = 2.0
        # 子弹的宽度
        self.bullet_width = 3
        # 子弹的高度
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
        # 每次最多只能发射三发子弹
        self.bullets_allowed = 3
```

抽取更新子弹的逻辑到 \_\_update_bullets() 方法中：

```python
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
```
