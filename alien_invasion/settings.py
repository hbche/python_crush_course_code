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