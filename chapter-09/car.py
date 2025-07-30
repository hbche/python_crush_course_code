class Car:
    """一次模拟汽车的简单尝试"""


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
