# 从 car 模块中导入 Car 类
from car import Car

class Battery:
    """模拟电动车电池"""


    def __init__(self, battery_size = 40):
        """初始化电池的属性"""
        self.battery_size = battery_size

    
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        if self.battery_size == 40:
            range = 150
        if self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """模拟一辆电动汽车"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 添加电动汽车特有的属性
        self.battery = Battery()


    def fill_gas_tank(self):
        """重写父类的方法，电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")