class Car:
    """一次模拟燃油汽车的简单尝试"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 里程
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")
    

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值，禁止将里程数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increase_odometer(self, miles):
        """让里程表读数增加指定的量"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")



class Battery:
    """一次模拟电池的简单尝试"""
    
    
    def __init__(self, battery_size=40):
        """初始化电池的信息"""
        self.battery_size = battery_size
        
    
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"The car has {self.battery_size}-kWh battery.")
        
        
    def get_range(self):
        """打印一条描述电池续航里程的消息"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
        
        
class ElectricCar(Car):
    """一次对电动汽车的简单模拟"""
    
    
    def __init__(self, make, model, year):
        """先初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
