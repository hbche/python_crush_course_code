# 练习9.1：餐馆　创建一个名为Restaurant的类，为其__init__()方法设置两个属性：restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type


#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} is {self.cuisine_type}")


#     def open_restaurant(self):
#         print(f"Restaurant is open now.")

    
# restaurant = Restaurant('Beijing Big Restaurant', 'Chinses food')
# print(f"The name of restaurant is: {restaurant.restaurant_name}, cuisine type is {restaurant.cuisine_type}.")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 练习9.2：三家餐馆　根据为练习9.1编写的类创建三个实例，并对每个实例调用describe_restaurant()方法。

# restaurant_01 = Restaurant('黄鹤楼酒店', '湖北菜')
# restaurant_02 = Restaurant('成都大酒店', '川菜')
# restaurant_03 = Restaurant('山东大酒店', '鲁菜')
# restaurant_01.describe_restaurant()
# restaurant_02.describe_restaurant()
# restaurant_03.describe_restaurant()

# 练习9.3：用户　创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介中通常会有的其他几个属性。
# 在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
# 再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    
    def describe_user(self):
        print(f"Fullname is {self.first_name.title()} {self.last_name.title()}.")

    
    def greet_user(self):
        print(f"Hello, {self.first_name}!")


user_01 = User('Lucy', 'Green')
user_01.describe_user()
user_02 = User('Sam', 'Alt')
user_02.describe_user()