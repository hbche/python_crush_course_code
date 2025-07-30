# 练习9.4：就餐人数　在为练习9.1编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例。
# 打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印。
# 添加一个名为set_number_served()的方法，用来设置就餐人数。
# 调用这个方法并向它传递新的就餐人数，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，用来让就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

# class Restaurant:
#     """模拟一个餐厅"""


#     def __init__(self, restaurant_name, cuisine_type, desc):
#         """初始化餐厅属性，餐厅名称、烹饪风格、desc"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.desc = desc
#         # 就餐人数，默认为 0
#         self.number_served =  0


#     def get_restaurant_desc(self):
#         print(f"{self.restaurant_name.title()} is {self.cuisine_type} reataurant.")
#         print(f"{self.desc}")


#     def describe_number_served(self):
#         """打印在这个餐厅就餐过的人数"""
#         print(f"This restaurant has served {self.number_served} customers.")


#     def set_number_served(self, number_served):
#         """更新就餐历史人数"""
#         if number_served >= self.number_served:
#             self.number_served = number_served
#         else:
#             print("You can't roll back the number served.")

        
#     def increment_number_served(self, increment_num):
#         if increment_num >= 0:
#             self.number_served += increment_num
#         else:
#             print("You can't roll back the number served.")


# restaurant = Restaurant('Quanjude', 'Chinese Roast Duck Cuisine（中式烤鸭料理）', '全聚德是北京极具代表性的老字号餐厅，创立于1864年，在国内外都享有盛誉。')
# restaurant.get_restaurant_desc()
# restaurant.describe_number_served()
# restaurant.set_number_served(100_000)
# restaurant.describe_number_served()
# restaurant.increment_number_served(100)
# restaurant.describe_number_served()

# 练习9.5：尝试登录次数　在为练习9.3编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，用来将属性login_attempts的值加1。
# 再编写一个名为reset_login_attempts()的方法，用来将属性login_attempts的值重置为0。
# 根据User类创建一个实例，再调用increment_login_attempts()方法多次。
# 打印属性login_attempts的值，确认它正确地递增了。
# 然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。

class User:
    """模拟用户登录信息"""


    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    
    def describe_login_attempts(self):
        print(f"You have attempted to log in {self.login_attempts} times.")


    def increment_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    
    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('Robin', 'Che', 0)
user.describe_login_attempts()
user.increment_login_attempts(10)
user.describe_login_attempts()
user.reset_login_attempts()
user.describe_login_attempts()