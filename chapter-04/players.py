players = ["charles", "martina", "michael", "florence", "eli"]
# # 取前三个元素
# print(players[0: 3])

# # 取2、3、4索引对应的元素
# print(players[1:4])

# # 如果没有指定第一个索引，Python将自动从第一个元素开始取。例如下面的切片对应的范围是第一个到第四个元素之间的元素
# print(players[:4])

# # 将取第三个元素到结尾的元素
# print(players[2:])

# # 当范围为负数时，表示从索引是从列表的结尾开始
# print(players[-3:])

# # 可以指定切片的第三个参数，表示指定范围切片每相隔几个元素取下一个元素
# print(players[0::2])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())