# 练习7.4：比萨配料　编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，指出要在比萨中添加这种配料。
# prompt = "Please input your toppings:"
# prompt += "\nEnter 'quit' when you are finished."
# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(f"\tAdd {topping} to pizza.")

# 练习7.5：电影票　有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3（含）～12岁的观众收费10美元；年满12岁的观众收费15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
# prompt = "Please input your age:"
# prompt += "\nEnter 'quit' when you are finished."
# while True:
#     age = input(prompt)
#     if age != 'quit':
#         age = int(age)
#         if age < 3:
#             print("Your cost is $0.")
#         elif age < 12:
#             print("Your cost is $10.")
#         elif age >= 12:
#             print("Your cost is $ 15.")
#     else:
#         break
    

# 练习7.6：三种出路　以不同的方式完成练习7.4或练习7.5，在程序中采取如下做法。
# • 在while循环中使用条件测试来结束循环。
# • 使用变量active来控制循环结束的时机。
# • 使用break语句在用户输入'quit'时退出循环。

# prompt = "Please input your age:"
# prompt += "\nEnter 'quit' when you are finished."
# age = ''
# while age != 'quit':
#     age = input(prompt)
#     realy_age = int(age)
#     if realy_age < 3:
#         print("Your cost is $0.")
#     elif realy_age < 12:
#         print("Your cost is $10.")
#     elif realy_age >= 12:
#         print("Your cost is $ 15.")

# prompt = "Please input your age:"
# prompt += "\nEnter 'quit' when you are finished."
# active = True
# while active:
#     age = input(prompt)
#     if age != 'quit':
#         age = int(age)
#         if age < 3:
#             print("Your cost is $0.")
#         elif age < 12:
#             print("Your cost is $10.")
#         elif age >= 12:
#             print("Your cost is $ 15.")
#     else:
#         active = False

# 练习7.7：无限循环　编写一个没完没了的循环，并运行它。​（要结束该循环，可按Ctrl + C，也可关闭显示输出的窗口。​）