# 练习5.3：外星人颜色1　假设玩家在游戏中消灭了一个外星人，请创建一个名为alien_color的变量，并将其赋值为'green'、'yellow'或'red'。
# • 编写一条if语句，测试外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分。
# • 编写这个程序的两个版本，上述条件测试在其中的一个版本中通过，在另一个版本中未通过（未通过条件测试时没有输出）​。
# alien_color = 'red'
# if alien_color == 'green':
#     print("You get 5")
# elif alien_color == 'yellow':
#     print("You get 10")
# elif alien_color == 'red':
#     print("You get 15")

# 练习5.4：外星人颜色2　像练习5.3那样设置外星人的颜色，并编写一个if-else结构。
# • 如果外星人是绿色的，就打印一条消息，指出玩家因消灭该外星人获得了5分。
# • 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。
# • 编写这个程序的两个版本，在一个版本中将执行if代码块，在另一个版本中将执行else代码块。

# 练习5.5：外星人颜色3　将练习5.4中的if-else结构改为if-elif-else结构。
# • 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
# • 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
# • 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
# • 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。

# 练习5.6：人生的不同阶段　设置变量age的值，再编写一个if-elif-else结构，根据age的值判断这个人处于人生的哪个阶段。
# • 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
# • 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
# • 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
# • 如果年龄为13（含）～18岁，就打印一条消息，指出这个人是少年。
# • 如果年龄为18（含）～65岁，就打印一条消息，指出这个人是中青年人。
# • 如果年龄达到65岁，就打印一条消息，指出这个人是老年人。

# age = 29
# if age < 2:
#     age_type = 'infant'
# elif age < 4:
#     age_type = 'toddler'
# elif age < 13:
#     age_type = 'child'
# elif age < 18:
#     age_type = 'juvenile'
# elif age < 65:
#     age_type = 'middle-age and young'
# elif age >= 65:
#     age_type = 'old age'
# print(f"You are {age_type}.")

# 练习5.7：喜欢的水果　创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if语句，检查列表中是否包含特定的水果。
# • 将该列表命名为favorite_fruits，并让其包含三种水果。
# • 编写5条if语句，每条都检查某种水果是否在列表中。如果是，就打印一条像下面这样的消息。You really like bananas!

favorite_fruits = ['apple', 'banana', 'pear', 'watermelon', 'lichee', 'peach']
if 'banana' in favorite_fruits:
    print("You really like banana!")
if 'watermelon' in favorite_fruits:
    print(f"You really like {'watermelon'}!")
if 'lichee' in favorite_fruits:
    print("You really like lichee!")