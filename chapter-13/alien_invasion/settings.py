class Settings:
    """模拟设置参数"""

    def __init__(self):
        """初始化设置参数"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置，三艘飞船
        self.ship_limit = 3
        self.ship_speed = 1.5

        # 子弹设置
        # 子弹的移动速度
        self.bullet_speed = 2.5
        # 子弹的宽度
        self.bullet_width = 3
        # 子弹的高度
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
        # 每次最多只能发射三发子弹
        self.bullets_allowed = 3

        # 外星舰队移动的速度
        self.alien_speed = 5.0
        # 外星舰队移动方向标识，1 表示向右移动， -1 表示向左移动 
        self.fleet_direction = 1
        # 外星人舰队触碰边缘之后想下移动速度
        self.fleet_drop_speed = 10