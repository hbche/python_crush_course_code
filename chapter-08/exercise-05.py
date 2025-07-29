# 练习8.12：三明治　编写一个函数，它接受顾客要在三明治中添加的一系列食材。
# 这个函数只有一个形参（它收集函数调用中提供的所有食材）​，并打印一条消息，对顾客点的三明治进行概述。
# 调用这个函数三次，每次都提供不同数量的实参。
# def make_sandwich(*toppings):
#     print("\nMake a sandwich with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_sandwich('Ham', 'Tomato Slices', 'Cheese', 'Butter Toast') # 火腿、番茄片、奶酪、黄油面包
# make_sandwich('Mashed Avocado', 'Tomato Slices', 'Red Bell Pepper Strips') # 牛油果泥、番茄片、红椒丝

# 练习8.13：用户简介　复制前面的程序user_profile.py，在其中调用build_profile()来创建有关你的简介。
# 在调用这个函数时，指定你的名和姓，以及三个用来描述你的键值对。
# def build_profile(first, last, **user_profile):
#     user_profile['first_name'] = first
#     user_profile['last_name'] = last
#     return user_profile
# user_profile = build_profile('Robin', 'Che', location="Wuhan", street='Yangjiawan', age=29)
# print(user_profile)

# 练习8.14：汽车　编写一个函数，将一辆汽车的信息存储在字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 在调用这个函数时，提供必不可少的信息，以及两个名值对，如颜色和选装配件。
# 这个函数必须能够像下面这样调用：
# car = make_car('subaru', 'outback', color='blue', two_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
def make_car(manufacture, model, **car_info):
    car_info['manufacture'] = manufacture
    car_info['model'] = model
    return car_info
car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)


