# 练习5.8：以特殊方式跟管理员打招呼　创建一个至少包含5个用户名的列表，并且其中一个用户名为'admin'。想象你要编写代码，在每个用户登录网站后都打印一条问候消息。遍历用户名列表，向每个用户打印一条问候消息。
# • 如果用户名为'admin'，就打印一条特殊的问候消息，如下所示。Hello admin, would you like to see a status report?
# • 否则，打印一条普通的问候消息，如下所示。Hello Jaden, thank you for logging in again.


# users = ['admin', 'tom', 'alice', 'bob', 'jack']
# for user in users:
#     if user == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {user.title()}, thank you for logging in again.")

# 练习5.9：处理没有用户的情形　在为练习5.8编写的程序中，添加一条if语句，检查用户名列表是否为空。
# • 如果为空，就打印如下消息。We need to find some users!
# • 删除列表中的所有用户名，确认将打印正确的消息。

# # users = ['admin', 'tom', 'alice', 'bob', 'jack']
# users = []
# if users:
#     for user in users:
#         if user == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print(f"Hello {user.title()}, thank you for logging in again.")
# else:
#     print("We need to find some users!")

# 练习5.10：检查用户名　按照下面的说明编写一个程序，模拟网站如何确保每个用户的用户名都独一无二。
# • 创建一个至少包含5个用户名的列表，并将其命名为current_users。
# • 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也在列表current_users中。
# • 遍历列表new_users，检查其中的每个用户名是否已被使用。如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
# • 确保比较时不区分大小写。换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。​（为此，需要创建列表current_users的副本，其中包含当前所有用户名的全小写版本。​）

# current_users = ['Admin', 'tom', 'alice', 'bob', 'jack']
# # 使用列表推导式将 current_users 转换成对应的全小写列表
# current_users = [user.lower() for user in current_users]
# new_users = ['TOM', 'jackson', 'Alice', 'lucy', 'lulu']

# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(f"The username {new_user} is already in use, please change it to a different username.")
#     else:
#         print(f"{new_user}, the username is not used.")


# 练习5.11：序数　序数表示顺序位置，如1st和2nd。序数大多以th结尾，只有1st、2nd、3rd例外。
# • 在一个列表中存储数字1～9。• 遍历这个列表。
# • 在循环中使用一个if-elif-else结构，打印每个数字对应的序数。输出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"，每个序数都独占一行。

# order_list = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
order_list = list(range(1, 10))
for order in order_list:
    if order == 1:
        print('1st')
    elif order == 2:
        print('2nd')
    elif order == 3:
        print('3rd')
    else:
        print(f"{order}th")