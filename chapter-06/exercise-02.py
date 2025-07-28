# 练习6.4：词汇表2　现在你知道了如何遍历字典，请整理你为练习6.3编写的代码，将其中的一系列函数调用print()替换为一个遍历字典中键和值的循环。确保该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
# word_list = {
#     '==': 'equality operator: returns True if the values of two operands are equal',
#     'in': 'membership operator: returns True if a value is found in a sequence (string, list, tuple, dict, set, etc.)',
#     'not in': 'negated membership operator: returns True if a value is NOT found in a sequence',
#     'and': 'logical AND operator: returns True only if both operands are truthy',
#     'or' : 'logical OR operator: returns True if at least one operand is truthy'
# }
# for op in word_list.keys():
#     print(f"The mean of '{op}' is: {word_list[op]}")

# 练习6.5：河流　创建一个字典，在其中存储三条河流及其流经的国家。例如，一个键值对可能是'nile': 'egypt'。
# • 使用循环为每条河流打印一条消息，如下所示。The Nile runs through Egypt.
# • 使用循环将该字典中每条河流的名字打印出来。
# • 使用循环将该字典包含的每个国家的名字打印出来。
# rivers = {
#     'Amazon': 'Brazil',      # 亚马孙河流经巴西
#     'Nile': 'Egypt',         # 尼罗河流经埃及
#     'Yangtze': 'China'       # 长江流经中国
# }
# for river, country in rivers.items():
#     print(f"The {river} runs through {country}")
# for river in rivers.keys():
#     print(river)
# for country in set(rivers.values()):
#     print(country)

# 练习6.6：调查　在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# • 创建一个应该会接受调查的人的名单，其中有些人已在字典中，而其他人不在字典中。
# • 遍历这个名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条邀请参加调查的消息。
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }
# current_users = favorite_languages.keys()
# users = ['sarah', 'phil', 'tom', 'alice']
# for user in users:
#     if user in current_users:
#         print(f'Thank you, {user.title()}')
#     else:
#         print(f"Hi {user.title()}, would you want to join?")
