# Python 编程: 从入门到实践代码

记录阅读《Python 编程: 从入门到实践代码》时的示例和练习的代码

## 第三章

## 第四章

## 第五章

## 第六章

## 第七章 [用户输入和 while 循环](./chapter-07/index.md)

## 第八章 [函数](./chapter-08/index.md)

## 第九章 [类](./chapter-09/index.md)

## 第十章 [文件和异常](./chapter-10/index.md)

## 第十一章 [测试代码](./chapter-11/index.md)

## 第十二章 [武装飞船](./chapter-12/index.md)

Pygame api

1. `pygame.init()`: 初始化 pygame
2. `pygame.display.set_mode((width, height))`: 根据制定尺寸生成屏幕，并返回表示
   游戏屏幕的 surface 实例
3. `pygame.event.get()`: 获取 pygame 的事件列表
4. `pygame.time.Clock()`: 创建 pygame 的时钟实例，用于控制循环的刷新帧率
5. `clock.tick(fps)`: 调用 Clock 实例上的 tick 放饭可以控制循环执行的帧率，该方
   法的参数是一个表示帧率的参数，比如 60，表示每秒执行 60 次循环
6. `screen.fill()`: 游戏屏幕默认是黑色背景，可以调用表示屏幕的 surface 实例上的
   fill 方法填充屏幕颜色，参数是一个 RGB 颜色格式的元组，例如
   `screen.fill((230, 230, 230))`
7. `screen.get_rect()`: 获取屏幕的外接矩形，其中存储的坐标和尺寸
8. `pygame.display.flip()`: 重绘屏幕
9. `pygame.image.load(path)`: 将指定路径的文件加载为图片 surface
10. `screen.blit(surface, rect)`: 在屏幕上指定位置绘制 surface。例如在屏幕上绘制
    飞船 `screen.bilt(self.ship, self.ship.get_rect())`
11. `pygame.Rect(x, y, width, height)`: 在指定位置生成指定宽高的 React 矩形
12. `pygame.draw.rect(screen, color, rect)`: 在指定屏幕 screen 上以指定的背景色
    绘制指定的 rect 矩形
13. `pygame.sprite.Group()`: 创建精灵编组，用于存储 Sprite 类的实例。我们游戏中
    的子弹类 Bullet 就是继承自 Sprite 类的
14. `group.update()`: group 是 `pygame.sprite.Group` 实例，调用该编组的 update
    方法，将自动调用其内部每个数据项的 update 方法。比如游戏中更新子弹的位置，直
    接调用子弹编组的 update 即可对每个子弹更新
15. `group.remove(item)`: 从 group 编组中移除 item 子项。本游戏中
    `bullets.remove(current_bullet)` 从子弹编组中移除飞到屏幕边缘外的子弹。
16. `group.draw(screen)`: 将指定分组绘制到 screen 屏幕上。游戏中用于在屏幕上绘制
    外星人舰队 `self.aliens.draw(self.screen)`

## 第十三章 [外星人](./chapter-13/index.md)

Pygame API

1. `pygame.sprite.groupcollide(group1, group2, True, True)`: 检测编组 1 与编组 2
   之间是否存在碰撞。游戏中用于检测子弹编组与外星人舰队编组是否存在碰撞，如果发
   生碰撞，将发生碰撞的元素从各自的编组中移除。返回存在碰撞的字典，key 是编组 1
   中的元素，value 是编组 2 中的元素
2. `pygame.sprite.spritecollideany(sprite, group)`: 用于检测精灵 sprite 与精灵编
   组 group 是否存在碰撞。游戏中用于检测飞船与外星人舰队之间是否存在碰撞。

## 第十八章 [Django 入门](./chapter-18/index.md)
