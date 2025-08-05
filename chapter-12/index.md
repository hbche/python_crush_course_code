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

#### 12.3.2 控制帧率

#### 12.3.3 设置背景色

### 12.4 添加飞船图像

#### 12.4.1 创建 Ship 类

### 12.5 重构: \_check_events()方法和\_update_screen()方法

在 python 中辅助方法的名称一般使用下划线打头。

#### 12.5.1 \_check_events() 方法

#### 12.5.2 \_update_screen() 方法

### 12.6 驾驶飞船

#### 12.6.1 响应按键

#### 12.6.2 允许持续移动

#### 12.6.3 左右移动

#### 12.6.4 调整飞船的速度

#### 12.6.5 限制飞船的活动范围

#### 12.6.6 重构 \_check_events() 方法

#### 12.6.7 按键 Q 退出

#### 12.6.8 在全屏模式下运行游戏

### 12.7 简单回顾

### 12.8 射击

#### 12.8.1 添加子弹设置

#### 12.8.2 创建 Bullet 类

#### 12.8.3 将子弹存储在编组中

#### 12.8.4 开火
