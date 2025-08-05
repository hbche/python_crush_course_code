class Settings:
    """模拟游戏的设置参数"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕尺寸设置
        self.screen_width = 1200
        self.screen_height = 800
        # 背景色设置
        self.bg_color = (135, 206, 235)
        # 飞船移动速度
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 2.0
        # 子弹的宽度
        self.bullet_width = 3
        # 子弹的高度
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)

    