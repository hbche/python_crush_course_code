# 练习4.10：切片　选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
# • 打印消息“The first three items in the list are:”​，再使用切片来打印列表的前三个元素。
# • 打印消息“Three items from the middle of the list are:”​，再使用切片来打印列表中间的三个元素。
# • 打印消息“The last three items in the list are:”​，再使用切片来打印列表末尾的三个元素。

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple' ]

# print(f"The first three items in the list are: {available_toppings[:3]}")
# print(f"Three items from the middle of the list are: {available_toppings[2:5]}")
# print(f"The last three items in the list are: {available_toppings[-3:]}")


# 练习4.11：你的比萨，我的比萨　在你为练习4.1编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas，再完成如下任务。
# • 在原来的比萨列表中添加一种比萨。
# • 在列表friend_pizzas中添加另一种比萨。
# • 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”​，再使用一个for循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”​，再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。

# my_pizzas = []
# friend_pizzas = my_pizzas[:]


# 练习4.12：使用多个循环　在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印列表。请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表都打印出来。