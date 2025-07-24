# 动手试一试

# # 练习4.3：数到20　使用一个for循环打印数1～20（含）​。
# values = list(range(1, 21))
# for value in values:
#     print(value)

# # 练习4.4: 100万　创建一个包含数1～1 000 000的列表，再使用一个for循环将这些数打印出来。​（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口。​）
# values = range(1, 1_000_001)
# for value in values:
#     print(value)

# # 练习4.5: 100万求和　创建一个包含数1～1 000 000的列表，再使用min()和max()核实该列表确实是从1开始、到1 000 000结束的。另外，对这个列表调用函数sum()，看看Python将100万个数相加需要多长时间。
# values = range(1, 1_000_001)
# print(min(values))
# print(max(values))
# print(sum(values))

# # 练习4.6：奇数　通过给range()函数指定第三个参数来创建一个列表，其中包含1～20的奇数；再使用一个for循环将这些数打印出来。
# odds = range(1, 20, 1)
# for odd in odds:
#     print(odd)

# # 练习4.7: 3的倍数　创建一个列表，其中包含3～30内能被3整除的数，再使用一个for循环将这个列表中的数打印出来。
# values = range(3, 31, 3)
# for value in values:
#     print(value)

# # 练习4.8：立方　将同一个数乘三次称为立方。例如，在Python中，2的立方用2**3表示。创建一个列表，其中包含前10个整数(1～10)的立方，再使用一个for循环将这些立方数打印出来。
# values = []
# for value in range(1, 11):
#     num = value ** 3
#     values.append(num)
#     print(num)

# # 练习4.9：立方推导式　使用列表推导式生成一个列表，其中包含前10个整数的立方。
# values = [value ** 3 for value in range(1, 11)]
# for value in values:
#     print(value)