# 练习9.6：冰激凌小店　冰激凌小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand的类，让它继承你为练习9.1或练习9.4编写的Restaurant类。
# 这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。
# 编写一个显示这些冰激凌口味的方法。创建一个IceCreamStand实例，并调用这个方法。

# class Restaurant:
#     """模拟一个餐饮店"""


#     def __init__(self, restaurant_name, cuisine_type):
#         """初始化餐饮店的属性"""
#         self.restaurant_name = restaurant_name
#         self.cusine_type = cuisine_type
#         self.number_served = 0

#     def get_number_served(self):
#         print(f"This restaurant served about {self.number_served} people every!")

    
#     def set_number_served(self, number_served):
#         self.set_number_served = number_served


# class IceCreamStand(Restaurant):

#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['Vanilla', 'Mint Chocolate Chip', 'Tiramisu']


#     def describe_flavors(self):
#         print(f"This ice cream stand has {len(self.flavors)} flavors:")
#         for flavor in self.flavors:
#             print(f"-{flavor}")


# ice_cream_stand = IceCreamStand('Mixue Ice Cream & Tea', 'Fast - food style drinks and desserts')
# ice_cream_stand.describe_flavors()

# 练习9.7：管理员　管理员是一种特殊的用户。
# 编写一个名为Admin的类，让它继承你为练习9.3或练习9.5完成编写的User类。
# 添加一个名为privileges的属性，用来存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为show_privileges()的方法，显示管理员的权限。
# 创建一个Admin实例，并调用这个方法。

# class User:
#     """模拟一个用户类"""

#     def __init__(self, first_name, last_name):
#         """初始化用户信息"""
#         self.first_name = first_name
#         self.last_name = last_name

    
#     def get_full_name(self):
#         """打印一条消息展示用户全名"""
#         return f"{self.first_name} {self.last_name}"


# class Admin(User):
#     """模拟管理员用户"""


#     def __init__(self, first_name, last_name):
#         """初始化用户和管理员用户属性"""
#         super().__init__(first_name, last_name)
#         self.privileges = ['can add post', 'can delete post', 'can ban user']

    
#     def show_privileges(self):
#         """打印一条消息展示管理员用户拥有的权限"""
#         print(f"{self.get_full_name()} have some privileges:")
#         for privilege in self.privileges:
#             print(f"-{privilege}")


# admin = Admin('Robin', 'Che')
# admin.show_privileges()

# 练习9.8：权限　编写一个名为Privileges的类，它只有一个属性privileges，其中存储了练习9.7所述的字符串列表。
# 将方法show_privileges()移到这个类中。
# 在Admin类中，将一个Privileges实例用作其属性。
# 创建一个Admin实例，并使用方法show_privileges()来显示权限。
# class User:
#     """模拟一个用户类"""

#     def __init__(self, first_name, last_name):
#         """初始化用户信息"""
#         self.first_name = first_name
#         self.last_name = last_name

    
#     def get_full_name(self):
#         """打印一条消息展示用户全名"""
#         return f"{self.first_name} {self.last_name}"


# class Admin(User):
#     """模拟管理员用户"""


#     def __init__(self, first_name, last_name):
#         """初始化用户和管理员用户属性"""
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()

# class Privileges:
#     """模拟权限"""


#     def __init__(self):
#         """初始化权限信息"""
#         self.privileges = ['can add post', 'can delete post', 'can ban user']


#     def show_privileges(self):
#         print("Privileges: ")
#         for privilege in self.privileges:
#             print(f"-{privilege}")


# admin = Admin('Robin', 'Che')
# admin.privileges.show_privileges()

# 练习9.9：电池升级　在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。
# 这个方法检查电池容量，如果电池容量不足65，就设置为65。
# 创建一辆电池容量为默认值的电动汽车，调用方法get_range()，然后对电池进行升级，并再次调用get_range()。
# 你将看到这辆汽车的续航里程增加了。

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        if self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
class ElectricCar(Car):


    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

electric_car = ElectricCar('audi', 'a4', 2024)
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()